#!/usr/bin/env python3
"""
average score retuens with key = averageScore
"""


def top_students(mongo_collection):
    """
    The top must be ordered
    Returns all students sorted by average score
    """
    return mongo_collection.aggregate([
        {
            "$project":
            {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort":
            {
                "averageScore": -1
            }
        }
    ])
