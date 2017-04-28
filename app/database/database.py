import os
from app.database.models import *
from app.amity import my_amity
from app.amity.amityClass import rooms
from app.rooms import my_rooms
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database(object):
    """
    This is the Database class that has all methods of creating,
    connecting and reading from the database.

    By using the save_people, save_rooms and save_allocations methods,
        it saves the data from the rooms and people_data dictionary to the
        database.

    Uses the connect_to_db function to connect to the database
        By using the load_people, load_rooms and load_allocations methods,
        it loads the data from the database to the rooms and people_data
        dictionaries.
    """

    def __init__(self):
        self.db = None
        self.amity = my_amity

    def connect_to_db(self, db_name):
        """
        Helper function to connect to database
        """
        self.db = create_engine("sqlite:///" + db_name)
        session = sessionmaker()
        session.configure(bind=self.db)
        Base.metadata.create_all(self.db)

        storage_session = session()
        return storage_session

    def save_state(self, args):
        """
        Takes up an optional argument --db that specifies the
        database to store the data in rooms and people dictionary.
        Creates database and saves data.
        """

        self.db_name = "amity.db"
        if args["--db"]:
            self.db_name = args["--db"]

        if os.path.exists(self.db_name):
            os.remove(self.db_name)

        try:
            save_session = self.connect_to_db(self.db_name)
            self.save_people(save_session)
            self.save_rooms(save_session)
            self.save_allocations(save_session)

            message = "Data has been stored in the {} database".format(
                self.db_name)

        except Exception:
            message = "Error saving data to {}".format(self.db_name)

        save_session.commit()
        save_session.close()

        return message

    def save_people(self, storage_session):
        """
        Loads data from the people_data dict into the database
        """
        try:
            for key, values in my_amity.people_data.items():
                person_id = key
                name = values["name"]
                wants_accommodation = values["accommodation"]
                is_fellow = values["is_fellow"]

                people = People(person_id=person_id, name=name,
                                wants_accommodation=wants_accommodation,
                                is_fellow=is_fellow)
                storage_session.add(people)

            return people
        except Exception:
            return "Failed"

    def save_rooms(self, storage_session):
        """
        Loads data from the rooms dict into the database
        """
        try:
            for key, values in rooms.items():
                room_name = key
                is_office = values["is_office"]
                room_data = Rooms(room_name=room_name, is_office=is_office)

                storage_session.add(room_data)

            return room_data
        except Exception:
            return "Failed"

    def save_allocations(self, storage_session):
        """
        Loads data of room allocations into allocations table
        """
        try:
            for key, values in rooms.items():
                room_name = key
                for identifier in values["occupants"]:
                    occupant_id = identifier

                    allocation_data = Allocations(room_name=room_name,
                                                  occupant_id=occupant_id)
                    storage_session.add(allocation_data)

            return allocation_data
        except Exception:
            return "Failed"

    def load_state(self, args):
        """
        Loads data from a database into the application
        """
        db_name = args["<sqlite_database>"]
        if os.path.exists(db_name):
            sess = self.connect_to_db(db_name)

            try:
                people_from_db = sess.query(People).all()
                rooms_from_db = sess.query(Rooms).all()
                allocations_from_db = sess.query(Allocations).all()

                self.load_people(people_from_db)
                self.load_rooms(rooms_from_db)
                self.load_allocations(allocations_from_db)

                message = "Data successfully added"
            except Exception:
                message = "No Data Added"

            sess.commit()
            sess.close()
        else:
            message = "{} does not exist".format(db_name)

        return message

    def load_people(self, people_from_db):
        """
        Saves data to people dictionary
        """
        message = ""
        for person in people_from_db:
            my_amity.people_data.update({
                person.person_id:
                {'name': str(person.name),
                 'accommodation': str(person.wants_accommodation),
                 'is_fellow': bool(person.is_fellow)}
            })

            message += "{} successfully added\n".format(person.name)
        return message

    def load_rooms(self, rooms_from_db):
        """
        Saves data to rooms dictionary
        """
        message = ""
        for room in rooms_from_db:
            room_name = str(room.room_name)
            is_office = bool(room.is_office)

            rooms.update(
                {room_name: {"occupants": [], "is_office": is_office}})

            message += "{} successfully added\n".format(room_name)
        return message

    def load_allocations(self, allocations_from_db):
        """
        Saves data to people dictionary
        """
        message = ""
        for allocation in allocations_from_db:
            room = rooms.get(str(allocation.room_name), None)
            if room is None:
                message += "{} Not Created".format(str(allocation.room_name))
                return message
            room['occupants'].append(allocation.occupant_id)
            name = my_rooms.get_names(allocation.occupant_id)


            message += "{} successfully added to room {}\n".format(
                name.upper(), str(allocation.room_name))

        return message
