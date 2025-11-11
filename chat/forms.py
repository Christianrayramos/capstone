from django import forms
from .models import Room, Message
from django.contrib.auth.models import User

class MessageForm (forms.ModelForm):
    class meta:
        model = Message
        fields = ['content']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'participants']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter room name'}),
            'participants' : forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
    