import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nickname = Column(String(250), nullable=False)
    email =Column (String(250), nullable=False)
    password= Column (String(250), nullable=False)
    favorite_id= Column(Integer, ForeignKey('Favorites.id') ) 

    def serialize(self):
        return {
            "email": self.email,
            "nickname": self.nickname
        }



class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    fav_planet = Column(Integer, ForeignKey('Planets.id'))
    fav_char = Column(Integer, ForeignKey('Characters.id'))
    fav_ship  = Column(Integer, ForeignKey('Starships.id'))

    def serialize(self):
        return {
            "fav_planet": self.fav_planet,
            "fav_char": self.fav_char,
            "fav_ship": self.fav_ship
        }

class Characters(Base):
    __tablename__ = "Characters"
    id = Column(Integer, primary_key=True)
    full_Name = Column(String(250), nullable=False)
    affiliation = Column(String(250), ForeignKey('Faction.name'))
    date_of_birth = Column(String(250), nullable=False)
    
    def serialize(self):
        return {
            "full_Name": self.full_Name,
            "affiliation": self.affiliation
        }

class Planets(Base):
    __tablename__ = "Planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    affiliation = Column(String(250), ForeignKey('Faction.name'))
    population = Column(String(250), nullable=False)
    size = Column(String(250), nullable=False)
    
    def serialize(self):
        return {
            "population": self.population,
            "name": self.name
        }

class Starships(Base):
    __tablename__ = "Starships"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    affiliation = Column(String(250), ForeignKey('Faction.name'))
    passangers = Column(String(250), nullable=False)
    size = Column(String(250), nullable=False)
    
    def serialize(self):
        return {
            "affiliation": self.affiliation,
            "name": self.name
        }

class Faction(Base):
    __tablename__ = "Faction"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

   
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')