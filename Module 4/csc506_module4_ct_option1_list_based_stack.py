"""
  Kiran Ponappan Sreekumari 
  CSC506 – Design and Analysis of Algorithms 
  Colorado State University - Global
  Dr. Dong Nguyen 
  February 5, 2024
  Module 4: Module 4: Critical Thinking - Option #1: List Based Stack. 
  Design and implement an experiment that will compare the performance of the Python list based stack and queue with the linked list implementation.
"""
import random
import timeit
import pandas as pd
import matplotlib.pyplot as plt

class Stack:
    def __init__(self):
        """Initilize python list as the base"""
        self.items = []

    def push(self, item):
        """Adds item to the stack"""
        self.items.append(item)

    def pop(self):
        """Removes item from the top of the stack"""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        """Return the last item in the stack"""
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0

    def size(self):
        """Return the size of the stack"""
        return len(self.items)

class Node:
    def __init__(self, data = None):
        """Initilize the node"""
        self.data = data
        self.next = None

class DoublyLinkedList:
    """Doubly Linked List"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check if empty"""
        return self.head is None

    def append(self, data):
        """Add data to the linked list"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        """Add data to the back"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

class Queue:
    def __init__(self):
        """Initialize Queue using linked list"""
        self.queue = DoublyLinkedList()

    def is_empty(self):
        """Check if queue is empty"""
        return self.queue.is_empty()

    def enqueue(self, data):
        """Add data to queue (linked list)"""
        self.queue.append(data)

    def dequeue(self):
        """Remove data from queue"""
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            removed_item = self.queue.head.data
            self.queue.head = self.queue.head.next
            if self.queue.head:
                self.queue.head.prev = None
            return removed_item

    def peek(self):
        """Find front of queue (head of the linked list)"""
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.queue.head.data

    def size(self):
        """Check size of queue"""
        current = self.queue.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count


if __name__ == "__main__":
    n_numbers = 10
    random_list = [random.randint(1, n_numbers) for _ in range(n_numbers)]
    
    stack = Stack()
    stack_push_time = timeit.timeit(lambda: [stack.push(num) for num in random_list.copy()], number=1)
    print(stack.size(),stack_push_time)
    stack_seek_time = timeit.timeit(lambda: [stack.peek() for _ in random_list.copy()], number=1)
    print(stack.size(),stack_seek_time)
    stack_pop_time = timeit.timeit(lambda: [stack.pop() for _ in random_list.copy()], number=1)
    print(stack.size(),stack_pop_time)
    
    queue = Queue()
    queue_push_time = timeit.timeit(lambda: [queue.enqueue(num) for num in random_list.copy()], number=1)
    print(queue.size(),queue_push_time)
    queue_seek_time = timeit.timeit(lambda: [queue.peek() for _ in random_list.copy()], number=1)
    print(queue.size(),queue_seek_time)
    queue_pop_time = timeit.timeit(lambda: [queue.dequeue() for _ in random_list.copy()], number=1)
    print(queue.size(),queue_pop_time)
    
    lst = []
    cols = ['Range', "Stack Push", "Stack Peek", "Stack Pop", "Queue Push", "Queue Peek", "Queue Pop"]
    
    for i in range(1,1000):
        random_list = [random.randint(1, i) for _ in range(i)]

        stack = Stack()
        stack_push_time = timeit.timeit(lambda: [stack.push(num) for num in random_list.copy()], number=1)
        stack_peek_time = timeit.timeit(lambda: [stack.peek() for _ in random_list.copy()], number=1)
        stack_pop_time = timeit.timeit(lambda: [stack.pop() for _ in random_list.copy()], number=1)
    
        queue = Queue()
        queue_push_time = timeit.timeit(lambda: [queue.enqueue(num) for num in random_list.copy()], number=1)
        queue_peek_time = timeit.timeit(lambda: [queue.peek() for _ in random_list.copy()], number=1)
        queue_pop_time = timeit.timeit(lambda: [queue.dequeue() for _ in random_list.copy()], number=1)
        
        lst.append([i, stack_push_time, stack_peek_time, stack_pop_time, queue_push_time, queue_peek_time, queue_pop_time])
    
    """**Plot (Log Scale)**"""
    # df = pd.DataFrame(lst, columns = cols)
     
	# # print(df)
    # x = df['Range']
    # y_cols= ["Stack Push", "Stack Peek", "Stack Pop", "Queue Push", "Queue Peek", "Queue Pop"]
    # y = df[y_cols]
        
	# # Plot the time in matplotlib
    # plt.figure(figsize=(10, 6))
    # for col in y_cols:
    #     plt.plot(x, y[col],  label=col)
               
    # plt.title('Performance Comparison')
    # plt.xlabel('Range')
    # plt.ylabel('Time Taken (s)')
    # plt.xscale('log')  # Log scale for x-axis
    # plt.yscale('log')  # Log scale for y-axis
    # plt.grid(True)
    # plt.legend()
    # # plt.show()

    df = pd.DataFrame(lst, columns = cols)
    x = df['Range']
    fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(15,6))
    fig.suptitle("Performance Comparison")
    ax1.plot(x, df[["Stack Push", "Queue Push"]])
    ax1.set_title("Push")
    # ax1.loglog()  # Log scale for x-axis
    ax1.legend(["Stack Push", "Queue Push"], loc = "upper left")

    
    ax2.plot(x, df[["Stack Peek", "Queue Peek"]])
    ax2.set_title("Peek")
    # ax2.loglog()  # Log scale for x-axis
    ax2.legend(["Stack Peek", "Queue Peek"], loc = "upper left")

    ax3.plot(x, df[["Stack Pop", "Queue Pop"]])
    ax3.set_title("Pop")
    # ax3.loglog()  # Log scale for x-axis
    ax3.legend(["Stack Pop", "Queue Pop"], loc = "upper left")

    plt.show()