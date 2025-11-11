from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import IntegrityError
from .models import User, Room, Message
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MessageForm, RoomForm

# Create your views here.
@csrf_exempt
def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = RoomForm(request.POST)
            if form.is_valid():
                room = form.save()
                room.participants.add(request.user)
                return redirect("room", room_name=room.name)
        else:
            form = RoomForm()   # ✅ this now works fine

        return render(request, "chat/index.html", {
            "rooms": Room.objects.filter(participants=request.user),
            "form": form,
        })
    else:
        return HttpResponseRedirect(reverse("login"))



def room(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    messages = room.messages.all().order_by('timestamp')
    return render(request, 'chat/room.html',{
        "room":room,
        "messages":messages,
    })





def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "chat/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "chat/login.html")
    

def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "chat/register.html",{
                "message" : "passwords must match"
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, 'chat/register.html',{
                "message" : "Email has already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "chat/register.html")
    

    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))