import unittest
#import mock

from app.person.personClass import Person


class AmityTest(unittest.TestCase):
    """This is a test class for rooms  and persons and their methods."""

    def setUp(self):
        self.person = Person()

    #@mock.patch("person.add_person")
    def test_adding_person(self):
        self.assertEqual("EVANS GACHERU", self.person.add_person("EVANS", "GACHERU"))

    def test_adding_room(self):
        pass

    def test_room_occupancy(self):
        pass


if __name__ == '__main__':
    unittest.main()
