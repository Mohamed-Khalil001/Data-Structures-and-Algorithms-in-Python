# Depth First Search (DFS) Lecture 10
# Implements DFS for binary trees and graphs in financial analysis.
# Time Complexity: Analyzed per function.
# Example: Traversing stock price trees or transaction networks.

# --------------------------------------------
# Concept: Depth First Search (DFS)
# Definition: A traversal algorithm that explores as far as possible along each branch before backtracking.
# Properties:
# - Binary Trees:
#   - In-order: Left, Node, Right (ascending order in BST).
#   - Pre-order: Node, Left, Right (copy tree, prefix expressions).
#   - Post-order: Left, Right, Node (delete tree, postfix expressions).
#   - Time Complexity: O(n), where n is number of nodes.
# - Graphs:
#   - Tracks visited vertices to avoid cycles.
#   - Uses recursion or stack for backtracking.
#   - Time Complexity: O(V + E), where V is vertices, E is edges.
# Use Case: Traverse stock price BSTs or analyze transaction networks in quantitative finance.
# --------------------------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data  # Stock price or value
        self.left = None  # Left child
        self.right = None  # Right child


class FinancialDFS:
    def in_order(self, node):
        """
        In-order traversal: Left, Node, Right.
        Time Complexity: O(n)
        """
        if node:  # If node exists
            self.in_order(node.left)  # Visit left subtree
            print(node.data, end=" ")  # Visit node
            self.in_order(node.right)  # Visit right subtree

    def pre_order(self, node):
        """
        Pre-order traversal: Node, Left, Right.
        Time Complexity: O(n)
        """
        if node:  # If node exists
            print(node.data, end=" ")  # Visit node
            self.pre_order(node.left)  # Visit left subtree
            self.pre_order(node.right)  # Visit right subtree

    def post_order(self, node):
        """
        Post-order traversal: Left, Right, Node.
        Time Complexity: O(n)
        """
        if node:  # If node exists
            self.post_order(node.left)  # Visit left subtree
            self.post_order(node.right)  # Visit right subtree
            print(node.data, end=" ")  # Visit node

    def dfs_graph(self, graph, vertex, visited=None):
        """
        DFS for graphs, tracking visited vertices.
        Time Complexity: O(V + E)
        """
        if visited is None:  # Initialize visited set
            visited = set()
        visited.add(vertex)  # Mark vertex as visited
        print(vertex, end=" ")  # Visit vertex
        for neighbor in graph[vertex]:  # Check all neighbors
            if neighbor not in visited:  # If not visited
                self.dfs_graph(graph, neighbor, visited)  # Recurse


# Testing
dfs = FinancialDFS()

# Binary Tree (BST) for stock prices
root = TreeNode(60)  # Root
root.left = TreeNode(50)  # Left child
root.right = TreeNode(70)  # Right child
root.left.left = TreeNode(40)  # Left child of 50
root.left.right = TreeNode(55)  # Right child of 50

print("In-order traversal:", end=" ")
dfs.in_order(root)  # Output: 40 50 55 60 70
print()  # New line
# How it works: Visits left (40, 50, 55), node (60), right (70)

print("Pre-order traversal:", end=" ")
dfs.pre_order(root)  # Output: 60 50 40 55 70
print()
# How it works: Visits node (60), left (50, 40, 55), right (70)

print("Post-order traversal:", end=" ")
dfs.post_order(root)  # Output: 40 55 50 70 60
print()
# How it works: Visits left (40, 55, 50), right (70), node (60)

# Graph for transaction network
graph = {
    0: [1, 2, 4],  # Company 0 connected to 1, 2, 4
    1: [0, 2],     # Company 1 connected to 0, 2
    2: [0, 1, 4],  # Company 2 connected to 0, 1, 4
    3: [4],        # Company 3 connected to 4
    4: [0, 2, 3]   # Company 4 connected to 0, 2, 3
}

print("DFS Graph from vertex 0:", end=" ")
dfs.dfs_graph(graph, 0)  # Output: 0 1 2 4 3
print()
# How it works: Visits 0, then 1, 2, 4, 3, avoiding cycles
















"""
        40
       /  \
     20    60
    / \    / \
  10  30  50 70

🧠 in_order Traversal Visualization :

🟩 in_order(40)
├── 🟨 in_order(20)
│   ├── 🟦 in_order(10) 
│   │   ├── ❌ in_order(None) ← يرجع
│   │   ├── ✅ print(10) 
│   │   └── ❌ in_order(None) ← يرجع
│   ├── ✅ print(20)
│   └── 🟦 in_order(30)
│       ├── ❌ in_order(None) ← يرجع
│       ├── ✅ print(30)
│       └── ❌ in_order(None) ← يرجع
├── ✅ print(40)
└── 🟨 in_order(60)
    ├── 🟦 in_order(50)
    │   ├── ❌ in_order(None) ← يرجع
    │   ├── ✅ print(50)
    │   └── ❌ in_order(None) ← يرجع
    ├── ✅ print(60)
    └── 🟦 in_order(70)
        ├── ❌ in_order(None) ← يرجع
        ├── ✅ print(70)
        └── ❌ in_order(None) ← يرجع

        10 20 30 40 50 60 70 (in order for order arranged )
        """

"""
     60
    /  \
  50    70

🌲 pre_order Traversal Visualization :

🟩 pre_order(60)
├── ✅ print(60)
├── 🟨 pre_order(50)
│   ├── ✅ print(50)
│   ├── ❌ pre_order(None) ← يرجع
│   └── ❌ pre_order(None) ← يرجع
└── 🟨 pre_order(70)
    ├── ✅ print(70)
    ├── ❌ pre_order(None) ← يرجع
    └── ❌ pre_order(None) ← يرجع

60 50 70 (pre order for copy tree  )

"""
"""
     60
    /  \
  50    70

🌲 post_order Traversal Visualization :

🟩 post_order(60)
├── 🟨 post_order(50)
│   ├── ❌ post_order(None) ← يرجع
│   ├── ❌ post_order(None) ← يرجع
│   └── ✅ print(50)
├── 🟨 post_order(70)
│   ├── ❌ post_order(None) ← يرجع
│   ├── ❌ post_order(None) ← يرجع
│   └── ✅ print(70)
└── ✅ print(60)

50 70 60 (post order _node print in the end )
 """


"""  
graph Visualization :
     0
   / | \
  1  2  4
     |   \
     1     3

🟩 dfs(0)
├── ✅ print(0)
├── 🟨 dfs(1)
│   ├── ✅ print(1)
│   └── 🟦 dfs(2)
│       ├── ✅ print(2)
│       └── 🟦 dfs(4)
│           ├── ✅ print(4)
│           └── 🟦 dfs(3)
│               └── ✅ print(3)

0 1 2 4 3

"""
