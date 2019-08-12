#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from os import getenv
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
elif getenv('HBNB_TYPE_STORAGE') == 'file':
    storage = FileStorage()
    storage.reload()
