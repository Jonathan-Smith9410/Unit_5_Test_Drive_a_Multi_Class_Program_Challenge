# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self._todo_list = []

    def add(self, todo):
        self._todo_inst = todo
        self._todo_list.append(self._todo_inst)

    def incomplete(self):
        return [self._todo_inst._task for self._todo_inst in self._todo_list if self._todo_inst._complete == False]

    def complete(self):
        return [self._todo_inst._task for self._todo_inst in self._todo_list if self._todo_inst._complete == True]

    def give_up(self):
        for self._todo_inst in self._todo_list:
            self._todo_inst._complete = True