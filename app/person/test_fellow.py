import unittest
from app.person.fellowClass import Fellow

class TestFellow(unittest.TestCase):
    """ This is a fellow initialization"""
    def setUp(self):
        self.test_fellow =Fellow()

    def test_class_initialization(self):
        self.assertIsInstance(self.test_fellow, Fellow, msg =" Cannot Create Fellow Instance")