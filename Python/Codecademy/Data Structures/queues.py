from node import Node


class Queue(Node):
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def peek(self):
        if self.get_size() == 0:
            print("Nothing to see here!")
        else:
            return self.head.get_value()

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
