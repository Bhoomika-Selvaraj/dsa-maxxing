from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    nums_set = set(nums)
    if len(nums_set) == len(nums):
        return False
    return True


print(containsDuplicate([1, 2, 3, 1]))

# Time complexity: O(n)
# Space complexity: O(n)
