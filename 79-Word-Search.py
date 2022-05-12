"""
https://leetcode.com/problems/word-search/

79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
 

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

Method: Backtracking.
As the general idea for the solution, we would walk around the 2D board. 
At each step we compare the board character with the first remaining character of the word. 
If matched, we continued on the path. 
If not, we give up the path. 
And at each step, we would mark or revert our visit so that we won’t have duplicated visits. 
Finally, if no more character left for the word, we find our solution.


Time complexity: 
O(N * (4**L)), where N is the number of cells in the board and L is the length of the word to be matched. 
For the backtracking function, its execution trace would be visualized as a 4-ary tree, each of the branches represent a potential exploration in the corresponding direction. 
Therefore, in the worst case, the total number of invocation would be the number of nodes in a full 4-nary tree, which is about 4**L. We iterate through the board for backtracking, i.e. there could be N times invocation for the backtracking function in the worst case. 
As a result, overall the time complexity of the algorithm would be O(N * (4**L)).

Space complexity: 
O(L), where L is the length of the word to be matched.

"""


        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if self.helper(board, i, j, word):
                    return True
        
        return False
                    
                    
    def helper(self, board, i, j, word):
        if len(word) == 0:
            return True
        
        if i < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or j < 0:
            return False

        if board[i][j] != word[0]:
            return False
         
        word = word[1:]
        char = board[i][j]
        board[i][j] = '#'

        result = self.helper(board, i + 1, j, word) or self.helper(board, i - 1, j, word) or self.helper(board, i, j + 1, word) or self.helper(board, i, j - 1, word)
        
        board[i][j] = char
                
        return result
