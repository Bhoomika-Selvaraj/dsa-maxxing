from typing import List


def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        current = nums[mid]
        if current == target:
            return mid
        elif current < target:
            low = mid + 1
        elif current > target:
            high = mid - 1
        else:
            pass

    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))

# Time complexity: O(log n)
# Space complexity: O(1)
