# lec 3 stacks
# this code imolements a stack using singly linked list , demonstating push , pop and peek operations .
# this example is tailored for quantitstive analysis (e.g track stock transactions )
# time complexity is analyzed using big o notation

# Stacks are a data structure that operates on the LIFO principle — Last In, First Out. This means that the last item added is the first one to be removed.

class Node:
    def __init__(self, data):
        """
        intializing the node with transaction data and  next pointer .
        Time complexity : O(1)
        """
        self.data = data  # transaction data (e.g., {"price": 300.00, "timestamp": "2025-06-11 08:00", "type": "buy"})
        self.next = None


class stockstransactionstack:

    def __init__(self):
        """
        intializing empty stack with one only set(node) equals None
        Time Complexity o(1)
        """
        self.top: Node  # identify top as node use it for Attributes (autocomplete)
        self.top = None

    def push(self, transaction):
        """
        pushes add a new transaction onto the top of the stack 
        Time complexity o(1)
        """
        new_node = Node(transaction)
        new_node.next = self.top
        self.top = new_node
        # top(last element added) → [5] → [4] → [3] → None (stack)

    def pop(self):
        """
        pop remove the top transaction and return it from the stack 
        Time complexity o(1)
        """
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next  # تغيير التوب
        popped_node.next = None  # فك الارتباط
        return popped_node.data

    def peek(self):
        """
        peek return the top transaction without removing 
        Time complexity o(1)
        """
        return self.top.data if self.top is not None else None

    def size(self):
        """
        Returns the number of transactions in the stack.
        Time Complexity: O(n) - Must traverse all nodes
        """
        count = 0
        current = self.top
        while current is not None:
            count += 1
            current = current.next
        return count


# Testing the Stack
stock_stack = stockstransactionstack()

# Adding stock transactions (O(1) each)
stock_stack.push(
    {"price": 300.00, "timestamp": "2025-06-11 08:00", "type": "buy"})
stock_stack.push(
    {"price": 305.50, "timestamp": "2025-06-11 09:00", "type": "buy"})
stock_stack.push(
    {"price": 307.75, "timestamp": "2025-06-11 10:00", "type": "sell"})

# Peek at the latest transaction (O(1))
# Output: {'price': 307.75, 'timestamp': '2025-06-11 10:00', 'type': 'sell'}
print("Latest Transaction:", stock_stack.peek())

# Pop a transaction (O(1))
# Output: {'price': 307.75, 'timestamp': '2025-06-11 10:00', 'type': 'sell'}
print("Popped Transaction:", stock_stack.pop())
# Output: {'price': 305.50, 'timestamp': '2025-06-11 09:00', 'type': 'buy'}
print("New Latest Transaction:", stock_stack.peek())
# Check stack size (O(n))
print("Stack Size:", stock_stack.size())  # Output: 2
