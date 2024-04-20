#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class DBStorage:
    """
    New Database storage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiates the Storage Ckase
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            os.getenv("HBNB_MYSQL_USER"), os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"), os.getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        function to show dictionary of all objects in the database
        """
        all_dict = {}
        if cls is not None:
            all_dict = {mdl.__class__.__name__ + "." + mdl.id:
                        mdl for mdl in self.__session.query(
                            classes[cls]).all()}
        else:
            for x in Base.__subclasses__():
                all_t = self.__session.query(x).all()
                for mdl in all_t:
                    all_dict[mdl.__class__.__name__ + "." + mdl.id] = mdl
        return all_dict

    def new(self, obj):
        """
        function to adds new object to session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        function to Save new object to the database
        """
        if self.__session:
            self.__session.commit()

    def delete(self, obj=None):
        """
        function to Delete object in current session
        """
        self.__session.delete(obj)

    def reload(self):
        """
        function to create new session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
