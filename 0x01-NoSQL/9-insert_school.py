#!/usr/bin/env python3
"""python script that insert doc"""


def insert_school(mango_collection, **kwargs):
    """
      insert doc in a collection
      return new_id
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
