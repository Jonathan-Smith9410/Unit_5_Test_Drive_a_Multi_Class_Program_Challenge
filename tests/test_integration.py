from lib.todo import *
from lib.todo_list import *

"""
Upon addition of a single Todo task
Check that task is added to the list
"""

def test_that_single_todo_task_is_added_to_todo_list_as_incomplete():
    todo_list = TodoList()
    todo_task1 = Todo("Task 1")
    todo_list.add(todo_task1)
    actual = todo_list.incomplete()
    expected = ["Task 1"]
    assert actual == expected



"""
Upon addition of two Todo tasks
Check that both tasks are added to the list
"""

def test_that_two_todo_tasks_are_added_to_todo_list_as_incomplete():
    todo_list = TodoList()
    todo_task1 = Todo("Task 1")
    todo_list.add(todo_task1)
    todo_task2 = Todo("Task 2")
    todo_list.add(todo_task2)
    actual = todo_list.incomplete()
    expected = ["Task 1", "Task 2"]
    assert actual == expected

"""
Upon addition of a single Todo task
Check that task is added to the complete list
when marked as complete
"""

def test_that_single_todo_task_is_added_to_todo_list_as_complete():
    todo_list = TodoList()
    todo_task1 = Todo("Task 1")
    todo_list.add(todo_task1)
    todo_task1.mark_complete()
    actual = todo_list.complete()
    expected = ["Task 1"]
    assert actual == expected

"""
Upon addition of two Todo tasks
Check that tasks are added to the complete list
when marked as complete
"""

def test_that_two_todo_tasks_are_added_to_todo_list_as_complete():
    todo_list = TodoList()
    todo_task1 = Todo("Task 1")
    todo_list.add(todo_task1)
    todo_task1.mark_complete()
    todo_task2 = Todo("Task 2")
    todo_list.add(todo_task2)
    todo_task2.mark_complete()
    actual = todo_list.complete()
    expected = ["Task 1", "Task 2"]
    assert actual == expected

"""
Upon addition of two Todo tasks
Check that tasks are not present on the incomplete list
when marked as complete
"""

def test_that_two_todo_tasks_are_not_on_incomplete_list_when_completed():
    todo_list = TodoList()
    todo_task1 = Todo("Task 1")
    todo_list.add(todo_task1)
    todo_task1.mark_complete()
    todo_task2 = Todo("Task 2")
    todo_list.add(todo_task2)
    todo_task2.mark_complete()
    actual = todo_list.incomplete()
    expected = []
    assert actual == expected


"""
Upon addition of two Todo tasks
Check that both tasks are added to the complete list
when give_up is invoked
"""

def test_that_two_todo_tasks_are_added_to_todo_list_as_complete():
    todo_list = TodoList()
    todo_task1 = Todo("Task 1")
    todo_list.add(todo_task1)
    todo_task2 = Todo("Task 2")
    todo_list.add(todo_task2)
    todo_list.give_up()
    actual = todo_list.complete()
    expected = ["Task 1", "Task 2"]
    assert actual == expected