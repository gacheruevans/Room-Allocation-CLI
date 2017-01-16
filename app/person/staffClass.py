from app.person.personClass import Person

class Staff(Person):
    """Fellow class inherits from Person class, it declares person role as fellow """
    def __init__(self):
        person_role = "Staff"