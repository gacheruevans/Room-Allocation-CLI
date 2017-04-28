import random

rooms = {}


class Amity(object):
    """
    class contains methods for getting room type, \
    creating room type and listing rooms to be added.
    """
    people_data = {
        1: {'name': 'EVANS GACHERU', 'is_fellow': True, 'accomodation': 'Y'},
        2: {'name': 'EVANS MUSOMI', 'is_fellow': False, 'accomodation': 'N'},
    }

    def get_room_type(self, room_type=None):
        """ Gets room type from user after the create room command"""
        room_type = room_type

        # Assign a group of rooms to a room type
        while room_type not in ["O", "L"]:
            room_type = input(
                "Enter room type: \n o: Office Space \n l: Living Space: \n")
            room_type = room_type.upper()
        return room_type

    def create_room(self, args, room_type=None):
        """Allows a user to input a list of room names specifying \
            whether they are office or living space
        """
        room_type = room_type

        room_type = self.get_room_type(room_type)
        is_office = False

        if room_type == "O":
            is_office = True

        # Adds rooms to the rooms dict
        for room in args["<room_name>"]:
            if room.upper() in rooms:
                message = "{} Exists \n".format(room.upper())
                return message

            rooms[room.upper()] = {"occupants": [], "is_office": is_office}
            message = "You have the following rooms\n"
            message += "\n".join(rooms.keys())

        return message

    def add_person(self, args):
        """
        Adds a person to the People_data dictionary
        allocates the person to a random room.
        """

        # converts new person details(first name, last name)to capital letters
        person_name = "{} {}".format(args["<first_name>"], args["<last_name>"])
        person_name = person_name.upper()
        is_fellow = args["Fellow"]
        wants_accommodation = 'N'
        if args["<wants_accommodation>"]:
            wants_accommodation = args["<wants_accommodation>"].upper()

        # This ensures last record isn't over written by adding new person
        # record after last existing id.
        self.person_identifier = len(Amity.people_data) + 1

        if args["<wants_accommodation>"] == "Y":

            for person in Amity.people_data:
                if Amity.people_data[person]['name'] == person_name:
                    message = "{} Already Exists\n".format(person_name)
                    return message

            Amity.people_data.update({
                self.person_identifier: {
                    'name': person_name,
                    'accommodation': wants_accommodation,
                    'is_fellow': is_fellow}
            })

            message = self.allocate_person_room(self.person_identifier)

            return message
        else:
            for person in Amity.people_data:
                if Amity.people_data[person]['name'] == person_name:
                    message = "{} Already Exists\n".format(person_name)
                    return message

            Amity.people_data.update({
                self.person_identifier: {
                    'name': person_name,
                    'accommodation': wants_accommodation,
                    'is_fellow': is_fellow}
            })

            message = self.allocate_person_room(self.person_identifier)

            return message

    def allocate_person_room(self, identifier):
        """Allocates a person their respective office and \
        living room based on whether they are a staff or fellow."""

        available_living_spaces = []
        available_offices = []

        allocated_living_space = "No"
        allocated_offices = "No"

        person = Amity.people_data.get(identifier, None)

        for room in rooms:
            if person["accommodation"] == "Y" and person["is_fellow"]:
                if rooms[room]["is_office"] and len(
                        rooms[room]["occupants"]) < 6:
                    available_offices.append(room)

                if not rooms[room]["is_office"] and len(
                        rooms[room]["occupants"]) < 4:
                    available_living_spaces.append(room)

            if person["accommodation"] == "N" and person["is_fellow"]:
                if rooms[room]["is_office"] and len(
                        rooms[room]["occupants"]) < 6:
                    available_offices.append(room)

            if not person["is_fellow"] == "Y" and person["accommodation"]:
                if rooms[room]["is_office"] and len(
                        rooms[room]["occupants"]) < 6:
                    available_offices.append(room)

        if len(available_offices) > 0:
            allocated_offices = random.choice(available_offices)
            rooms[allocated_offices]["occupants"].append(identifier)

        if person["accommodation"] == "Y" and person["is_fellow"]:
            if len(available_living_spaces) > 0:
                allocated_living_space = random.choice(available_living_spaces)
                rooms[allocated_living_space]["occupants"].append(identifier)

        message = "{} has been added and has automatically" \
            "been allocated to {} office and {}" \
            "living space respectively.\n".format(
                Amity.people_data[identifier]["name"],
                allocated_offices,
                allocated_living_space)
        return message

    def reallocate_person(self, args):
        """Reallocated person a new room"""
        person_name = args["<person_name>"].upper()
        new_room = args["<new_room>"].upper()
        person_identifier = None

        for person_id in Amity.people_data:
            if person_name in Amity.people_data[person_id]["name"]:
                person_identifier = person_id

        new_room_type = rooms[new_room]["is_office"]
        # Find current allocated room and remove identifier
        for current_room in rooms:
            current_room_type = rooms[current_room]["is_office"]
            if new_room_type and current_room_type:
                if person_identifier in rooms[current_room]["occupants"]:
                    rooms[current_room]["occupants"].remove(person_identifier)

        # Append identifier to new_room
        if new_room_type and len(rooms[new_room]["occupants"]) < 6:
            rooms[new_room]["occupants"].append(person_identifier)
            message = "{} has been reallocated {} room\n".format(
                person_name, new_room)
            return message

        if not new_room_type and len(rooms[new_room]["occupants"]) < 4:
            if Amity.people_data[person_identifier]["is_fellow"]:
                rooms[new_room]["occupants"].append(person_identifier)
                message = "{} has been reallocated {} room\n".format(
                    person_name, new_room)
                return message
            return "STAFF CANNOT BE ALLOCATED LIVING SPACE"

        return "{} is full".format(new_room)

    def remove_person(self, args):
        """Delete's a person from a room"""
        for person_id, person_info in Amity.people_data.items():
            if args["<person_name>"].upper() in person_info["name"]:
                # Remove's the item at the given position in the list and
                # returns it.
                for current_room in rooms:
                    if person_id in rooms[current_room]["occupants"]:
                        rooms[current_room]["occupants"].remove(person_id)
                        # Returns a copy of the string in which all case-based
                        # characters have been uppercased
                Amity.people_data.pop(person_id)
                return "{} has been deleted".format(
                    args["<person_name>"].upper())

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

                    if "Y" in person:
                        wants_accommodation = "Y"

                    arg_dict = ({
                        "<first_name>": person[0],
                        "<last_name>": person[1],
                        "Staff": is_staff,
                        "Fellow": is_fellow,
                        "<wants_accommodation>": wants_accommodation
                    })
                    message += self.add_person(arg_dict)
        return message

    def get_names(self, identifier):
        """Get's the occupants of of the person from people data."""

        person = Amity.people_data.get(identifier, None)
        if person is None:
            return "Person Does Not Exist."
        return person["name"]

    def print_room(self, args):
        """Prints the occupants of the room"""
        room_name = args["<room_name>"].upper()

        room = rooms.get(room_name, None)
        if room is None:
            message = "{} Room Does Not Exist".format(room_name)
            return message
        message = "{} \n".format(room_name.upper())
        message += "-" * 50
        message += "\n"

        if not room["occupants"]:
            message += "No Occupants"
            return message
        occupants = list(map(self.get_names, room["occupants"]))
        message += "\n".join(occupants)

        return message

    def print_allocations(self, args):
        """Print rooms and number of occupants"""

        data = ""
        for room in rooms:
            room_info = rooms.get(room, None)
            room_type = "Living Space"

            if room_info["is_office"]:
                room_type = "Office"
            data += "\n\n{} ({}) \n".format(room.upper(), room_type)
            data += "-" * 50
            data += "\n"

            if len(rooms[room]["occupants"]) is 0:
                data += "No Occupants"
            occupants = map(self.get_names, rooms[room]["occupants"])
            data += "\n".join(occupants)

        if args["-o"]:
            with open(args["<filename>"], "wt") as output_file:
                output_file.write(data)
                print ("Allocations has been saved to {}".format(
                    args["<filename>"]))
        return data

    def print_unallocated(self, args):
        """Check if person has been allocated a office if not prints out name, checks if person who wants accommodation
         has been allocated has been allocated living space if not prints out name"""
        data = ""

        office_allocations = []
        living_space_allocations = []
        people_without_living_spaces = []

        for room_name, room_info in rooms.items():
            if room_info["is_office"]:
                office_allocations += room_info["occupants"]
            if not room_info["is_office"]:
                living_space_allocations += room_info["occupants"]

        unallocated_offices = list(
            set(Amity.people_data.keys()) - set(office_allocations))
        people_without_offices = list(map(self.get_names, unallocated_offices))

        data += "Those unallocated Offices: \n"
        if len(people_without_offices):
            data += "\n".join(people_without_offices)
        else:
            data += "-" * 50
            data += "\n"
            data += "NONE"

        data += "\n\nThose unallocated living spaces:\n"

        for person_id, person_info in Amity.people_data.items():
            if person_info["is_fellow"] and person_info["accommodation"] == "Y":
                if person_id not in living_space_allocations:
                    people_without_living_spaces.append(person_info["name"])

        if len(people_without_living_spaces):
            data += "\n".join(people_without_living_spaces)
        else:
            data += "-" * 50
            data += "\n"
            data += "NONE"

        if args["-o"]:
            with open(args["<filename>"], "wt") as output_file:
                output_file.write(data)
                print ("Unallocated people have been saved to {}".format(
                    args["<filename>"]))
        return data
