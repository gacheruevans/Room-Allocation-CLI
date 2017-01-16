import unittest
import unittest.mock as mock
from app.rooms.roomClass import Room


class TestRoom(unittest.TestCase):
    """ Holds all tests for rooms."""

    def setUp(self):
        self.test_room = Room()

    @mock.patch.dict("app.person.personClass.Person.people_data", {
        1: {"name": "EVANS GACHERU", "is_fellow": True, "accommodation": "Y"}})
    def test_getting_persons_name_from_people_data(self):
        # Test's whether the record being sought for is in people data
        self.get_name = self.test_room.get_names(1)
        self.get_name_with_wrong_id = self.test_room.get_names(8)
        self.assertEqual(self.get_name, "EVANS GACHERU",
                         msg="Wrong Person name retrieved.")
        self.assertEqual(self.get_name_with_wrong_id,
                         "Person Does Not Exist.", msg="Person Exists")

    @mock.patch.dict("app.amity.amityClass.rooms", {
        "VALHALLA": {"is_office": True, "occupants": [2]},
        "HOGWARTS": {"is_office": True, "occupants": [3]},
        "OCULUS": {"is_office": True, "occupants": [4]},
        "PYTHON": {"is_office": False, "occupants": [2]}
    })
    @mock.patch.dict("app.person.personClass.Person.people_data", {
        1: {"name": "EVANS GACHERU", "is_fellow": True, "accommodation": "Y"},
        2: {"name": "Evans MUSOMI", "is_fellow": False, "accommodation": "N"}})
    @mock.patch("app.rooms.roomClass.open")
    def test_print_allocations(self, mocked_open):
        # Test Print allocations function
        self.print_allocations_without_filename = self.test_room.print_allocations({
            "-o": False, "<filename>": None})
        self.test_room.print_allocations({
            "-o": True, "<filename>": "test_allocations.txt"})
        mocked_open.assert_called_once_with("test_allocations.txt", "wt")
        self.assertNotEqual(
            self.print_allocations_without_filename, "", msg="Wrong data printed ")

    @mock.patch.dict("app.amity.amityClass.rooms", {
        "KRYPTON": {"is_office": True, "occupants": []}})
    @mock.patch.dict("app.person.personClass.Person.people_data", {
        1: {"name": "EVANS GACHERU", "is_fellow": True, "accommodation": "Y"}})
    @mock.patch("app.rooms.roomClass.open")
    def test_print_unallocated(self, mocked_open):
        # Test print unallocated
        self.print_unallocated_without_filename = self.test_room.print_unallocated({
            "-o": False, "<filename>": None})
        self.test_room.print_unallocated({
            "-o": True, "<filename>": "test_unallocated.txt"})
        self.assertIn(
            "EVANS GACHERU", self.print_unallocated_without_filename, msg="Wrong data printed")
        mocked_open.assert_called_once_with("test_unallocated.txt", "wt")

    @mock.patch.dict("app.amity.amityClass.rooms", {
        "PYTHON": {"is_office": False, "occupants": [2]},
        "GO": {"is_office": False, "occupants": []}})
    @mock.patch.dict("app.person.personClass.Person.people_data", {
        1: {"name": "EVANS GACHERU", "is_fellow": True, "accommodation": "Y"}})
    def test_print_room(self):
        # Test print rooms
        self.printing_non_existent_room = self.test_room.print_room(
            {"<room_name>": "LONGONOT"})
        self.assertEqual(self.printing_non_existent_room,
                         "LONGONOT Room Does Not Exist")
        self.printing_existent_room = self.test_room.print_room(
            {"<room_name>": "PYTHON"})
        self.assertNotEqual(self.printing_existent_room,
                            "", msg="Room Does Not Exist")
        self.printing_empty_room = self.test_room.print_room(
            {"<room_name>": "GO"})
        self.assertIn("No Occupants", self.printing_empty_room,
                      msg="Room has no occupants")

if __name__ == '__main__':
    unittest.main()
