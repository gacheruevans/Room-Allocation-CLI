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

    def allocate_person_room(self):
        """Allocates a person their respective office and living room based on whether they are a staff or fellow"""

        pass
