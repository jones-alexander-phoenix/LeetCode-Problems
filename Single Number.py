"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

def singleNumber(nums):
    for i in nums:
        if nums.count(i) == 1:
            return i

