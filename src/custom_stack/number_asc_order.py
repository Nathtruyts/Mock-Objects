from .custom_stack import CustomStack, StackEmptyException

class NumberAscOrder:
    @staticmethod
    def sort(stack):
        if stack.isEmpty():
            return []
        numbers = []
        while not stack.isEmpty():
            numbers.append(stack.pop())
        numbers.sort()
        return numbers