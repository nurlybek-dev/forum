from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def breadcrumbs(section):
    sections = []
    while section != None:
        sections.append(f'<span><a href="{section.get_absolute_url()}">{section.name}</a></span>')
        section = section.parent
    sections.reverse()
    return mark_safe(" > ".join(sections))
