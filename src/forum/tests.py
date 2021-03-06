from django.test import TestCase
from django.template import Context, Template
from users.models import User

from forum.models import Message, Section, Topic


class SectionTest(TestCase):
    
    def test_is_top_section(self):
        top_section = Section(name="Top section")
        self.assertTrue(top_section.is_top_section())
    
    def test_is_not_top_section(self):
        top_section = Section(name="Top section")
        second_section = Section(name="Second section", parent=top_section)
        self.assertFalse(second_section.is_top_section())
    
    def test_get_last_message(self):
        user = User.objects.create(username="user", email="user@email.com", password="testuser123")
        section = Section.objects.create(name="Section")
        topic = Topic.objects.create(name="Topic", section=section, author=user)
        message = Message.objects.create(topic=topic, author=user, text="Text")
        self.assertEqual(section.get_last_message(), message)
        self.assertEqual(section.get_last_message().topic, topic)
    
    def test_get_empty_last_message(self):
        section = Section.objects.create(name="Section")
        self.assertIsNone(section.get_last_message())


class TopicTest(TestCase):
    def test_get_last_message(self):
        user = User.objects.create(username="user", email="user@email.com", password="testuser123")
        section = Section.objects.create(name="Section")
        topic = Topic.objects.create(name="Topic", section=section, author=user)
        message = Message.objects.create(topic=topic, author=user, text="Text")
        self.assertEqual(topic.get_last_message(), message)
    
    def test_get_empty_last_message(self):
        user = User.objects.create(username="user", email="user@email.com", password="testuser123")
        section = Section.objects.create(name="Section")
        topic = Topic.objects.create(name="Topic", section=section, author=user)
        self.assertIsNone(topic.get_last_message())


class BreadcrumbsTemplateTagTest(TestCase):

    def setUp(self):
        self.section1 = Section.objects.create(name='Level 1')
        self.section2 = Section.objects.create(name='Level 2', parent = self.section1)
        self.section3 = Section.objects.create(name='Level 3', parent = self.section2)
        self.template_to_render = Template(
            '{% load breadcrumbs %}'
            '{% breadcrumbs %}'
        )

    def test_rendered_level_1_section(self):
        context = Context({'section': self.section1})
        rendered_template = self.template_to_render.render(context)
        self.assertInHTML('<span><a href="/">??????????</a></span>'
        ' &gt; <span><a href="/section/1/">Level 1</a></span>',
        rendered_template)

    def test_rendered_level_2_section(self):
        context = Context({'section': self.section2})
        rendered_template = self.template_to_render.render(context)
        self.assertInHTML(
            '<span><a href="/">??????????</a></span>'
            ' &gt; <span><a href="/section/1/">Level 1</a></span>'
            ' &gt; <span><a href="/section/2/">Level 2</a></span>',
            rendered_template)

    def test_rendered_level_3_section(self):
        context = Context({'section': self.section3})
        rendered_template = self.template_to_render.render(context)
        self.assertInHTML(
            '<span><a href="/">??????????</a></span>'
            ' &gt; <span><a href="/section/1/">Level 1</a></span>'
            ' &gt; <span><a href="/section/2/">Level 2</a></span>'
            ' &gt; <span><a href="/section/3/">Level 3</a></span>',
            rendered_template)

    def test_rendered_topic(self):
        topic = Topic(section=self.section2, name='Level 2 Topic')
        context = Context({'topic': topic})
        rendered_template = self.template_to_render.render(context)
        self.assertInHTML(
            '<span><a href="/">??????????</a></span>'
            ' &gt; <span><a href="/section/1/">Level 1</a></span>'
            ' &gt; <span><a href="/section/2/">Level 2</a></span>',
            rendered_template)

    def test_rendeded_section_topic(self):
        topic = Topic(section=self.section1, name='Level 1 Topic')
        context = Context({'section': self.section1, 'topic': topic})
        rendered_template = self.template_to_render.render(context)
        self.assertInHTML(
            '<span><a href="/">??????????</a></span>'
            ' &gt; <span><a href="/section/1/">Level 1</a></span>',
            rendered_template)

    def test_rendered_no_section_no_topic(self):
        context = Context({})
        rendered_template = self.template_to_render.render(context)
        self.assertInHTML(
            '<span><a href="/">??????????</a></span>',
            rendered_template)
