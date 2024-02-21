"""
  Kiran Ponappan Sreekumari 
  CSC506 – Design and Analysis of Algorithms 
  Colorado State University - Global
  Dr. Dong Nguyen 
  February 20, 2024
  Module 6: Critical Thinking - Option #2: Driver Script
"""
import random
from graphviz import Digraph
from gvgen import GvGen
from binarytree import build 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def build_tree(self, values):
        for value in values:
            self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    def balanced(self):
        return self._balanced(self.root)

    def _balanced(self, node):
        if node is None:
            return True
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return abs(left_height - right_height) <= 1 and \
               self._balanced(node.left) and \
               self._balanced(node.right)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def level_order(self):
        if self.root is None:
            return []
        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def pre_order(self, node):
        if node is None:
            return []
        result = [node.value]
        result += self.pre_order(node.left)
        result += self.pre_order(node.right)
        return result

    def post_order(self, node):
        if node is None:
            return []
        result = self.post_order(node.left)
        result += self.post_order(node.right)
        result.append(node.value)
        return result

    def in_order(self, node):
        if node is None:
            return []
        result = self.in_order(node.left)
        result.append(node.value)
        result += self.in_order(node.right)
        return result

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def rebalance(self):
        values = self.in_order(self.root)
        self.root = self._build_balanced(values)

    def _build_balanced(self, values):
        if not values:
            return None
        mid = len(values) // 2
        root = Node(values[mid])
        root.left = self._build_balanced(values[:mid])
        root.right = self._build_balanced(values[mid + 1:])
        return root

    # def display_tree_structure(self):
    #     self._display_tree_structure(self.root, 0)

    # def _display_tree_structure(self, node, depth):
    #     if node is None:
    #         return
    #     self._display_tree_structure(node.right, depth + 1)
    #     print("    " * depth, node.value)
    #     self._display_tree_structure(node.left, depth + 1)    

    def display_tree_structure(self):
        g = GvGen()
        self._build_dot(self.root, g)
        g.write('binary_search_tree.dot')
        print("DOT file of the tree structure has been saved as 'binary_search_tree.dot'")

    def _build_dot(self, node, g):
        if node is None:
            return
        if node.left:
            g.edge(str(node.value), str(node.left.value))
            self._build_dot(node.left, g)
        if node.right:
            g.edge(str(node.value), str(node.right.value))
            self._build_dot(node.right, g)

    def display_full_tree(self):
        tree = self._build_binary_tree(self.root)
        print(tree)

    def _build_binary_tree(self, node):
        if node is None:
            return None
        left_tree = self._build_binary_tree(node.left)
        right_tree = self._build_binary_tree(node.right)
        return Node(node.value, left_tree, right_tree)
    
# Driver script
if __name__ == "__main__":
    bst = BinarySearchTree()
    random_numbers = random.sample(range(1, 101), 15)
    print("Random numbers array:", random_numbers)
    bst.build_tree(random_numbers)
    # bst.display_full_tree()
    print("Tree is balanced:", bst.balanced())
    print("Level order:", bst.level_order())
    # print(build(bst.level_order()))
    print("Pre order:", bst.pre_order(bst.root))
    print("Post order:", bst.post_order(bst.root))
    print("In order:", bst.in_order(bst.root))
    # bst.display_tree_structure()
    print()

    # Unbalance the tree
    random_numbers = random.sample(range(101, 150), 5)
    print("New Random Numbers : ", random_numbers)

    for num in random_numbers:
        bst.insert(num)

    print("Tree is unbalanced:", not bst.balanced())
    print("Level order:", bst.level_order())
    print("Pre order:", bst.pre_order(bst.root))
    print("Post order:", bst.post_order(bst.root))
    print("In order:", bst.in_order(bst.root))
    print()

    # Balance the tree
    bst.rebalance()
    print("Tree is balanced:", bst.balanced())
    print("Level order:", bst.level_order())
    print("Pre order:", bst.pre_order(bst.root))
    print("Post order:", bst.post_order(bst.root))
    print("In order:", bst.in_order(bst.root))
