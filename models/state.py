#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """Returns: cities in a state
            """
            import models
            return [city for city in models.storage.all(
                City).values() if city.state_id == self.id]

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ geeter method for cities of a given state
            """
            cilty_list = []
            gen_cities = models.storage.all(City)
            for city in gen_cities.values():
                if city.state.id == self.id:
                    city_list.append(city)
            return city_list
