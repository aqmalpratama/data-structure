class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()

    def clear(self):
        return self.items.clear()
    
    def size(self):
        return len(self.items)
    
def reverseStringStack(string):
  length = len(string)
  stack = createStack()