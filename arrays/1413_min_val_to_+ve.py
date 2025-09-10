"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.


"""

from typing import List


def minStartValue(nums: List[int]) -> int:
    prefix_sum = [0] * len(nums)
    prefix_sum[0] = nums[0]
    for i in range(1, len(nums)):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]
    minimum = min(prefix_sum)
    return 1 if minimum > 0 else abs(minimum) + 1


print(minStartValue([-3, 2, -3, 4, 2]))

# Time complexity is O(n)
# Space complexity is O(n)
