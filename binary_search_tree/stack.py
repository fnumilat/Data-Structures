from singly_linked_list import LinkedList


# Using the Link List
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def len(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_tail()