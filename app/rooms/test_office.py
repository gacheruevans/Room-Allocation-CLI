import unittest
from app.rooms.officeClass import Office

class TestOffice(unittest.TestCase):
    """This tests Office initialization """
    def setUp(self):
        self.test_office = Office()

    def test_class_initialization(self):
        self.assertIsInstance(self.test_office, Office, msg = "Cannot create Office instance")