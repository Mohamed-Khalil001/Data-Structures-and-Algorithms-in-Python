# Trees and Graphs Lecture 6
# This code implements a Binary Search Tree for stock prices and a Graph for stock correlations.
# Time complexity is analyzed using Big O Notation.
# The example is tailored for quantitative analysis (e.g., stock classification and correlation analysis).

# -----------------------------------------------
# Data Structure: Binary Search Tree (BST)
# Definition: A tree data structure where each node has at most two children (left and right).
#             In a BST, the left child's value is less than the parent's value, and the right child's value is greater.
# Properties:
# - Root: The topmost node of the tree.
# - Parent/Children: Each node can be a parent to up to two children (left and right).
# - Levels: The tree is organized in levels, with the root at level 0.
# - No cycles: A tree cannot have circular references.
# - Connected: All nodes are reachable from the root.
# - Use Case: Efficient for searching, inserting, and sorting (e.g., stock prices).
# Time Complexity:
# - Insert/Search: O(h) where h is the height of the tree (O(log n) for balanced trees, O(n) for unbalanced).
# ---------------------------------------------------------------------------------------------------------------------

# remeber the recrecursion

def recursion_print(n):
    if n == 0:
        print("finished")
    else:
        print(n)
        recursion_print(n-1)


recursion_print(5)


class treenode:
    def __init__(self, price):
        """
        intializing a node for the tree 
        time complexity o(1) 
        """
        self.price = price
        self.left = None
        self.right = None


class stockbst:
    def __init__(self):
        """
        intializing root fot the tree 
        o(1)
        """

        self.root: treenode = None

    def insert(self, price):
        """
        inserting node to the tree
        o(h)
        """
        if self.root is None:
            self.root = treenode(price)
        else:
            self.insert_recursive(self.root, price)

    def insert_recursive(self, node, price):
        """
        differrential inserting of the price in the tree 
        o(h) 
        """

        if price < node.price:
            if node.left is None:
                node.left = treenode(price)
            else:
                self.insert_recursive(node.left, price)
        if price > node.price:
            if node.right is None:
                node.right = treenode(price)
            else:
                self.insert_recursive(node.right, price)

    def print_inorder(self):
        self._print_inorder_recursive(self.root)

    def _print_inorder_recursive(self, node):
        if node:
            self._print_inorder_recursive(node.left)
            print(node.price)
            self._print_inorder_recursive(node.right)


# Testing the Implementations
# Binary Search Tree
stock_bst = stockbst()
stock_bst.insert(300.00)
stock_bst.insert(295.50)
stock_bst.insert(305.50)


stock_bst.print_inorder()


# Properties:
# - Vertices (Nodes): Represent entities (e.g., stocks).
# - Edges: Represent relationships (e.g., correlation between stocks).
# - Directed/Undirected: Directed graphs have edges with direction (e.g., follower relationships);
#                       undirected graphs have mutual relationships (e.g., friendships).
# - Weighted/Unweighted: Edges can have weights (e.g., correlation values) or be unweighted.
# - Cycles: Graphs can have cycles (unlike trees).
# - Connectivity: Graphs can have unconnected nodes (unlike trees).
# - Use Case: Analyze relationships, optimize routes, or model networks (e.g., financial correlations).
# Time Complexity:
# - Add Vertex/Edge: O(1)
# - Get Neighbors: O(1) average
# -----------------------------------------------
class StockCorrelationGraph:
    def __init__(self):
        """
        Initializes an empty graph using an adjacency list.
        Time Complexity: O(1)
        """
        self.graph = {}

    def add_vertex(self, stock):
        """
        Adds a stock to the graph.
        Time Complexity: O(1)
        """
        if stock not in self.graph:
            self.graph[stock] = []

    def add_edge(self, stock1, stock2, correlation):
        """
        Adds an undirected edge with correlation weight.
        Time Complexity: O(1)
        """
        self.add_vertex(stock1)
        self.add_vertex(stock2)
        self.graph[stock1].append((stock2, correlation))
        self.graph[stock2].append((stock1, correlation))

    def get_neighbors(self, stock):
        """
        Returns neighbors with their correlations.
        Time Complexity: O(1) average
        """
        return self.graph.get(stock, [])

    def get_vertices(self):
        """
        Returns all stocks in the graph.
        Time Complexity: O(1)
        """
        return list(self.graph.keys())


# Graph
stock_graph = StockCorrelationGraph()
stock_graph.add_edge("TSLA", "AAPL", 0.75)
stock_graph.add_edge("TSLA", "GOOG", 0.60)
stock_graph.add_edge("AAPL", "GOOG", 0.65)
# Output: [('AAPL', 0.75), ('GOOG', 0.60)]
print("\nTSLA Neighbors:", stock_graph.get_neighbors("TSLA"))
# Output: ['TSLA', 'AAPL', 'GOOG']
print("All Stocks:", stock_graph.get_vertices())


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, source, target):
        self.vertices[source].append(target)


my_graph = Graph()

# Create the vertices
my_graph.add_vertex('Paris')
my_graph.add_vertex('Toulouse')
my_graph.add_vertex('Biarritz')


# Create the edges
my_graph.add_edge('Paris', 'Toulouse', 678)
my_graph.add_edge('Toulouse', 'Biarritz', 312)
my_graph.add_edge('Biarritz', 'Paris', 783)
