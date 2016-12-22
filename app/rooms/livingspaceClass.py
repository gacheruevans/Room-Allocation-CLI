from app.rooms.roomClass import Room

class LivingSpace(Room):
    """This is the living space class that inherits from thr Room class"""
    def __init__(self):
        self.room_type = "Living Space"
        self.room_capacity= 4