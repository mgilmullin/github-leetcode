"""
https://leetcode.com/problems/surrounded-regions/

130. Surrounded Regions

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Explanation: 
Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
 

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Example 2:
Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.

Methodology: Depth First Search (DFS)

To find the surrounded regions, we can first find the on boarder regions and mark them (N). After we find all on border regions. Then we iterate the board again, make the surround regions to be ‘X’ and on border regions to be ‘O’

Complexity (BigO):
We iterate each cell, it will cost O(m*n) where m*n is the size of the 2D list. 
Each cell will also iterate four directions:  O(4*m*n). 
Then we iterate twice to render the on border regions and surrounded regions which take O(2*m*n). 
In total O(m*n). 

"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board: return board
        row,col=len(board),len(board[0])
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        visited=set()
        def dfs(x,y):
            for dx, dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<row and 0<=ny<col and board[nx][ny]=='O' and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    board[nx][ny]='N'
                    dfs(nx, ny)
                
        for x in range(row):
            for y in range(col):
                if (x==0 or x==row-1 or y== 0 or y==col-1) and board[x][y] == 'O' and (x,y) not in visited:
                    board[x][y]='N'
                    visited.add((x,y))
                    dfs(x,y)
                    
        for x in range(row):
            for y in range(col):
                if board[x][y]=='O':
                    board[x][y]='X'
                elif board[x][y]=='N':
                    board[x][y]='O'
