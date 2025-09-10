from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        current = nums[mid]

        if current == target:
            return mid
        elif current < target:
            low = mid + 1
        else:
            high = mid - 1

    return low


print(searchInsert([1, 3, 5, 6], 5))

# Time complexity: O(log n)
# Space complexity: O(1)
