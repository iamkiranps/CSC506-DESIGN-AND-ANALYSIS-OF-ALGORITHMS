"""
  Kiran Ponappan Sreekumari 
  CSC506 – Design and Analysis of Algorithms 
  Colorado State University - Global
  Dr. Dong Nguyen 
  February 23, 2024
  Portfolio Project - Option #1: Analysis of Algorithms and Data Structures
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from CSV
df = pd.read_csv('results/FullSize.csv')

# Extract data for each operation
insert_data = df[['Python Insert', 'Numpy Insert', 'Linked List Insert']]
search_data = df[['Python Search', 'Numpy Search', 'Linked List Search']]
delete_data = df[['Python Delete', 'Numpy Delete', 'Linked List Delete']]

python_data = df[['Python Insert', 'Python Search', 'Python Delete']]
numpy_data = df[['Numpy Insert', 'Numpy Search', 'Numpy Delete']]
linkedlist_data = df[['Linked List Insert', 'Linked List Search', 'Linked List Delete']]

def plot_1():
  # Create a figure and subplots
  fig, axs = plt.subplots(3, 1, figsize=(10, 10))

  # Plot insert operation comparison
  axs[0].plot(insert_data)
  axs[0].set_title('Insert Operation Comparison')
  axs[0].set_xlabel('Iterations')
  axs[0].set_ylabel('Time (nanoseconds)')
  axs[0].legend(insert_data.columns)

  # Plot search operation comparison
  axs[1].plot(search_data)
  axs[1].set_title('Search Operation Comparison')
  axs[1].set_xlabel('Iterations')
  axs[1].set_ylabel('Time (nanoseconds)')
  axs[1].legend(search_data.columns)

  # Plot delete operation comparison
  axs[2].plot(delete_data)
  axs[2].set_title('Delete Operation Comparison')
  axs[2].set_xlabel('Iterations')
  axs[2].set_ylabel('Time (nanoseconds)')
  axs[2].legend(delete_data.columns)

  # Adjust layout
  plt.tight_layout()

  # Show the plot
  plt.show()

def plot_2():
  # Create a figure and subplots
  fig, axs = plt.subplots(3, 1, figsize=(10, 10))

  # Plot insert operation comparison
  axs[0].plot(python_data)
  axs[0].set_title('Python List Operation Comparison')
  axs[0].set_xlabel('Iterations')
  axs[0].set_ylabel('Time (nanoseconds)')
  axs[0].legend(python_data.columns)

  # Plot search operation comparison
  axs[1].plot(numpy_data)
  axs[1].set_title('Numpy Array Operation Comparison')
  axs[1].set_xlabel('Iterations')
  axs[1].set_ylabel('Time (nanoseconds)')
  axs[1].legend(numpy_data.columns)

  # Plot delete operation comparison
  axs[2].plot(linkedlist_data)
  axs[2].set_title('Linked List Operation Comparison')
  axs[2].set_xlabel('Iterations')
  axs[2].set_ylabel('Time (nanoseconds)')
  axs[2].legend(linkedlist_data.columns)

  # Adjust layout
  plt.tight_layout()

  # Show the plot
  plt.show()

if __name__ == '__main__':
  plot_2()
