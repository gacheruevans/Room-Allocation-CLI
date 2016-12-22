from app.rooms.roomClass import Room

class Office(Room):
    """This is the Office class that inherits from thr Room class"""
    def __init__(self):
        self.room_type = "Office"
        self.room_capacity = 6