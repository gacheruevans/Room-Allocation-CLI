class Room:
    def __init__(self):
        self.entries = {}

    def add(self, room_type, name):
        self.entries[room_type] = name

    def lookup(self, name):
        return self.entries[name]
