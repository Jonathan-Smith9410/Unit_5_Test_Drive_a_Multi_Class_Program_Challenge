from lib.todo import *
import pytest

"""
Upon instantiation
Add task to self_task
"""

def test_add_task():
    todo = Todo("Test task")
    actual = todo._task
    expected = "Test task"
    assert actual == expected


"""
Upon instantiation
Set complete to false
"""
def test_complete_is_false():
    todo = Todo("Test task")
    actual = todo._complete
    expected = False
    assert actual == expected

"""
Upon instantiation
Raise error if task = ""
"""
def test_error_on_empty_task():
    with pytest.raises(Exception) as e:
        todo = Todo("")
    error_message = str(e.value)
    assert error_message == "No task present to add."

"""
Upon invoking mark_complete
Set complete to True
"""

def test_complete_is_true():
    todo = Todo("Test task")
    todo.mark_complete()
    actual = todo._complete
    expected = True
    assert actual == expected