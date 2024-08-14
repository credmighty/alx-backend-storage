#!/usr/bin/env python3
"""
topics (list of strings) will be the list of topics approached in the school
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
