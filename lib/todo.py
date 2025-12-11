class Todo:

    def __init__(self, task):
        if task == "":
            raise Exception("No task present to add.")
        self.task = task
        self.complete = False

    def mark_complete(self):
        self.complete = True

