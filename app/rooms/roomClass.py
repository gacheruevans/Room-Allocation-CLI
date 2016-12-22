from app.person.personClass import Person
from app.amity.amityClass import rooms


class Room(object):
    """Holds all the functions that display rooms data."""

    def get_names(self, identifier):
        """Get's the name of of the person from people data."""

        person = Person.people_data.get(identifier, None)
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
        message += "-" * 40
        message += "\n"

        if not room["occupants"]:
            message += "No Occupants"
            return message
        occupants = list(map(self.get_names, room["occupants"]))
        message += "\n".join(occupants)

        return message

    def print_allocations(self, args):
        """Print rooms and occupants"""

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

        unllocated_offices = list(
            set(Person.people_data.keys()) - set(office_allocations))
        people_without_offices = list(map(self.get_names, unllocated_offices))

        data += "Those unallocated Offices: \n"
        if len(people_without_offices):
            data += "\n".join(people_without_offices)
        else:
            data += "NONE"

        data += "\n\nThose unallocated living spaces:\n"

        for person_id, person_info in Person.people_data.items():
            if person_info["is_fellow"] and person_info["accommodation"] == "Y":
                if person_id not in living_space_allocations:
                    people_without_living_spaces.append(person_info["name"])

        if len(people_without_living_spaces):
            data += "\n".join(people_without_living_spaces)
        else:
            data += "NONE"

        if args["-o"]:
            with open(args["<filename>"], "wt") as output_file:
                output_file.write(data)
                print ("Unallocated people have been saved to {}".format(
                    args["<filename>"]))
        return data
