#!/usr/bin/env python3
"""
topic (String) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return list of schools having a specific topic
    """
    return mongo_collection.find({"topics": topic})
