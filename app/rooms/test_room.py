# coding=utf-8
import unittest
import mock
import roomClass import Room

class TestRoom(unittest.TestCase):
    """ """
    def setUp(self):
        self.test_room = Room()

    @mock.patch.dict("person.personClass.people_data", {
        1:{"name":"EVANS GACHERU", "is_fellow": True, "accommodation":"Y"}})
    def test_getting_persons_name_from_people_data(self):
        #Test's whether the record being sought for is in people data
        self.get_name = self.test_room.get_names(1)
        self.get_name_with_wrong_id = self.test_room.get_names(8)
        self.assertEqual(self.get_name, "EVANS GACHERU", msg = "Wrong Person name retrieved.")
        self.assertEqual(self.get_name_with_wrong_id, "Person Does not exist", msg= "Person Exists")

    @mock.patch.dict("amity.amityClass.rooms", {})