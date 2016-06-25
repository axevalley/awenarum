from django.db import models
from django.forms import ModelForm


class Message(models.Model):
    REQUEST = 'R'
    QUERY = 'Q'
    FEEDBACK = 'F'
    OTHER = 'O'
    MESSAGE_TYPE_CHOICES = (
        (REQUEST, 'Request'),
        (QUERY, 'Query'),
        (FEEDBACK, 'Feedback'),
        (OTHER, 'Other')
    )
    email = models.CharField(max_length=50)
    message_type = models.CharField(
        max_length=30, choices=MESSAGE_TYPE_CHOICES)
    message = models.TextField()


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['email', 'message_type', 'message']
