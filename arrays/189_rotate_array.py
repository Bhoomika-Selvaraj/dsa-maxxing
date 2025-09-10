from typing import List


def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k]
    print(nums)


rotate([1, 2, 3, 4, 5, 6, 7], 3)

# Time complexity: O(n)
# Space complexity: O(1)
