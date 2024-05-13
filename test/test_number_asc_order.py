import pytest
from custom_stack.custom_stack import CustomStack
from custom_stack.number_asc_order import NumberAscOrder

def test_sort_numbers():
    stack = CustomStack(6)
    nums = [31, 10, 45, 20, 11, 18]
    for num in nums:
        stack.push(num)
    sorted_nums = NumberAscOrder.sort(stack)
    assert sorted_nums == sorted(nums)

def test_sort_empty_stack():
    stack = CustomStack(6)
    sorted_nums = NumberAscOrder.sort(stack)
    assert sorted_nums == []
