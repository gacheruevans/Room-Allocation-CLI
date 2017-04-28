import unittest
from app.person.staffClass import Staff


class TestStaff(unittest.TestCase):
    """ This is a staff initialization """

    def setUp(self):
        self.test_staff = Staff()

    def test_class_initialization(self):
        self.assertIsInstance(self.test_staff, Staff,
                              msg="Cannot Create Staff instance")
