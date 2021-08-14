from django.shortcuts import redirect, render
from django.urls import reverse

from forum.forms import MessageForm

from .models import Message, Section, Topic


def index(request):
    sections = Section.objects.filter(parent__isnull=True)
    context = {
        'sections': sections
    }
    return render(request, 'forum/index.html', context=context)


def section(request, pk):
    section = Section.objects.get(pk=pk)
    context = {
        'section': section
    }
    return render(request, 'forum/section.html', context=context)


def topic(request, pk):
    topic = Topic.objects.get(pk=pk)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.topic = topic
            instance.author = request.user
            instance.save()
            return redirect(reverse('topic', kwargs={'pk': pk}))
        
    else:
        form = MessageForm()
    context = {
        'topic': topic,
        'form': form
    }
    return render(request, 'forum/topic.html', context=context)
