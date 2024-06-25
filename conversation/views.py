from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from Element.models import Element

from .forms import ConversationMessageForm
from .models import Conversation

@login_required
def new_conversation(request, element_pk):
    element = get_object_or_404(Element, pk=element_pk)

    if element.creer_par == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(element=element).filter(membres__in=[request.user.id])

    if conversations:
        pass # redirect to conversation

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(element=element)
            conversation.membres.add(request.user)
            conversation.membres.add(element.creer_par)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.cree_par = request.user
            conversation_message.save()

            return redirect('Element:detail', pk=element_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(membres__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })
