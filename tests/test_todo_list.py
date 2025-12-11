from lib.todo_list import *


"""
Upon instantiation
Create empty todo_list
"""

def test_add_task():
    todo = TodoList()
    actual = todo._todo_list
    expected = []
    assert actual == expected