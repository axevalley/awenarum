from django import forms
from contactform.models import Message


class MessageForm(forms.Form):
    email = forms.CharField(max_length=50)
    message_type = forms.ChoiceField(
        choices=Message.MESSAGE_TYPE_CHOICES, widget=forms.RadioSelect())
