#!/usr/bin/env python3
"""python script that lists all doc"""


def list_all(mango_collection):
    """
      lists all doc in a collection
      return is empty
    """
    documents = mongo_collection.find()
    return documents
