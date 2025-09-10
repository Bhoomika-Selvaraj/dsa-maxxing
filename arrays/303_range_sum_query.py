from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        total = 0

        for n in nums:
            total += n
            self.prefix_sum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        r = self.prefix_sum[right]
        l = self.prefix_sum[left - 1] if left > 0 else 0

        return r - l


example = NumArray([-2, 0, 3, -5, 2, -1])
print(example.sumRange(0, 2))

# Time complexity: O(1) for sumRange
# Space complexity: O(n)
