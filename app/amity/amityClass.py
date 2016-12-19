rooms= {}

class Amity(object):
    """ class contains methods for getting room type, creating room type and listing rooms to be added. """
    def get_room_type(self, room_type = None):
        """ Gets room type from user after the create room command"""
        room_type = room_type

        #Assign a group of rooms to a room type
        while room_type not in ["O","L"]:
            room_type = input("Enter room type: \n o: Office Space \n l: Living Space: \n")
            room_type = room_type.upper()
        return room_type

    def create_room(self, args, room_type = None):
        """Allows a user to input a list of room names specifying whether they are office or living space"""
        room_type = room_type

        room_type = self.get_room_type(room_type)
        is_office = False

        if room_type == "O":
            is_office = True

        #Adds rooms to the rooms dict
        for room in args["<room_name>"]:
            if room.upper() in rooms:
                message = "{} Exists \n".format(room.upper())
                return  message

            rooms.update({room.upper():{"occupants": [], "is_office": is_office}})
            message = "You have the following rooms\n"
            message += "\n".join(rooms.keys)

            return message