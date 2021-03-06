"""
https://leetcode.com/problems/all-paths-from-source-to-target/

797. All Paths From Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
 

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

Constraints:
n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.

Method: Depth First Search: (DFS)
Build an adjacency list representing the relationship between nodes and edges. 
Conduct a DFS to find all the paths from source to target.

Time Complexity: O(V + E). V is the number of vertices, E is the number of edges.
Space Complexity: O(V + E). V is the number of vertices, E is the number of edges.

"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        
        results = []
        
        adjList = []

        for i in graph:
            adjList.append([])
            
        for i in range(len(graph)):
            edges = graph[i]
            
            for edge in edges:
                adjList[i].append(edge)
            
        
        self.helper(results, adjList, 0, len(adjList) - 1, [0])
        
        return results
    
    def helper(self, results, adjList, current, target, path):
        if current == target:
            results.append(list(path))
            return
        
        for node in adjList[current]:
            path.append(node)
            self.helper(results, adjList, node, target, path)
            path.pop()
