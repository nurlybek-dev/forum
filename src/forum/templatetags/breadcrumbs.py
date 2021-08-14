from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag(takes_context=True)
def breadcrumbs(context):
    if 'section' in context:
        section = context['section']
    elif 'topic' in context:
        section = context['topic'].section
    else:
        section = None

    index_url = reverse('index')
    sections = []
    while section != None:
        sections.append(f'<span><a href="{section.get_absolute_url()}">{section.name}</a></span>')
        section = section.parent
    sections.append(f'<span><a href="{index_url}">Форум</a></span>')
    sections.reverse()
    return mark_safe(" > ".join(sections))
