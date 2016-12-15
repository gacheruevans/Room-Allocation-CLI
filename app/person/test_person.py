# coding=utf-8
import unittest
import mock

from personClass import Person

class TestPerson(unittest.TestCase):

    def Setup(self):
        self.person = Person()

    def test_add_person(self):
        """Test adding person"""
        new_person = {
            '<first_name>':'EVANS',
            '<last_name>': 'GACHERU',
            'Fellow': True,
            'Staff':False,
            '<wants accommodation>':'Y'
        }
        add_person = self.test_add_person(new_person)
        add_person_twice = self.test_add_person(new_person)
        self.assertIn('EVANS GACHERU', add_person,msg='Person not added.')
        self.assertEqual('EVANS GACHERU', add_person_twice, msg='Person already exists.')

    @mock.patch('personClass.open')
    @mock.patch('personClass.Person.add_person')
    def test_load_people_from_a_text_file(self, mocked_add_person, mocked_open):

        self.test_person.load_people({"<filename>": "non_existent.txt"})
        mocked_open.assert_called_once_with("non_existent.txt", 'r')

        sample_txt_data = "STEVEN NJOROGE FELLOW Y\n ALEX KIURA FELLOW Y\n DOMINIC WALTERS STAFF\n MAUREEN MAINGI STAFF\n"

        with mock.patch('builtins.open', mock.mock_open(read_data=sample_txt_data)) as mock_file:
            mock_read_line =open("try.txt").readline()
            assert mock_file.called
        mock_file.assert_called_once_with("try.txt")
        self.assertEqual(mock_read_line, "STEVEN NJOROGE FELLOW Y\n")

        mocked_add_person.return_value = "STEVEN NJOROGE has been allocated No office and No livingSpace\n"
        self.assertEqual("STEVEN NJOROGE has been allocated No office and No livingSpace\n",
                         mocked_add_person.return_value, msg="Person not added from file")

    @mock.patch.dict('app.amity.amityClass.rooms',{'OCULUS': {'is_office': True, 'occupants':[]}})
    def test_office_allocation_in_add_person(self):

        #Tests if person is added and is allocated an office
        sample_staff = {"<first_name>":"JOHN",
                        "<last_name>": "DOE",
                        "Fellow":False,
                        "Staff":True,
                        "<wants_accommodation>":None
                        }
        self.test_allocate_office = self.test_person.add_person(sample_staff)
        self.assertRaises(Exception, self.test_allocate_office, msg="Person not allocated office")

    @mock.patch.dict('app.amity.amityClass.rooms',{
        'HOGWARTS':{'is_office':True, 'occupants':[]},
        'PYTHON':{'is_office':False, 'occupants':[]}})
    def test_allocation_of_office_and_living_space_when_adding_fellow(self):

        #Tests if fellow is added and allocated an office and living space
        sample_fellow = {"<first_name>":"MIKE",
                         "<last_name>":"KAMAU",
                         "Fellow":True,
                         "Staff":False,
                         "<wants_accommodation>":'Y'
                        }
        self.test_adding_fellow = self.test_person.addd_person(sample_fellow)
        self.assertIn("PYTHON", self.test_adding_fellow, msg="Person allocated living space")

    @mock.patch.dict('app.amity.amityClass.rooms',{
        'HOGWARTS':{'is_office':True, 'occupants':[3]},
        'VALHALLA':{'is_office':True, 'occupants':[3]},
        'KRYPTON':{'is_office':True, 'occupants':[2]},
        'OCULUS':{'is_office':True, 'occupants':[6]},
        'MODOR':{'is_office':True, 'occupants':[4]},
        'PYTHON':{'is_office':False, 'occupants':[2]},
        'GO':{'is_office':False, 'occupants':[2]},
        'PHP':{'is_office': False, 'occupants':[1]}})
    @mock.patch.dict('personClass.people_data',{
        1:{'name':'EVANS GACHERU', 'is_fellow':True, 'accommodation':'Y'},
        2:{'name':'KAREN KINOTI', 'is_fellow':False, 'accomodation':'N'}})
    def test_reallocation_room(self):
        #Test reallocation of rooms

        self.reallocate = self.test_person.reallocate_person({"<person_name>":"GACHERU","<new_room_name>":"OCULUS"})
        self.assertIn("Allocated OCULUS", self.reallocate, msg="Person Successfully allocated")

        self.allocate_to_full_room = self.test_person.reallocate({"<person_name>":"STEVEN", "<new_room_name>":"OCULUS"})
        self.assertIn("full", self.reallocate_to_full_room, msg="Person can not be reallocated")

        self.reallocate_staff_living_space = self.test_person.reallocate_person({"<person_name>":"KINOTI","<new_room_name>":"GO"})
        self.assertEqual(self.reallocate_living_space, "STAFF CANNOT BE ALLOCATED LIVING SPACE",
                         msg="Staff Not Allocated Living Space")

        self.reallocate = self.test_person.reallocate_person({"<person_name>":"GACHERU","<new_room_name>":"GO"})
        self.assertIn()
