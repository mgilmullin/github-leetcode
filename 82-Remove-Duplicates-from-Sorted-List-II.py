"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

82. Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
 

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

If a node’s value repeats in other nodes, we want to delete all of these nodes. 
We have to compare with its previous value and keep a pointer at the previous value in case if we want to delete the current node. This include the head , and  we add a dummy node and point it to the head.

Detailed explanation in the comments.

Complexity Analysis
Time complexity: O(N) 

Space complexity: O(1) because we don't allocate any additional data structure.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # add dummy and initialize all the pointers
        dummy = ListNode(0) 
        dummy.next = head 
        pre = dummy
        cur = head 
        while cur: 
            # if cur is not the last not and it has the same 
            # value as the next node, we update the cur pointer
            while cur.next and cur.val == cur.next.val: 
                cur = cur.next 

            if pre.next == cur:   # 1 #
                # this means cur pointer is not updated in 
                # the while loop, thus cur's value is distinct
                # we move pre pointer to the cur's location
                pre = cur 
            else:  # 2 # 
                # cur's value has repeated itself so
                # we skip the entire sequence of nodes with 
                # this value
                pre.next = cur.next 
            # and in either case we update the cur pointer
            cur = cur.next # 3 #
        return dummy.next
