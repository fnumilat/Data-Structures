
from singly_linked_list import LinkedList


# Using the Link List
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def len(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()


