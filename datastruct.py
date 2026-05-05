"""datastruct.py

# Data Structures

This module defines the LinkedList abstract data type
"""
############################### 72 chars ###############################


class Node:
    """Represents a node in a linkedlist.

    Arguments
        - data
          The data encapsulated in the node.

    Attributes
        - next: Node | None
          The next node in the linkedlist, or None if the node is the tail.

    Methods
        - get() -> data
          Return the data stored in the node.
    """

    def __init__(self, data: tuple[int, int]):
        # Replace the line below with your code
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self) -> tuple[int, int]:
        """Return the data stored in the node.

        Arguments
            None

        Return
            tuple[int, int]
        """
        # Replace the line below with your code
        return self.data


class LinkedList:
    """Represents a sequence of data items.

    Arguments
        None

    Attributes
        None

    Methods
        - length() -> int
        - get(index) -> item
        - insert(index, item) -> None
        - append(item) -> None
        - delete(index) -> None
    """

    def __init__(self):
        self._head = None
        

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
            None

        Return
            length of linkedlist as an integer (zero or positive)
        """
        # Replace the line below with your code
        count = 0
        current = self._head
        while current != None:
            current = current.next
            count += 1
        return count

    def get(self, n: int) -> tuple[int, int]:
        """Returns item at n-th node.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Returns
            item

        Raises
            IndexError if n >= length
        """
        # Replace the line below with your code
        if n >= self.length():
            raise IndexError
        current = self._head
        count = 0
        while count <= n:
            current = current.next
            count += 1
        return current.get()
        
    def insert(self, n: int, item: tuple[int, int]) -> None:
        """Insert item into linkedlist at position n.

        If n == 0, inserts item at the head.
        If n == length, appends item at the tail of the linkedlist.

        Arguments
            - n: int
              sequence number of item to be inserted.

        Raises
            IndexError if n > length
        """
        # Replace the line below with your code
        if n == 0:
            node = Node(item)
            self._head = node
        elif n == self.length():
            node = Node(item)
            self.append(node)
        else:
            node = Node(item)
            node.next = 


    def append(self, item: tuple[int, int]) -> None:
        """Append item at the end of linkedlist.

        Arguments
            - item
              The item to be appended.

        Returns
            None
        """
        # Replace the line below with your code
        if self._head is None:
            self._head = Node(item)
        else:
            current  = self._head
            while current.next is not None:
                current = current.next
            current.next = Node(item)
        
    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Raises
            IndexError if n > length
        """
        # Replace the line below with your code
        if n > self.length():
            raise IndexError
        elif n == 0:
            self._head = self._head.next
        else:
            current = self._head
            count = 0 
            while count < n:
                if count == n - 1:
                    beforeNode = current
                elif count == n:
                    


                
        
       
    def contains(self, item: tuple[int, int]) -> bool:
        """Checks whether an item is in the linkedlist.
        Returns a boolean value to indicate the status of the search.

        Arguments
            - item
              The item to be searched for.

        Returns
            True if item is found in the linkedlist,
            otherwise False
        """
        # Replace the line below with your code
        return  in LinkedList


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python datastruct.py`

    pass
