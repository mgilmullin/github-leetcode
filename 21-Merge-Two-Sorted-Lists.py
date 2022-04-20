"""
https://leetcode.com/problems/merge-two-sorted-lists/

21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

Methodology
We need to creat a head node that allow us to return the head of the merged list. We need two pointers for each linked list. We will compare the value of each pointer and put the smaller value node into the merged linked list and update the pointer to next. We iterate both linked list at same time until one reach to end. Return the head. (We can also use heap to solve this question or even more complecated question for example merge k sorted linked lists where k is greater than 2)

Time complexity : O(n + m)
Because exactly one of list1 and list2 is incremented on each loop iteration, the while loop runs for a number of iterations equal to the sum of the lengths of the two lists (n + m). All other work is constant, so the overall complexity is linear.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = newList = ListNode(0)
        
        while list1 and list2:
            if list1.val < list2.val:
                newList.next = list1
                list1 = list1.next 

            else:
                newList.next = list2
                list2 = list2.next

            newList = newList.next

        newList.next = list1 or list2

        return head.next
