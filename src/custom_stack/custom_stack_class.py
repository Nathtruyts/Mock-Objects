class StackEmptyException(Exception):
     def __init__(self, message="empty stack"):
        self.message = message
        super().__init__(self.message)

class StackFullException(Exception):
    def __init__(self, message="full stack"):
        self.message = message
        super().__init__(self.message)


class CustomStack:

    def __init__(pLimit):
        self.limit = pLimit
        self.elements = []
    
    def size():
        return len(self.elements)

    def isEmpty():
        return self.size() == 0

    def push(element):
        if (self.size == self.limit):
            raise StackFullException
        
        self.elements.append(element)
    
    def pop():
        if self.isEmpty():
            raise StackEmptyException
        return self.elements.pop()
    
    def top():
        if self.isEmpty():
            raise StackEmptyException
        return self.elements[-1]