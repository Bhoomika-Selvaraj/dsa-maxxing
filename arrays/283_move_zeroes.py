from typing import List


def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left, right = 0, 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
        right += 1

    for i in range(left, len(nums)):
        nums[i] = 0


# Time complexity: O(n)
# Space complexity: O(1)

# Note: This can also be solved using a single pass with a swap operation (will be trying again later!)
