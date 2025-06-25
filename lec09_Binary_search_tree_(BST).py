# Binary Search Tree (BST) Lecture Code
# Implements BST operations for financial data.
# Time Complexity: Analyzed per function.
# Example: Managing stock prices in quantitative analysis.

# --------------------------------------------
# Concept: Binary Search Tree (BST)
# Definition: A binary tree where each node has at most two children, with left subtree values less than the node and right subtree values greater.
# Properties:
# - Each node has 0, 1, or 2 children.
# - Left subtree: All nodes have values < current node.
# - Right subtree: All nodes have values > current node.
# - Operations:
#   - Search: O(log n) average, O(n) worst case (unbalanced tree).
#   - Insert: O(log n) average, O(n) worst case.
#   - Delete: O(log n) average, O(n) worst case.
# Use Case: Efficiently manage sorted financial data like stock prices or transactions.
# --------------------------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data  # Store stock price or value
        self.left = None  # Left child (smaller values)
        self.right = None  # Right child (larger values)


class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize empty tree

    def search(self, value):
        """
        Searches for a value in the BST.
        Time Complexity: O(log n) average, O(n) worst case
        """
        current = self.root  # Start at root
        while current:  # While there are nodes to check
            if value == current.data:  # If value matches current node
                return True  # Found it
            elif value < current.data:  # If value is smaller
                current = current.left  # Go left
            else:  # If value is larger
                current = current.right  # Go right
        return False  # Value not found

    def insert(self, data):
        """
        Inserts a new value into the BST.
        Time Complexity: O(log n) average, O(n) worst case
        """
        new_node = TreeNode(data)  # Create new node
        if not self.root:  # If tree is empty
            self.root = new_node  # Set as root
            return
        current = self.root  # Start at root
        while True:  # Loop until inserted
            if data < current.data:  # If new value is smaller
                if not current.left:  # If no left child
                    current.left = new_node  # Insert here
                    break
                current = current.left  # Move to left child
            else:  # If new value is larger or equal
                if not current.right:  # If no right child
                    current.right = new_node  # Insert here
                    break
                current = current.right  # Move to right child

    def find_min(self, node):
        """
        Finds the smallest value in a subtree (used for deletion).
        Time Complexity: O(h) where h is tree height
        """
        current = node  # Start at given node
        while current.left:  # Keep going left
            current = current.left  # Move to left child
        return current  # Return node with smallest value

    def delete(self, value):
        """
        Deletes a value from the BST.
        Time Complexity: O(log n) average, O(n) worst case
        """
        def delete_node(node, value):
            if not node:  # If node is None
                return None
            if value < node.data:  # If value is smaller
                node.left = delete_node(node.left, value)  # Recurse left
            elif value > node.data:  # If value is larger
                node.right = delete_node(node.right, value)  # Recurse right
            else:  # Found the node to delete
                if not node.left and not node.right:  # Case 1: No children
                    return None  # Delete by returning None
                if not node.left:  # Case 2: Only right child
                    return node.right  # Replace with right child
                if not node.right:  # Case 2: Only left child
                    return node.left  # Replace with left child
                # Case 3: Two children
                successor = self.find_min(node.right)  # Find successor
                node.data = successor.data  # Replace with successor's value
                node.right = delete_node(
                    node.right, successor.data)  # Delete successor
            return node
        self.root = delete_node(self.root, value)  # Update root


# Testing
bst = BinarySearchTree()

# Insert stock prices
bst.insert(60)  # Root
bst.insert(50)  # Left child of 60
bst.insert(70)  # Right child of 60
bst.insert(65)  # Left child of 70
print("Search 65:", bst.search(65))  # Output: True
# How it works: Start at 60, go right to 70, go left to 65, found

# Delete a node with no children
bst.delete(65)  # Delete 65 (leaf node)
print("Search 65 after delete:", bst.search(65))  # Output: False
# How it works: 65 is a leaf, so it's removed

# Delete a node with one child
bst.insert(65)  # Re-insert 65
bst.insert(62)  # Left child of 65
bst.delete(65)  # Delete 65 (has one child)
print("Search 62:", bst.search(62))  # Output: True
# How it works: 65 replaced by 62

# Delete a node with two children
bst.insert(65)  # Re-insert 65
bst.insert(68)  # Right child of 65
bst.delete(60)  # Delete root (has two children)
print("Search 60:", bst.search(60))  # Output: False
print("Search 62:", bst.search(62))  # Output: True
# How it works: 60 replaced by successor (62), 62 deleted
