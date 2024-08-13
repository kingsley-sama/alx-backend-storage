#!/usr/bin/env python3
import pymongo
from pymongo import MongoClient
"""inserts a file into a databases"""


cluster = MongoClient("mongodb://localhost:27017")
db = cluster["my_db"]
collection = db["school"]
post = {"name": "Holberton school"}
collection.insert_one(post)
