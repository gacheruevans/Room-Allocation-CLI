import unittest

import mock

from tests.person import Person
from tests.room import Room


class AmityTest(unittest.TestCase):
    """This is a test class for rooms and its methods."""

    def setUp(self):
        self.room = Room()
        self.person = Person()

    def test_class_initialize(self):
        self.assertIsInstance(self.room, Room, msg="Cannot create 'Room' instance")

    @mock.patch.dict('person.Person.add', {
        1: {'name': 'EVANS JAMES', 'role': 'Fellow'},
        2: {'name': 'MAUREEN MAINA', 'role': 'Staff'},
        3: {'name': 'LOICE ANDIA', 'role': 'Fellow'},
        4: {'name': 'GILBERT GATHARA', 'role': 'Fellow'}
    })
    def test_look_up_user(self):
        self.get_name = self.room.get_names(2)
        self.get_name_with_wrong_id = self.room.get_names(10)
        self.assertEqual(self.get_name, 'Loice Anida', msg='Wrong Person name retrieved')
        self.assertEqual(self.get_name_with_wrong_id, 'Person Does not exist', msg='Person Exists')

    @mock.patch.dict('room.Room.add', {
        1: {'room_name': 'HOGWARTS', 'room_type': 'Office', 'Occupancy': '6'},
        2: {'room_name': 'VALHALLA', 'room_type': 'Office', 'Occupancy': '6'},
        3: {'room_name': 'LILAC', 'room_type': 'Office', 'Occupancy': '6'},
        4: {'room_name': 'KRYPTON', 'room_type': 'Office', 'Occupancy': '6'}

    })
    def test_look_up_office(self):
        self.get_room_name = self.room.get_room_name(1)
        self.get_room_name_with_wrong_id = self.room.get_room_name(5)
        self.assertEqual(self.get_room_name, 'Hogwarts', msg='Wrong Room name retrieved')
        self.assertEqual(self.get_room_name_with_wrong_id, 'Room Does not exist', msg='Room Exists')

    @mock.patch.dict('room.Room.get_room_max_occupancy', {
        'HOGWARTS': {'is_office': True, 'Occupancy': [3]},
        'VALHALLA': {'is_office': True, 'Occupancy': [6]},
        'LILAC': {'is_office': True, 'Occupancy': [2]},
        'KRYPTON': {'is_office': True, 'Occupancy': [4]}
    })
    @mock.patch.dict('person.Person.personel', {
        1: {'name': 'EVANS JAMES', 'is_fellow': True, 'accomodation': 'Y'},
        2: {'name': 'GILBERT GATHARA', 'is_fellow': False, 'accomodation': 'N'}
    })
    @mock.patch('room.open')
    def test_print_allocations(self, mocked_open):
        # Test print allocations function
        self.print_allocations_without_filename = self.test_room.print_allocations({
            "-o": False, "<filename>": None})
        self.test_room.print_allocations({
            "-o": True, "<filename>": "test_allocations.txt"})

        mocked_open.assert_called_once_with("test_allocations.txt", 'wt')
        self.assertNotEqual(self.print_allocations_without_filename,
                            "", msg="Wrong data printed")
    def test_living_room_max_occupancy(self):
        self.get_room_max_occupancy = self.room.max_occupancy(4)
        self.get_room_wrong_occupancy = self.room.max_occupancy(5)
        self.assertEqual(self.max_occupancy, 'Jade', msg='Wrong Room Occupancy retrieved')
        self.assertEqual(self.get_room_wrong_occupancy, 'Room limit Exceeded', msg='Occupancy Exceeded')

    def test_empty_room(self):
        self.assertTrue(self.room.is_office())

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
