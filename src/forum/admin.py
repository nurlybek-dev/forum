from django.contrib import admin

from .models import Section

class SectionInline(admin.TabularInline):
    model = Section
    extra = 0


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_top_section',)
    list_filter = (
        ('parent', admin.BooleanFieldListFilter),
    )
    search_fields = ('name',)
    ordering = ('name',)
    inlines = (
        SectionInline,
    )
