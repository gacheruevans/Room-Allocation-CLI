import unittest

from room import Room


class AmityTest(unittest.TestCase):

    def setUp(self):
        self.room = Room()

    def test_look_up_room(self):
        self.room.add('Living Space', 'Python')
        self.assertEqual('Python', self.room.lookup('Living Space'))

    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.room.lookup('Missing')

if __name__ == '__main__':
    unittest.main()

