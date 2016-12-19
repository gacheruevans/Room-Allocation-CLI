from app.person.personClass import people_data
from app.amity.amityClass import rooms

class Room(object):
    """Holds all the functions that display rooms data."""

    def get_names(self, identifier):
        """get's the name of of the person from people data."""

        person = people_data.get(identifier, None)
        if person == None:
            return "Person Does Not Exist."
        return person["name"]

    def print_room(self, args):
        """Prints the occupants of the room"""
        room_name = args["<room_name>"].upper()

        room = rooms.get(room_name, None)
        if room == None:
            message=  "{} Room Does Not Exist".format(room_name)
            return message
        message = "{} \n".format(room_name.upper())
        message += "-" * 40
        message +="\n"

        if not room["occupants"]:
            message += "No Occupants"
            return  message
        occupants = list(map(self.get_name, room["occupants"]))
        message += "\n".join(occupants)

        return message

    