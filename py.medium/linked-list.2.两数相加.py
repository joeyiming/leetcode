#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ListNode(0)
        head = cur
        remainder = 0
        while l1 or l2:
            if l1 is None:
                l1 = ListNode(0)
            elif l2 is None:
                l2 = ListNode(0)

            if remainder > 0:
                remainder, cur.val = divmod(l1.val+l2.val+1, 10)
            else:
                remainder, cur.val = divmod(l1.val+l2.val, 10)

            l1 = l1.next
            l2 = l2.next
            if l1 or l2 or remainder > 0:
                cur.next = ListNode(remainder)
                cur = cur.next
            else:
                break

        return head

# @lc code=end
