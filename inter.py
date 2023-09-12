"""
Challenge 1: Reverse a String
Write a Python function reverse_string(s: str) -> str that reverses a given string s. For example, if the
input is "Hello, World!", the function should return "!dlroW ,olleH".
"""


# Ans1
def reverse_string(string: str):
    return string[::-1]


print(reverse_string("Hello, World!"))


"""
Challenge 2: Find the Missing Number
Write a Python function find_missing_number(nums: List[int]) -> int that takes a list of integers nums
containing unique numbers from 1 to n except for one missing number. The function should find and
return the missing number. For example, if nums is [3, 7, 1, 2, 8, 4, 5], the missing number is 6.
"""

def find_missing_number(nums: list[int]):
    mx = max(nums)
    mi = min(nums)
    return mi, mx


print(find_missing_number([3, 7, 1, 2, 8, 4, 5]))


# Trie: