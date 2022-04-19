"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2^12 - 1].
-1000 <= Node.val <= 1000

Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

Hint:
Using the iterative approach, count the number of nodes at current level, append the children of the node to the queue. Also while dequeueing the node from the queue add it to a list (named “rows” in code) so that all nodes at a level are stored in the list “rows”

Time Complexity : O(n)

"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = []
        queue.append(root)
        
        while len(queue) > 0:
            row = []
            cnt = len(queue)
            
            while cnt>0:
                cnt -= 1
                node = queue.pop(0)
                row.append(node)
                
                if node is None:
                    continue
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            for i in range(len(row) - 1):
                row[i].next = row[i + 1]
            
        return root
