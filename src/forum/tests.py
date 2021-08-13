from django.test import TestCase

from forum.models import Section


class SectionTest(TestCase):
    
    def test_is_top_section(self):
        top_section = Section(name="Top section")
        self.assertTrue(top_section.is_top_section())
    
    def test_is_not_top_section(self):
        top_section = Section(name="Top section")
        second_section = Section(name="Second section", parent=top_section)
        self.assertFalse(second_section.is_top_section())
