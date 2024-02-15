"""
  Kiran Ponappan Sreekumari 
  CSC506 – Design and Analysis of Algorithms 
  Colorado State University - Global
  Dr. Dong Nguyen 
  February 15, 2024
  Module 5: Critical Thinking : Option #1: Linear Probing
  Illustrate the linear probing method in hashing. Explain its performance analysis. 
  Lastly, discuss how rehashing overcomes the drawbacks of linear probing. Provide at least one visual in your activity.
"""
import timeit
import random
import pandas as pd
import matplotlib.pyplot as plt

class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            index = (index + 1) % self.size

        self.keys[index] = key
        self.values[index] = value

    def search(self, key):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size

        return None

    def delete(self, key):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return
            index = (index + 1) % self.size

    def display(self):
        print(f"Index |Hash |Key |Value")
        for i in range(self.size):
                print(f"{i}     |{self.hash_function(0 if not self.keys[i] else self.keys[i])}    |{self.keys[i]}   |{self.values[i]}")

class ReHashTable:
    def __init__(self, initial_size):
        self.size = initial_size
        self.keys = [None] * initial_size
        self.values = [None] * initial_size
        self.load_factor = 0.7  # Threshold for rehashing
        self.load_factor_kv = []

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):      
        if self.load_factor > 0.7:
            self.rehash()

        index = self.hash_function(key)
        # self.load_factor_kv.append(self.load_factor)

        while self.keys[index] is not None:
            index = (index + 1) % self.size

        self.keys[index] = key
        self.values[index] = value

        # Recalculate load factor
        self.load_factor = sum(1 for key in self.keys if key is not None) / self.size
        self.load_factor_kv.append(self.load_factor)
        # print(self.load_factor, self.load_factor_kv, key, value)

    def search(self, key):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size

        return None

    def delete(self, key):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return
            index = (index + 1) % self.size

    def rehash(self):
        new_size = self.size * 2
        new_keys = [None] * new_size
        new_values = [None] * new_size

        for i in range(self.size):
            if self.keys[i] is not None:
                new_index = self.hash_function(self.keys[i]) % new_size

                while new_keys[new_index] is not None:
                    new_index = (new_index + 1) % new_size

                new_keys[new_index] = self.keys[i]
                new_values[new_index] = self.values[i]

        self.keys = new_keys
        self.values = new_values
        self.size = new_size
        self.load_factor = sum(1 for key in self.keys if key is not None) / self.size

        print("Rehashing completed. New size:", new_size)
        
    def display(self):
        print(f"Index |Hash |Key |Value")
        for i in range(self.size):
                print(f"{i}     |{self.hash_function(0 if not self.keys[i] else self.keys[i])}    |{self.keys[i]}   |{self.values[i]}")		

# Test the HashTable class
if __name__ == "__main__":
    hash_table = HashTable(10)

    # Insert key-value pairs
    hash_table.insert(1, "pine apple")
    hash_table.insert(5, "apple")
    hash_table.insert(15, "banana")
    hash_table.insert(25, "orange")
    hash_table.insert(35, "grapes")
    hash_table.insert(45, "blue berry")
    hash_table.insert(55, "straw berry")

    # Display the hash table
    print("Hash Table:")
    hash_table.display()

    # Search for a key
    print("\nSearch for key 25:")
    print(hash_table.search(25))  # Output: orange

    # Delete a key
    print("\nDeleting key 15:")
    hash_table.delete(15)
    print("Updated Hash Table:")
    hash_table.display()
    
    performance = []
    rehash_performance = []
    for i in range(1,1000):
        hash_table_1 = HashTable(i)
        hash_table_2 = HashTable(i)
        random_list_10 = [random.randint(1, 10) for _ in range(i)]
        random_list_1000 = [random.randint(1, 1000) for _ in range(i)]
        hash_insert_time_10 = timeit.timeit(lambda: [hash_table_1.insert(num,num) for num in random_list_10.copy()], number=1)
        hash_insert_time_1000 = timeit.timeit(lambda: [hash_table_2.insert(num,num) for num in random_list_1000.copy()], number=1)
        performance.append([i, hash_insert_time_10, hash_insert_time_1000])

        # rehash_table_1 = ReHashTable(i)
        # rehash_table_2 = ReHashTable(i)
        # rehash_insert_time_10 = timeit.timeit(lambda: [rehash_table_1.insert(num,num) for num in random_list_10.copy()], number=1)
        # rehash_insert_time_1000 = timeit.timeit(lambda: [rehash_table_2.insert(num,num) for num in random_list_1000.copy()], number=1)
        # rehash_performance.append([i, hash_insert_time_10, rehash_insert_time_10])


    df = pd.DataFrame(performance, columns=['Range','Random 10','Random 1000'])
    df.plot(x='Range', y=['Random 10', 'Random 1000'])
    plt.title("Linear Probing Performance")
    plt.ylabel("Time")
    plt.show()

    # df2 = pd.DataFrame(rehash_performance, columns=['Range','Hash','Rehash'])
    # df2.plot(x='Range', y=['Hash', 'Rehash'])
    # plt.title("Linear Probing Performance")
    # plt.ylabel("Time")
    # plt.show()
    

    rehash_table = ReHashTable(10)
    # Insert key-value pairs
    rehash_table.insert(1, "pine apple")
    rehash_table.insert(5, "apple")
    rehash_table.insert(15, "banana")
    rehash_table.insert(25, "orange")
    rehash_table.insert(35, "grapes")
    rehash_table.insert(45, "blue berry")
    rehash_table.insert(55, "straw berry")
    rehash_table.insert(65, "avacado")
    rehash_table.insert(75, "raspberry")
    # rehash_table.insert(85, "straw berry4")
    # hash_table.insert(95, "straw berry5")
    # rehash_table.insert(105, "straw berry6")

    # for i in range(1, 21):
    #     rehash_table.insert(i, f"value_{i}")
        
    # Display the hash table
    print("ReHash Table:")
    rehash_table.display()