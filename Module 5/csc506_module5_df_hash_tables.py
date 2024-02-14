"""
  Kiran Ponappan Sreekumari 
  CSC506 – Design and Analysis of Algorithms 
  Colorado State University - Global
  Dr. Dong Nguyen 
  February 12, 2024
  Module 5: Discussion Forum 
  Explain the concept of a hash table. Then, compare it to other collection types such as dictionaries and sets.
"""
import time
import random
import matplotlib.pyplot as plt
import timeit 
import pandas as pd

class HashTable:
	def __init__(self, size):
		self.size = size
		self.table = [[] for _ in range(size)]  # Initialize hash table as a list of lists

	def _hash_function(self, key):
		return hash(key) % self.size

	def insert(self, key, value):
		index = self._hash_function(key)
		for pair in self.table[index]:
			if pair[0] == key:  # If key already exists, update the value
				pair[1] = value
				return
		self.table[index].append([key, value])  # Add key-value pair to the appropriate index

	def get(self, key):
		index = self._hash_function(key)
		for pair in self.table[index]:
			if pair[0] == key:  # If key is found, return its value
				return pair[1]
		return None  # Key not found

class Dictionary:
	def __init__(self) -> None:
		self.dict = {}
		
	def insert(self, key, value):
		self.dict[key] = value
		
	def get(self, key):
		return self.dict[key]


# Function to perform time complexity analysis
def time_complexity_analysis(data_sizes):
	execution_times = []

	for size in data_sizes:
		hash_table = HashTable(size)

		# Generate test data
		test_data = [(str(random.randint(1, 1000)), random.randint(1, 100)) for _ in range(size)]

		# Measure execution time
		start_time = time.time()
		for key, value in test_data:
			hash_table.insert(key, value)
		end_time = time.time()

		execution_times.append(end_time - start_time)

	return execution_times

# if __name__ == "__main__":
#     # Define input sizes
#     data_sizes = [1000, 2000, 3000, 4000, 5000]

#     # Perform time complexity analysis
#     execution_times = time_complexity_analysis(data_sizes)

#     # Plot results
#     plt.plot(data_sizes, execution_times, marker='o', linestyle='-')
#     plt.title('Hash Table Time Complexity Analysis')
#     plt.xlabel('Input Size')
#     plt.ylabel('Execution Time (seconds)')
#     plt.grid(True)
#     plt.show()

if __name__ == "__main__":
	performance = []
	for size in range(1,10000,100):
		test_data = [(str(random.randint(1, 1000)), random.randint(1, 100)) for _ in range(size)]
		hash_table = HashTable(size)
		hash_list = [hash_table.insert(key,value) for key,value in test_data]
		hash_list = [hash_table.get(key) for key,value in test_data]
		hash_insert_time = timeit.timeit(lambda: [hash_table.insert(key,value) for key,value in test_data.copy()], number=1)
		hash_get_time = timeit.timeit(lambda: [hash_table.get(key) for key,value in test_data.copy()], number=1)
		
		
		my_dict = Dictionary()
		dict_insert_time = timeit.timeit(lambda: [my_dict.insert(key, value) for key,value in test_data.copy()], number=1)
		dict_get_time = timeit.timeit(lambda: [my_dict.get(key) for key,value in test_data.copy()], number=1)
		
		# print(size,hash_insert_time, hash_get_time, dict_insert_time, dict_get_time)
		performance.append([size,hash_insert_time, hash_get_time, dict_insert_time, dict_get_time])
	
	columns = ["Range", "Hash Insert", "Hash Get", "Dict Insert", "Dict Get"]
	df = pd.DataFrame(performance, columns = columns)
	x = df['Range']
	fig, [(ax1, ax2),( ax3, ax4)] = plt.subplots(2,2, figsize=(15,6))
	fig.suptitle("Performance Comparison")
	ax1.plot(x, df[["Hash Insert", "Dict Insert"]])
	ax1.set_title("Insert")
	ax1.legend(["Hash Insert", "Dict Insert"], loc = "upper left")

	ax2.plot(x, df[["Hash Get", "Dict Get"]])
	ax2.set_title("Get")
	ax2.legend(["Hash Get", "Dict Get"], loc = "upper left")

	time_comparision = (df["Hash Insert"]-df["Dict Insert"])
	ax3.plot(x, time_comparision)
	ax3.set_title("Time Comparision")
	ax3.legend(["Time Comparision"], loc = "upper left")

	time_comparision = (df["Hash Get"]-df["Dict Get"])
	ax4.plot(x, time_comparision)
	ax4.set_title("Time Comparision")
	ax4.legend(["Time Comparision"], loc = "upper left")

	plt.show()
