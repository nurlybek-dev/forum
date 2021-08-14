from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from forum.forms import MessageForm, TopicForm

from .models import Section, Topic


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
    form = MessageForm()
    context = {
        'topic': topic,
        'form': form
    }
    return render(request, 'forum/topic.html', context=context)


@login_required
def message_create(request, topic):
    topic = Topic.objects.get(pk=topic)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.topic = topic
            instance.author = request.user
            instance.save()
    
    return redirect(reverse('topic', kwargs={'pk': topic.pk}))


@login_required
def topic_create(request, section):
    section = Section.objects.get(pk=section)

    if section.is_top_section():
        return redirect(reverse('section', kwargs={'pk': section.pk}))

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            instance = form.save(section, request.user)
            return redirect(reverse('topic', kwargs={'pk': instance.pk}))
    else:
        form = TopicForm()

    context = {
        'section': section,
        'form': form
    }

    return render(request, 'forum/topic_create.html', context=context)
