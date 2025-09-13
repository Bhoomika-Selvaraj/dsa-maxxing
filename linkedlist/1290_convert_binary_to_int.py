from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary_num_list = []
        curr = head
        while curr is not None:
            binary_num_list.append(str(curr.val))
            curr = curr.next
        return int("".join(binary_num_list), 2)


head = ListNode(1, ListNode(0, ListNode(1)))
print(Solution().getDecimalValue(head))

# Time complexity: O(n)
# Space complexity: O(n)
