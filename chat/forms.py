from django import forms
from .models import Room, Message

class MessageForm (forms.ModelForm):
    class meta:
        model = Message
        fields = ['content']