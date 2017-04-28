from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Rooms(Base):
    """
    This is the Rooms Table class that inherits from Base.
    It specifies the tablename and columns of the database table.
    tablename: 'rooms'
    columns:
        id: Integer column that is unique and the primary key.
        room_name: String column thats holds the name of a room.
        is_office: Boolean column that indicates the room type.
                    If false then the room is a living space
        }
    """
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    room_name = Column(String)
    is_office = Column(Boolean)


class People(Base):
    """
    This is the People Table class that inherits from Base.
    It specifies the tablename and columns of the database table.
    tablename: 'people'
    columns:
        person_id: Integer column that is unique and the primary key.
        name: String column thats holds the name of a person.
        wants_accomodation: String column thats holds the person's
                accomodation request.It can be either 'Y' or 'N'
        is_office: Boolean column that indicates the room type.
                    If false then the room is a living space
        }
    """
    __tablename__ = 'people'
    person_id = Column(Integer, primary_key=True)
    name = Column(String)
    wants_accommodation = Column(String)
    is_fellow = Column(Boolean)


class Allocations(Base):
    """
    This is the Allocations Table class that inherits from Base.
    It specifies the tablename and columns of the database table.
    tablename: 'allocations'
    columns:
        id: Integer column that is unique and the primary key.
        room_name: String column thats holds the name of a room
                    an occupant is in.
        occupant_id: Integer column that holds the id of the
                    person occupying the room.
        }
    """
    __tablename__ = 'allocations'
    id = Column(Integer, primary_key=True)
    room_name = Column(String)
    occupant_id = Column(Integer)
