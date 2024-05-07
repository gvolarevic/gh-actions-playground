from unittest import TestCase

from src.functions import greet


class TestFunctions(TestCase):
    def test_greet_alice(self):
        result = greet("Alice")
        self.assertEqual(result, "Hello, Alice")

    def test_greet_bob(self):
        result = greet("Bob")
        self.assertEqual(result, "Hello, Bob")
