import unittest
from livingspaceClass import LivingSpace

class TestLivingSpace(unittest.TestCase):
    """This tests living space initialization"""
    def setUp(self):
        self.test_living_space = LivingSpace()

    def test_class_initialization(self):
        self.assertIsInstance(self.test_living_space, LivingSpace, msg = "Cannot Create Living Space instance")