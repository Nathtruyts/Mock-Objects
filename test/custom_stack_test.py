import pytest
from custom_stack import CustomStack, StackEmptyException, StackFullException

def test_push():
    stack = CustomStack(3)
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
    assert stack.top() == 2

def test_pop():
    stack = CustomStack(3)
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.size() == 1

def test_empty_pop():
    stack = CustomStack(3)
    with pytest.raises(StackEmptyException):
        stack.pop()

def test_full_push():
    stack = CustomStack(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    with pytest.raises(StackFullException):
        stack.push(4)

def test_is_empty():
    stack = CustomStack(3)
    assert stack.isEmpty()
    stack.push(1)
    assert not stack.isEmpty()

def test_top_empty_stack():
    stack = CustomStack(3)
    with pytest.raises(StackEmptyException):
        stack.top()

def test_size():
    stack = CustomStack(3)
    assert stack.size() == 0
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
