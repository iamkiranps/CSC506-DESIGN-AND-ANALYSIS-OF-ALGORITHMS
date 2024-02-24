"""
  Kiran Ponappan Sreekumari 
  CSC506 – Design and Analysis of Algorithms 
  Colorado State University - Global
  Dr. Dong Nguyen 
  February 23, 2024
  Portfolio Project - Option #1: Analysis of Algorithms and Data Structures
"""
class ListNode:
    """Node structure for a linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __eq__(self, other):
        if isinstance(other, ListNode):
            return self.value == other.value
        return self.value == other

    def __lt__(self, other):
        if isinstance(other, ListNode):
            return self.value < other.value
        return self.value < other

    def __le__(self, other):
        if isinstance(other, ListNode):
            return self.value <= other.value
        return self.value <= other

    def __gt__(self, other):
        if isinstance(other, ListNode):
            return self.value > other.value
        return self.value > other

    def __ge__(self, other):
        if isinstance(other, ListNode):
            return self.value >= other.value
        return self.value >= other


class LinkedList:
    """Doubly linked list implementation."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_front(self, value):
        """Inserts a node at the front of the list."""
        if value is None:
            print("Will not insert None value into the list")
            return

        new_node = ListNode(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def insert_at_back(self, value):
        """Inserts a node at the back of the list."""
        if value is None:
            print("Will not insert None value into the list")
            return

        new_node = ListNode(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert_in_order(self, value):
        """Inserts a node in ascending order."""
        if value is None:
            print("Will not insert None value into the list")
            return

        new_node = ListNode(value)
        if self.length == 0:
            self.head = self.tail = new_node
            self.length = 1
        else:
            cur_node = self.head
            while cur_node and cur_node <= new_node:
                cur_node = cur_node.next

            if cur_node is None:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            elif cur_node is self.head:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                new_node.prev = cur_node.prev
                cur_node.prev.next = new_node
                new_node.next = cur_node
                cur_node.prev = new_node

            self.length += 1

    def remove_at_front(self):
        """Removes the node at the front of the list."""
        if self.length == 0:
            return None

        node = self.head
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return node

    def remove_at_back(self):
        """Removes the node at the back of the list."""
        if self.length == 0:
            return None

        node = self.tail
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return node

    def remove(self, item):
        """Removes a specific item from the list."""
        cur_node = self.head
        while cur_node:
            if cur_node == item:
                if cur_node is self.head and cur_node is self.tail:
                    self.head = self.tail = None
                elif cur_node is self.head:
                    cur_node.next.prev = None
                    self.head = cur_node.next
                elif cur_node is self.tail:
                    cur_node.prev.next = None
                    self.tail = cur_node.prev
                else:
                    cur_node.prev.next = cur_node.next
                    cur_node.next.prev = cur_node.prev
                self.length -= 1
                return True
            cur_node = cur_node.next
        return False

    def search(self, item):
        """Searches for a specific item in the list."""
        cur_node = self.head
        while cur_node:
            if cur_node == item:
                return True
            cur_node = cur_node.next
        return False

    def is_empty(self):
        """Checks if the list is empty."""
        return self.head is None and self.tail is None

    def get_length(self):
        """Returns the length of the list."""
        self.length = 0
        cur_node = self.head
        while cur_node:
            self.length += 1
            cur_node = cur_node.next
        return self.length

    def sort(self):
        """Sorts the list in ascending order using modified insertion sort."""
