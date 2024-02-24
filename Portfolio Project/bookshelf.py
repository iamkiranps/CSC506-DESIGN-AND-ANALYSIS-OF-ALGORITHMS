"""
  Kiran Ponappan Sreekumari 
  CSC506 – Design and Analysis of Algorithms 
  Colorado State University - Global
  Dr. Dong Nguyen 
  February 23, 2024
  Portfolio Project - Option #1: Analysis of Algorithms and Data Structures
"""
from enum import Enum
from typing import List
import numpy as np
import bisect
import data_structures as ds
import progressbar

class SortScheme(Enum):
    TITLE = 1
    LENGTH = 2
    ISBN = 3


class DataStructure(Enum):
    PYTHON_LIST = 1
    NUMPY_ARRAY = 2
    DOUBLY_LINKED_LIST = 3

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False

        if self.sort_scheme == SortScheme.TITLE:
            return self.title == other.title
        elif self.sort_scheme == SortScheme.LENGTH:
            return self.pages == other.pages
        elif self.sort_scheme == SortScheme.ISBN:
            return self.isbn == other.isbn

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False

        if self.sort_scheme == SortScheme.TITLE:
            return self.title < other.title
        elif self.sort_scheme == SortScheme.LENGTH:
            return self.pages < other.pages
        elif self.sort_scheme == SortScheme.ISBN:
            return self.isbn < other.isbn

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False

        if self.sort_scheme == SortScheme.TITLE:
            return self.title <= other.title
        elif self.sort_scheme == SortScheme.LENGTH:
            return self.pages <= other.pages
        elif self.sort_scheme == SortScheme.ISBN:
            return self.isbn <= other.isbn

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False

        if self.sort_scheme == SortScheme.TITLE:
            return self.title > other.title
        elif self.sort_scheme == SortScheme.LENGTH:
            return self.pages > other.pages
        elif self.sort_scheme == SortScheme.ISBN:
            return self.isbn > other.isbn

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False

        if self.sort_scheme == SortScheme.TITLE:
            return self.title >= other.title
        elif self.sort_scheme == SortScheme.LENGTH:
            return self.pages >= other.pages
        elif self.sort_scheme == SortScheme.ISBN:
            return self.isbn >= other.isbn

class Book:
    def __init__(self, title: str = None, pages: int = 0, isbn: int = None, sort_scheme: SortScheme = SortScheme.TITLE) -> None:
        self.title = title
        self.pages = pages
        self.isbn = isbn
        self.sort_scheme = sort_scheme

class Shelf:
    def __init__(self, size: int = 10000, datastructure: DataStructure = DataStructure.PYTHON_LIST, sort_scheme: SortScheme = SortScheme.TITLE) -> None:
        self.max_size = size
        self.cur_size = 0
        self.datastructure = datastructure
        self.sort_scheme = sort_scheme

        # Determine underlying datastructure
        if self.datastructure == DataStructure.PYTHON_LIST:
            self.book_list = []
        elif self.datastructure == DataStructure.NUMPY_ARRAY:
            self.book_list = np.array([], dtype=Book)
        elif self.datastructure == DataStructure.DOUBLY_LINKED_LIST:
            self.book_list = ds.LinkedList()

    def add_book(self, book: Book) -> list:
        overflow = []

        # Add based on the underlying datastructure
        if self.datastructure == DataStructure.PYTHON_LIST:
            bisect.insort(self.book_list, book)
            self.cur_size += book.pages

            # Remove overflow
            while self.cur_size > self.max_size:
                extra = self.book_list.pop()
                self.cur_size -= extra.pages
                overflow.append(extra)

        elif self.datastructure == DataStructure.NUMPY_ARRAY:
            index = np.searchsorted(self.book_list, book)
            self.book_list = np.insert(self.book_list, index, book)
            self.cur_size += book.pages

            # Remove overflow
            while self.cur_size > self.max_size:
                extra, self.book_list = self.book_list[-1], self.book_list[:-1]
                self.cur_size -= extra.pages
                overflow.append(extra)

        elif self.datastructure == DataStructure.DOUBLY_LINKED_LIST:
            self.book_list.insert_in_order(book)
            self.cur_size += book.pages

            # Remove overflow
            while self.cur_size > self.max_size:
                temp = self.book_list.remove_at_back().value
                self.cur_size -= temp.pages
                overflow.append(temp)

        return overflow
    
    def remove_book(self, book: Book) -> bool:
        if self.datastructure == DataStructure.PYTHON_LIST:
            try:
                self.book_list.remove(book)
                self.cur_size -= book.pages
                return True
            except ValueError:
                return False

        elif self.datastructure == DataStructure.NUMPY_ARRAY:
            results = np.where(self.book_list == book)
            if len(results) != 0:
                self.book_list = np.delete(self.book_list, results)
                self.cur_size -= book.pages
                return True
            return False
        
        elif self.datastructure == DataStructure.DOUBLY_LINKED_LIST:
            removed =  self.book_list.remove(book)
            if removed == True:
                self.cur_size -= book.pages
            return removed
        
        return False
    
    def remove_front(self)->Book:
        if self.is_empty():
            return None
        
        if self.datastructure == DataStructure.PYTHON_LIST:
            book = self.book_list.pop(0)
        elif self.datastructure == DataStructure.NUMPY_ARRAY:
            book = self.book_list[0]
            self.book_list = self.book_list[1:]
        elif self.datastructure == DataStructure.DOUBLY_LINKED_LIST or self.datastructure == DataStructure.DOUBLY_LINKED_LIST_AVL:
            book = self.book_list.remove_at_front().value

        self.cur_size -= book.pages
        return book
    
    def find_books(self, name: str = None, pages: int = None, isbn: int = None) -> list:
        matches = []

        if name is None and pages is None and isbn is None:
            return matches
    
        # Perform search based on the underlying datastructure
        if self.datastructure == DataStructure.PYTHON_LIST:
            for book in progressbar.progressbar(self.book_list):
                if (name is None or name == book.name) and (pages is None or pages == book.pages) and (isbn is None or isbn == book.isbn):
                    matches.append(book)

        elif self.datastructure == DataStructure.NUMPY_ARRAY:
            for book in progressbar.progressbar(self.book_list):
                if (name is None or name == book.name) and (pages is None or pages == book.pages) and (isbn is None or isbn == book.isbn):
                    matches.append(book)

        elif self.datastructure == DataStructure.DOUBLY_LINKED_LIST:
            cur_node = self.book_list.head      
            bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
            while cur_node is not None:
                if (name is None or name == cur_node.value.name) and (pages is None or pages == cur_node.value.pages) and (isbn is None or isbn == cur_node.value.isbn):
                    matches.append(cur_node.value)
                bar.update()
    
        return matches

    def search(self, book: Book) -> bool:
        if self.datastructure == DataStructure.PYTHON_LIST:
            return True if book in self.book_list else False
        elif self.datastructure == DataStructure.NUMPY_ARRAY:
            return True if len(np.where(self.book_list == book)) != 0 else False
        elif self.datastructure == DataStructure.DOUBLY_LINKED_LIST:
            return self.book_list.search(book)

    def is_empty(self) -> bool:
        if self.datastructure == DataStructure.PYTHON_LIST:
            return True if len(self.book_list) == 0 else False
        elif self.datastructure == DataStructure.NUMPY_ARRAY:
            return True if len(self.book_list) == 0 else False
        elif self.datastructure == DataStructure.DOUBLY_LINKED_LIST:
            return self.book_list.is_empty()

    def peek(self):
        if self.is_empty():
            return None

        if self.datastructure == DataStructure.PYTHON_LIST:
            return self.book_list[0]
        elif self.datastructure == DataStructure.NUMPY_ARRAY:
            return self.book_list[0]
        elif self.datastructure == DataStructure.DOUBLY_LINKED_LIST:
            return self.book_list.head.value

from typing import List
from copy import deepcopy

class BookCase:
    """A collection of shelves to store books."""

    def __init__(self, num_shelves: int = 4, shelf_size: int = 10000, datastructure: DataStructure = DataStructure.PYTHON_LIST):
        if num_shelves is None or num_shelves == 0:
            print(f"Error - Unable to create a bookcase with no shelves")
            quit()

        self.shelves: List[Shelf] = []
        for _ in range(num_shelves):
            self.shelves.append(Shelf(shelf_size, datastructure))

        print(f"Initialized BookCase - {num_shelves} shelves with capacity for {shelf_size} pages each")
     
    def add(self, new_book: Book) -> List[Book]:
        """Adds a book to the bookcase in proper order. Returns a list of books that were removed due to overflow."""

        overflow = self.shelves[0].add_book(new_book)
        temp_overflow = []

        for i in range(1, len(self.shelves)):
            if not overflow:
                return []

            for book in overflow:
                temp = self.shelves[i].add_book(book)
                temp_overflow.extend(temp)
            
            overflow.clear()
            overflow = deepcopy(temp_overflow)
            temp_overflow.clear()

        return overflow
  
    def remove(self, book: Book) -> bool:
        """Removes a book from the bookcase and shifts remaining books to remove empty space."""
        removed = False

        for i in range(len(self.shelves)):
            removed = self.shelves[i].remove_book(book)

            if removed:
                if i < len(self.shelves) - 1:
                    for j in range(i, len(self.shelves) - 1):
                        next_book = self.shelves[j + 1].peek()

                        while next_book:
                            if (self.shelves[j].cur_size + next_book.pages) <= self.shelves[j].max_size:
                                self.shelves[j].add_book(self.shelves[j + 1].remove_front())
                                self.shelves[j].cur_size += next_book.pages
                                self.shelves[j + 1].cur_size -= next_book.pages
                                next_book = self.shelves[j + 1].peek()
                            else:
                                break
                break

        return removed
  
    def find_books(self, name: str = None, pages: int = None, isbn: int = None) -> List[List[Book]]:
        """Searches the book case for all books matching the given criteria."""
        found = []

        for i in range(len(self.shelves)):
            found.append(self.shelves[i].find_books(name, pages, isbn))

        return found

    def search(self, book: Book) -> bool:
        """Searches the bookcase for a specific book and returns true if found."""
        for i in range(len(self.shelves)):
            if self.shelves[i].search(book):
                return True

        return False
