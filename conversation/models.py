from django.contrib.auth.models import User
from django.db import models

from Element.models import Element

class Conversation(models.Model):
    element = models.ForeignKey(Element, related_name='conversation', on_delete=models.CASCADE)
    membres = models.ManyToManyField(User, related_name='conversation')
    cree_a = models.DateTimeField(auto_now_add=True)
    modifie_a = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modifie_a',)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    contenu = models.TextField()
    cree_a = models.DateTimeField(auto_now_add=True)
    cree_par = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)

