#!/usr/bin/python3
"""Minimum number of operations algorithm challenge"""



def minOperations(n):
    """return minimum number of Copy-Paste Operations to reach target"""
    if n <= 1:
        return 0

    operations = 0
    current_no = 1
    clipboard = 0

    while current_no < n:
        if n - current_no >= current_no:
            # Copy all and Paste
            clipboard = current_no
            current_no += clipboard
            operations += 2
        else:
            # Only Paste
            current_no += clipboard
            operations += 1

    return operations
