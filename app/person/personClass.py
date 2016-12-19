import random

from app.amity.test_amity import rooms

people_data = {}

class Person(object):
    """
    This is the Person class that has all methods of adding a person,
    loading people from a text file and allocating them rooms.
    sample people_data dictionary:
        people_data = {
            1:{'name': 'EVANS GACHERU', 'is_fellow': True, 'accomodation': 'Y'},
            2:{'name': 'EVANS MUSOMI', 'is_fellow': False, 'accomodation': 'N'},
        }
    """
    def __init__(self):
        self.person_name = None

    def add_person(self, args):
        """
        Adds a person to the People_data dictionary
        allocates the person to a random room.
        """

        person_name = "{} {}".format(args["<first_name>"], args["<last_name>"])
        person_name = person_name.upper()
        wants_accommodation = 'N'
        is_fellow = args['Fellow']

        self.person_identifier = len(people_data) + 1

        if args["<wants_accommodation>"]:
            wants_accommodation = args["<wants_accommodation>"]

        for person in people_data:
            if people_data[person]['name'] == person_name:
                message = "{} Already Exists\n".format(person_name)
                return message

        people_data.update({
            self.person_identifier: {
                'name': person_name,
                'accommodation': wants_accommodation,
                'is_fellow': is_fellow}
        })

        message = self.allocate_rooms(self.person_identifier)

        return message

    def allocate_person_room(self, identifier):
        """Allocates a person their respective office and living room based on whether they are a staff or fellow"""

        available_living_spaces = []
        available_offices = []

        allocated_living_space = "No"
        allocated_offices = "No"

        person = people_data.get(identifier, None)

        for room in rooms:
            if rooms [room]["is_office"] and len(rooms[room]["occupants"]) < 6:
                available_offices.append(room)
            if not room[room]["is_living_space"] and len(rooms[room]["occupants"]) < 4:
                available_living_spaces.append(room)

        if len(available_offices) > 0:
            allocated_offices = random.choice(available_offices)
            rooms[allocated_offices] ["occupants"].append(identifier)

        if person["accommodation"] == "Y":
            if person["is_fellow"] and len(available_living_spaces) > 0:
                allocated_living_space = random.choice(available_living_spaces)
                rooms[allocated_living_space] ["occupants"].append(identifier)

        message ="{} has not been allocated {} office and {} living space\n".format(
            people_data[identifier]["name"], allocated_offices, allocated_living_space)
        return message

    def reallocate_person(self, args):
        """Reallocated person a new room"""
        person_name = args["person_name"].upper()
        new_room = args["new_room"].upper()

        for person in people_data:
            if person_name in people_data[person]['name']:
                person_identifier = person

            new_room_type = rooms[new_room]["is_office"]
            #Find current allocated room and remove identifier
            for current_room in rooms:
                current_room_type = rooms[current_room]["is_office"]
                if new_room_type and current_room_type:
                    if person_identifier in rooms[current_room]["occupants"]:
                        rooms[current_room]["occupants"].remove(person_identifier)

            #Append identifier to new_room
            if rooms[new_room]["is_office"] and len(rooms[new_room]["occupants"]) < 6:
                rooms[new_room]["occupants"].append(person_identifier)
                message = "{} has been reallocated {} romm\n".format(person_name, new_room)
                return message

            if not rooms[new_room]["is_office"] and len(rooms[new_room]["occupants"]):
                if people_data[person_identifier]["is_fellow"]:
                    rooms[new_room]["occupants"].append(person_identifier)
                    message = "{} has been reallocated {} room\n".format(person_name, new_room)
                    return message

                if not people_data[person_identifier]["is_fellow"]:
                    return "Staff CANNOT be Allocated Living Space"
            return "{} is full".format(new_room)

    def remove_person(self, args):
        """Delete's a person from a room"""
        for person_id, person_info in people_data.items():
            if args["<person_name>"].upper() in person_info["name"]:
                #Remove's the item at the given position in the list and returns it.
                if people_data.pop(person_id):
                    for current_room in rooms:
                        if person_id in rooms[current_room]["occupants"]:
                            rooms[current_room]["occupants"].remove(person_id)
                        #Returns a copy of the string in which all case-based characters have been uppercased
                        return "{} has been deleted".format(args["<person_name>"].upper())
        return "{} not found".format(args["<person_name>"].upper())

    def load_people(self, args):
        """Add people to rooms from a .txt file"""
        message = ""

        with open(args["<filename>"], 'r') as input_file:
            people = input_file.readlines()
            for person in people:
                person = person.split()
                if person:
                    is_fellow = True
                    is_staff = False
                    wants_accommodation = None

                    if "STAFF" in person:
                        is_fellow = False
                        is_staff = True

                    if "YES" in person:
                        wants_accommodation = "Y"

                    arg_dict = ({
                        "<first_name>":person[0],
                        "<last_name>":person[1],
                        "Staff":is_staff,
                        "Fellow":is_fellow,
                        "<wants_accommodation>":wants_accommodation
                    })
                    message += self.add_person(arg_dict)
        return message