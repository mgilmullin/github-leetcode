"""
https://leetcode.com/problems/subtree-of-another-tree/

572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 
Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

Method: Depth First Search
The following conditions must be established at the same time. ：

- the values of the current two root nodes are the same. 
- the left subtree of root is the same as the left subtree of subRoot.
- the right subtree of the  root is the same as the right subtree of subRoot.

- Enumerate root to determine whether the subtree of this point is the same as that of the subRoot equal. 
- Use depth-first search check ， starting from the root.
- Synchronize mobile traverses two trees.
- Determine whether the corresponding positions are equal.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return self.dfs(root, subRoot)
    
    def dfs(self, c, t):
        # c  returns when the subtree is empty  False
        if not c:
            return False
        return self.isSame(c, t) or self.dfs(c.left, t) or self.dfs(c.right, t)
    
    def isSame(self, c, t):
        #  when both trees are empty, they are also considered to be the same. 
        if (not c) and (not t):
            return True
        #  when one of the trees is empty, but the other tree is not empty ， at this time, it is different. 
        if (not c and t) or (c and not t):
            return False
        #  neither tree is empty, if the values are different ， it's also different. 
        if (c.val != t.val):
            return False
        #  if none of the above conforms to the above, continue to check down. 
        return self.isSame(c.left, t.left) and self.isSame(c.right, t.right)
