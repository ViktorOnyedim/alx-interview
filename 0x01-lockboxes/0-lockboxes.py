#!/usr/bin/python3
"""Lockboxes Module"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    n = len(boxes)

    # Start with the first box that is unlocked
    unlocked = set([0])
    # Keys from the first box
    keys = set(boxes[0])

    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])

    return len(unlocked) == n
