"""
  Kiran Ponappan Sreekumari 
  CSC506 – Design and Analysis of Algorithms 
  Colorado State University - Global
  Dr. Dong Nguyen 
  February 5, 2024
  Module 4: Module 4: Discussion Forum - Create a queue data structure using two stacks 
"""
class Queue:
	def __init__(self) -> None:
		"""
		Initilize queue
		"""
		self.s1 = []
		self.s2 = []
	
	def enqueue(self, item):
		"""
		Add item into the Queue
		"""
		while self.s1:
			self.s2.append(self.s1.pop())
			
		self.s1.append(item)
		
		while self.s2:
			self.s1.append(self.s2.pop())
	
	def dequeue(self):
		"""
		Remove item into the queue
		"""
		if self.s1:
			return self.s1.pop()
		else:
			return "Queue is empty"
	
	def peek(self):
		"""
		Get the front element
		"""
		return self.s1[-1]
	
	def empty(self):
		"""
		Check if queue is empty
		"""
		return not self.s1
	
	def size(self):
		"""
		Check size if queue
		"""
		return len(self.s1) + len(self.s2)
	
if __name__ == "__main__":
	queue = Queue()
	print("Dequeue : ", queue.dequeue()) #Queue is empty
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)
	print("Size : ", queue.size()) #Queue size is 3
	print("Who is in the front : ", queue.peek()) # 1 is in the front
	
	print("Dequeue : ", queue.dequeue()) #Dequeue 1
	print("Dequeue : ", queue.dequeue()) #Dequeue 2
	print("Size : ", queue.size()) #Queue size is 1
	print("Who is in the front : ", queue.peek()) # 3 is in the front

	queue.enqueue(4)
	print("Dequeue : ", queue.dequeue()) #Dequeue 3
	print("Dequeue : ", queue.dequeue()) #Dequeue 4
	print("Dequeue : ", queue.dequeue()) #Queue is empty
	print("Size : ", queue.size()) #Queue size is 0
	
#Good to go. Thank you.