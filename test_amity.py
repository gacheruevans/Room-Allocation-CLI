import unittest

from tests.person import Person
from tests.room import Room


class AmityTest(unittest.TestCase):

    def setUp(self):
        self.room = Room()

    def test_look_up_room(self):
        self.room.add('Living Space', 'Python','Office')
        self.assertEqual('Python', self.room.lookup('Living Space', 'Office'))

    def test_normal_entries_is_consistent(self):
        self.room.add('Living Space', 'Go')
        self.room.add('Living Space', 'PHP')
        self.room.add('Office Space', 'valhalla')
        self.assertTrue(self.room.is_consistent())

    def test_adds_roomType_roomName(self):
        self.room.add('Living Space')

    def test_livingroom_max_occupancy(self):
        pass


    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.room.lookup('Missing')

    def test_empty_room(self):
        self.assertTrue(self.room.is_office())

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
