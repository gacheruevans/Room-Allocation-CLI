class Person(object):
    def __init__(self):
        self.entries = {}

    def add(self, name, room):
        self.entries[name] = room

    def lookup(self, state):
        return self.entries[state]

    def is_staff(self):
        return True