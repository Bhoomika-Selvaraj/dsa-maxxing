from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 1:
        return 1

    left, right = 0, 1
    while right < len(nums):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
        right += 1
    return left + 1


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

# Time complexity: O(n)
# Space complexity: O(1)
