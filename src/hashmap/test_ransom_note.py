from unittest import TestCase
from ransom_note import checkMagazine


class TestcheckMagazine(TestCase):
    def test_check_magazine(self):
        self.assertEqual(checkMagazine("two times three is not four", "two times two is four"), "No")

        self.assertEqual(checkMagazine("give me one grand today night", "give one grand today"), "Yes")
