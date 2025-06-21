# Lec 4 QUEUES
# This code implements a Queue using a Singly Linked List for processing stock trade orders.
# Time complexity is analyzed using Big O Notation.
# The example is tailored for quantitative analysis (e.g., managing trade order execution).

# Queues are a data structure that operates on the FIFO (First-In-First-Out) principle, meaning "the first one in is the first one out.
# It’s like a line of people at a supermarket — the person who arrives first gets served first.
# Stack differs from Queues in adding and removing happens in the only top direction last in first out

import queue
from queue import Queue
from queue import SimpleQueue


class Node:
    def __init__(self, data):
        """
        intializing new Node 
        Time complexity o(1)
        """
        self.data = data
        self.next = None


class linkedstocksqueues():
    def __init__(self):
        """
        intializing empty Queue
        Time complexity o(1) 
        """
        self.head: Node = None   # : Node  as defined as node so it can auto completed by attributes
        self.tail: Node = None

    def enqueue(self, stock):
        """
        add Node to the Queue (to the tail )
        Time complexity o(1)
        """
        new_node = Node(stock)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        """
        remove node from the Queue (from the head) and return it 
        Time complexity o(1)
        """
        if self.head is None:
            return None
        deueue_node = self.head
        self.head = self.head.next
        deueue_node.next = None  # لعزل النود دي
        return deueue_node.data

    def peek(self):
        """
        return first node of the queue without remove it 
        Time complexity o(1)
        """
        return self.head.data if self.head is not None else None

    def empty(self):
        """
        yes or no : is  Queue is empty !?
        Time complexity o(1)
        """
        if self.head is None or self.tail is None:
            print('Queue is empty ')

    def size(self):
        """
        finding the size of Queue
        Time Complexity: O(n) - Must traverse all nodes
        """
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count


# Testing the Queue
order_queue = linkedstocksqueues()

# Adding stock orders (O(1) each)
order_queue.enqueue(
    {"price": 300.00, "timestamp": "2025-06-11 08:00", "type": "buy"})
order_queue.enqueue(
    {"price": 305.50, "timestamp": "2025-06-11 09:00", "type": "sell"})
order_queue.enqueue(
    {"price": 307.75, "timestamp": "2025-06-11 10:00", "type": "buy"})

# Peek at the first order (O(1))
print("First Order:", order_queue.peek())  # Output: {'price': 300.00, ...}

# Dequeue an order (O(1))
# Output: {'price': 300.00, ...}
print("Dequeued Order:", order_queue.dequeue())
print("New First Order:", order_queue.peek())  # Output: {'price': 305.50, ...}

# Check queue size (O(n))
print("Queue Size:", order_queue.size())  # Output: 2

# Check if queue is empty (O(1))
print("Is Queue Empty?", order_queue.empty())  # Output: False


print("\n &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& \n")


# we can use this built in class instead of building one to make Queue
# Create queue
order_queue = Queue()

# Enqueue
order_queue.put(
    {"price": 300.00, "timestamp": "2025-06-11 08:00", "type": "buy"})
order_queue.put(
    {"price": 305.50, "timestamp": "2025-06-11 09:00", "type": "sell"})
order_queue.put(
    {"price": 307.75, "timestamp": "2025-06-11 10:00", "type": "buy"})

# Peek at the first item
print("First Order:", order_queue.queue[0])

# Dequeue
print("Dequeued Order:", order_queue.get())

# Peek again
print("New First Order:", order_queue.queue[0])

# Size
print("Queue Size:", order_queue.qsize())

# Is empty
print("Is Queue Empty?", order_queue.empty())
