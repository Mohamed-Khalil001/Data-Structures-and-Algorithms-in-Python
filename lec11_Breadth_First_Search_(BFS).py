

# Breadth First Search (BFS) Lecture 11
# Implements BFS for binary trees and graphs in financial analysis.
# Time Complexity: Analyzed per function.
# Example: Traversing stock price trees or transaction networks.

# --------------------------------------------
# Concept: Breadth First Search (BFS)
# Definition: A traversal algorithm that visits all nodes at the current level before moving to the next level.
# Properties:
# - Binary Trees:
#   - Visits nodes level by level (root, then level 1, then level 2, etc.).
#   - Uses a queue to track nodes to visit.
#   - Time Complexity: O(n), where n is number of nodes.
# - Graphs:
#   - Visits vertices level by level, tracking visited vertices to avoid cycles.
#   - Uses a queue to track vertices to visit.
#   - Time Complexity: O(V + E), where V is vertices, E is edges.
# Use Case: Analyze stock price trees level by level or find shortest paths in transaction networks in quantitative finance.
# --------------------------------------------

from queue import SimpleQueue


class TreeNode:
    def __init__(self, data):
        self.data = data  # Stock price or value
        self.left = None  # Left child
        self.right = None  # Right child


class FinancialBFS:
    def bfs_tree(self, root):
        """
        BFS for binary trees, visiting nodes level by level.
        Time Complexity: O(n)
        """
        if not root:  # If no root
            return []
        visited_nodes = []  # Track visited nodes
        queue = SimpleQueue()  # Queue for nodes to visit
        queue.put(root)  # Add root to queue
        while not queue.empty():  # Until queue is empty
            current_node = queue.get()  # Get first node
            visited_nodes.append(current_node.data)  # Visit node
            if current_node.left:  # If left child exists
                queue.put(current_node.left)  # Add to queue
            if current_node.right:  # If right child exists
                queue.put(current_node.right)  # Add to queue
        return visited_nodes  # Return visited nodes

    def bfs_graph(self, graph, initial_vertex):
        """
        BFS for graphs, visiting vertices level by level.
        Time Complexity: O(V + E)
        """
        visited_vertices = []  # Track visited vertices
        queue = SimpleQueue()  # Queue for vertices to visit
        visited_vertices.append(initial_vertex)  # Visit initial vertex
        queue.put(initial_vertex)  # Add to queue
        while not queue.empty():  # Until queue is empty
            current_vertex = queue.get()  # Get first vertex
            for neighbor in graph[current_vertex]:  # Check neighbors
                if neighbor not in visited_vertices:  # If not visited
                    visited_vertices.append(neighbor)  # Visit neighbor
                    queue.put(neighbor)  # Add to queue
        return visited_vertices  # Return visited vertices


# Testing
bfs = FinancialBFS()

# Binary Tree (BST) for stock prices
root = TreeNode(60)
root.left = TreeNode(50)
root.right = TreeNode(70)
root.left.left = TreeNode(40)
root.left.right = TreeNode(55)

print("BFS Tree:", bfs.bfs_tree(root))  # Output: [60, 50, 70, 40, 55]
# How it works: Visits level by level (60, then 50, 70, then 40, 55)

# Graph for transaction network
graph = {
    '0': ['1', '2', '4'],
    '1': ['0', '2'],
    '2': ['0', '1', '4'],
    '3': ['4'],
    '4': ['0', '2', '3']
}

# Output: ['0', '1', '2', '4', '3']
print("BFS Graph from vertex 0:", bfs.bfs_graph(graph, '0'))
# How it works: Visits level by level (0, then 1, 2, 4, then 3)



"""   
         🟩 60
        /    \
    🟨 50     🟨 70
     /  \
  🟦 40  🟦 55

🟩 bfs_tree(60)
├── ✅ زيارة: 60
│   ├── 🔁 إضافة للصف: 50
│   └── 🔁 إضافة للصف: 70
├── ✅ زيارة: 50
│   ├── 🔁 إضافة للصف: 40
│   └── 🔁 إضافة للصف: 55
├── ✅ زيارة: 70
│   └── 🔕 لا يوجد أولاد
├── ✅ زيارة: 40
│   └── 🔕 لا يوجد أولاد
└── ✅ زيارة: 55
    └── 🔕 لا يوجد أولاد

[60, 50, 70, 40, 55]

"""