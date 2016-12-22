import unittest
import mock
from app.database.database import Database


class testDatabase(unittest.TestCase):
    """
    This is Test class for Database methods.
    It contains tests for the save_state and load_state methods.
    """

    def setUp(self):
        self.test_database = Database()

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_database, Database,
            msg="Cannot create `Database` instance")

    @mock.patch('app.database.Database.connect_to_db')
    def test_database_creation(self, mocked_connection):
        # Test database methods
        self.test_sample_database = mocked_connection(
            "test_database.db")
        mocked_connection.assert_called_once_with("test_database.db")

    @mock.patch.dict('app.amity.amityClass.rooms', {
        'KRYPTON': {'is_office': True, 'occupants': [2]},
        'VALHALLA': {'is_office': True, 'occupants': [1]},
        'PYTHON': {'is_office': False, 'occupants': [1]}})
    @mock.patch.dict('app.person.personClass.Person.people_data', {
        1: {'name': ' EVANS GACHERU', 'is_fellow': True, 'accomodation': 'Y'},
        2: {'name': 'KAREN KINOTI', 'is_fellow': False, 'accomodation': 'N'}})
    @mock.patch('app.database.Database.save_state')
    @mock.patch('app.database.Database.connect_to_db')
    def test_database_save_state_method(self, mocked_connection, mocked_save_state):
        # Test methods for saving to the database
        mocked_connection("test_database.db")
        self.test_save_people = self.test_database.save_people(
            mocked_connection)
        self.assertNotEqual(self.test_save_people,
                            "Failed", msg="People not added to database")

        self.test_save_rooms = self.test_database.save_rooms(
            mocked_connection)
        self.assertNotEqual(self.test_save_rooms,
                            "Failed", msg="Rooms not added to database")

        self.test_save_allocations = self.test_database.save_allocations(
            mocked_connection)
        self.assertNotEqual(self.test_save_allocations,
                            "Failed", msg="Allocations not added to database")

        self.test_save_state_with_dbname = mocked_save_state(
            "test_database.db")
        mocked_connection.assert_called_once_with("test_database.db")
        mocked_save_state.assert_called_once_with("test_database.db")

    @mock.patch('app.database.Database.load_state')
    @mock.patch('app.database.Database.connect_to_db')
    def test_database_load_state_method(self, mocked_connection, mocked_load_state):
        # Test Load state methods
        mocked_connection("test_database.db")
        mocked_connection.assert_called_once_with("test_database.db")
        self.load_people = self.test_database.load_people(
            mocked_connection)
        self.assertNotEqual(self.load_people,
                            "Failed", msg="People not loaded")

        self.test_load_rooms = self.test_database.load_rooms(
            mocked_connection)
        self.assertNotEqual(self.test_load_rooms,
                            "Failed", msg="Rooms not loaded")

        self.test_load_allocations = self.test_database.load_allocations(
            mocked_connection)
        self.assertNotEqual(self.test_load_allocations,
                            "Failed", msg="Allocations not loaded")
        load_state = mocked_load_state("test_database.db")
        load_state.return_value = "Data successfully added"
        self.assertEqual(load_state.return_value,
                         "Data successfully added",
                         msg="Data not added from the database")

        load_state_failure = mocked_load_state("")
        load_state_failure.return_value = Exception
        self.assertEqual(Exception, load_state_failure.return_value,
                         msg="Exception not raised")

        load_state_with_non_existing_db = mocked_load_state({
            "<sqlite_database>": "test.db"})
        load_state_with_non_existing_db.return_value = "test.db does not exist"
        self.assertEqual(load_state_with_non_existing_db.return_value,
                         "test.db does not exist",
                         msg="Database Exists")


if __name__ == '__main__':
    unittest.main()