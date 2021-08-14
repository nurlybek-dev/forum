from django.shortcuts import render

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
    context = {
        'topic': topic
    }
    return render(request, 'forum/topic.html', context=context)
