"""
  Kiran Ponappan Sreekumari 
  CSC506 – Design and Analysis of Algorithms 
  Colorado State University - Global
  Dr. Dong Nguyen 
  February 23, 2024
  Portfolio Project - Option #1: Analysis of Algorithms and Data Structures
"""
import pandas as pd
import numpy as np
import os 
import timeit
import bookshelf
from progressbar import progressbar


def load_data() -> pd.DataFrame:
    """Loads all book data for the program."""
    column_list = ['title', 'isbn13', 'num_pages']
    data_path = 'books.csv'

    try:
        df = pd.read_csv(data_path, usecols=column_list)
        df['num_pages'] = df['num_pages'].astype(np.int64, errors="raise")
        df['isbn13'] = df['isbn13'].astype(np.int64, errors="raise")
        print("Data load: Success")
        return df
    except Exception as e:
        print(f"Data load: Failed - {e}")
        exit(0)

def run_tests(iterations):
    """Run all of the tests and records the data for the provided number of iterations"""

    data = load_data()
    totalPages = data['num_pages'].sum()
    results = []
    columns = ['Python Insert', 'Numpy Insert', 'Linked List Insert', 'Python Search', 'Numpy Search', 'Linked List Search', 'Python Delete', 'Numpy Delete', 'Linked List Delete']
    dfFull, dfThreeQuater, dfHalf, dfQuarter = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    print(iterations)

    for i in range(iterations):
        print(f"\n\n***** Running Iteration - {i+1} out of {iterations} *****\n\n")

        shuffled_data = data.sample(frac=1, random_state=i)
        search_data = data.sample(frac=.1, random_state=i)
        delete_data = data.sample(frac=.1, random_state=i*i)

        for j in progressbar(range(1,5)):
            print(f"\n*** Running Subtest - {j} of iteration - {i + 1} ***\n")

            results.clear()

            if j == 1:
                size = totalPages // 4
            elif j == 2:
                size = totalPages * 0.75 // 4
            elif j == 3:
                size = totalPages * 0.5 // 4
            elif j == 4:
                size = totalPages * 0.25 // 4

            python_bookcase = bookshelf.BookCase(4, size, bookshelf.DataStructure.PYTHON_LIST)
            numpy_bookcase = bookshelf.BookCase(4, size, bookshelf.DataStructure.NUMPY_ARRAY)
            linked_list_bookcase = bookshelf.BookCase(4, size, bookshelf.DataStructure.DOUBLY_LINKED_LIST)

            time_taken = timeit.timeit(lambda: [python_bookcase.add(bookshelf.Book(shuffled_data.iloc[item]['title'], shuffled_data.iloc[item]['num_pages'], shuffled_data.iloc[item]['isbn13']))\
                                    for item in range(shuffled_data.shape[0])], number=1)
            results.append(time_taken)

            time_taken = timeit.timeit(lambda: [numpy_bookcase.add(bookshelf.Book(shuffled_data.iloc[item]['title'], shuffled_data.iloc[item]['num_pages'], shuffled_data.iloc[item]['isbn13']))\
                                    for item in range(shuffled_data.shape[0])], number=1)
            results.append(time_taken)
           
            time_taken = timeit.timeit(lambda: [linked_list_bookcase.add(bookshelf.Book(shuffled_data.iloc[item]['title'], shuffled_data.iloc[item]['num_pages'], shuffled_data.iloc[item]['isbn13']))\
                                    for item in range(shuffled_data.shape[0])], number=1)
            results.append(time_taken)

            time_taken = timeit.timeit(lambda: [python_bookcase.search(bookshelf.Book(search_data.iloc[item]['title'], search_data.iloc[item]['num_pages'], search_data.iloc[item]['isbn13']))\
                                    for item in range(search_data.shape[0])], number=1)
            results.append(time_taken)
            
            time_taken = timeit.timeit(lambda: [numpy_bookcase.search(bookshelf.Book(search_data.iloc[item]['title'], search_data.iloc[item]['num_pages'], search_data.iloc[item]['isbn13']))\
                                    for item in range(search_data.shape[0])], number=1)
            results.append(time_taken)
                     
            time_taken = timeit.timeit(lambda: [linked_list_bookcase.search(bookshelf.Book(search_data.iloc[item]['title'], search_data.iloc[item]['num_pages'], search_data.iloc[item]['isbn13']))\
                                    for item in range(search_data.shape[0])], number=1)
            results.append(time_taken)			

            time_taken = timeit.timeit(lambda: [python_bookcase.remove(bookshelf.Book(delete_data.iloc[item]['title'], delete_data.iloc[item]['num_pages'], delete_data.iloc[item]['isbn13']))\
                                    for item in range(delete_data.shape[0])], number=1)
            results.append(time_taken)			

            time_taken = timeit.timeit(lambda: [numpy_bookcase.remove(bookshelf.Book(delete_data.iloc[item]['title'], delete_data.iloc[item]['num_pages'], delete_data.iloc[item]['isbn13']))\
                                    for item in range(delete_data.shape[0])], number=1)
            results.append(time_taken)			

            time_taken = timeit.timeit(lambda: [linked_list_bookcase.remove(bookshelf.Book(delete_data.iloc[item]['title'], delete_data.iloc[item]['num_pages'], delete_data.iloc[item]['isbn13']))\
                                    for item in range(delete_data.shape[0])], number=1)
            results.append(time_taken)			

            if j == 1:
                dfFull = dfFull.append(pd.DataFrame([results], columns=columns), ignore_index=True)
                dfFull.to_csv('results/FullSize.csv')
            if j == 2:
                dfThreeQuater = dfThreeQuater.append(pd.DataFrame([results], columns=columns), ignore_index=True)
                dfThreeQuater.to_csv('results/ThreeQuarterSize.csv')
            if j == 3:
                dfHalf = dfHalf.append(pd.DataFrame([results], columns=columns), ignore_index=True)
                dfHalf.to_csv('results/HalfSize.csv')
            if j == 4:
                dfQuarter = dfQuarter.append(pd.DataFrame([results], columns=columns), ignore_index=True)
                dfQuarter.to_csv('results/QuarterSize.csv')

    dfFull.to_csv('results/FullSize.csv')
    dfThreeQuater.to_csv('results/ThreeQuarterSize.csv')
    dfHalf.to_csv('results/HalfSize.csv')
    dfQuarter.to_csv('results/QuarterSize.csv')

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    run_tests(25)
    
