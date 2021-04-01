from unittest import TestCase
from main import Hello


class TestHello(TestCase):
    def test_hello(self):
        self.hi = Hello()


class TestInit(TestHello):
    def test_Initial_Reply(self):
        self.assertEqual(self.hi, "Hello")
