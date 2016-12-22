import unittest
from app.amity.amityClass import Amity, rooms


class TestAmity(unittest.TestCase):
    """ Class contains method tests for creating rooms and getting rooms"""

    def setUp(self):
        self.test_amity = Amity()
        self.test_create_single_room = self.test_amity.create_room(
            {"<room_name>": ["OCULUS"]}, "O")

    def test_get_room_type(self):
        self.get_room_type = self.test_amity.get_room_type("O")
        self.assertEqual(self.get_room_type, "O",
                         msg="Wrong room type returned")

    def test_creation_of_rooms(self):
        # Test for creation of multiple offices
        self.test_amity.create_room(
            {"<room_name>": ["KRYPTON", "HOGWARTS"]}, "O")

        # Test or creation of multiple living spaces
        self.test_amity.create_room({"<room_name>": ["GO", "PHP"]}, "L")

        self.assertIn("OCULUS", self.test_create_single_room,
                      msg="Room Not Created")
        # All the key/value pairs in dictionary exist in rooms
        self.assertDictContainsSubset({
            "GO": {"occupants": [], "is_office": False},
            "KRYPTON": {"occupants": [], "is_office": True},
            "PHP": {"occupants": [], "is_office": False},
            "HOGWARTS": {"occupants": [], "is_office": True}},
            rooms, msg="Multiple Rooms were not created")

    def test_adding_rooms_twice(self):
        # Test if room is added twice
        self.adding_rooms_twice = self.test_amity.create_room(
            {"<room_name>": ["OCULUS"]}, "O")
        self.assertIn("OCULUS Exists \n",
                      self.adding_rooms_twice, msg="Room added twice")


if __name__ == '__main__':
    unittest.main()
