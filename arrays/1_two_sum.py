from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    enumerated_nums = list(enumerate(nums))
    nums = enumerated_nums.sort(key=lambda x: x[1])

    left, right = 0, len(enumerated_nums) - 1
    while left < right:
        current_sum = enumerated_nums[left][1] + enumerated_nums[right][1]
        if current_sum == target:
            return [enumerated_nums[left][0], enumerated_nums[right][0]]
        elif current_sum > target:
            right -= 1
        else:
            left += 1


print(twoSum([3, 2, 4], 6))

# Time complexity: O(n log n) due to sorting
# Space complexity: O(n) due to creating the enumerated list

# Note: This can also be solved in O(n) time using a hash map to store the indices of the numbers.
