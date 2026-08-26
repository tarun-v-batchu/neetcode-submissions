"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def dfs(node, visited_nodes) :
            print(node.val)
            
            if node.val in visited_nodes :
                return visited_nodes, visited_nodes[node.val]
            
            curr_node = Node(node.val)
            visited_nodes[node.val] = curr_node

            for new_node in node.neighbors :
                visited_nodes, neighbor_node = dfs(new_node, visited_nodes)
                curr_node.neighbors += [neighbor_node]
            
            return visited_nodes, curr_node

        visited_nodes = {}
        if node == None :
            return None
        visited_nodes, node = dfs(node, visited_nodes)
        return node


