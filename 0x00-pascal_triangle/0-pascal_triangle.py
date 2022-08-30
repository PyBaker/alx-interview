#!/usr/bin/python3
"""
Pascal triangle module
"""


def pascal_triangle(n):
    """ Function to return Pascal's Triangle """
    if n <= 0:
        return []
    pascal_list = [[1]]
    for i in range(n):
        if i == n:
            continue
        while len(pascal_list) != n:
            previous_row = pascal_list[-1]
            current_row = [1]
            for i in range(len(previous_row) - 1):
                current_row.append(previous_row[i] + previous_row[i + 1])
            current_row.append(1)
            pascal_list.append(current_row)
    return pascal_list
