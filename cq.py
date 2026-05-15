"""cq.py

# Circular Queue

This module defines the CircularQueue data type
"""
############################### 72 chars ###############################


class CircularQueue:
    """Circular Queue implemented as Array.

    Methods
        - enqueue(item)
          Adds item at the end of the queue.

        - dequeue()
          Returns the first item in the queue.
    """

    def __init__(self, size: int):
        self.size = size
        self._data = [None] * size
        self._head = -1
        self._tail = -1
        

    def __repr__(self) -> str:
        return f"CircularQueue({self.size})"
        
    def isEmpty(self):
        """Checks if the queue is empty"""
        return self._head == -1
    
    def isFull(self):
        """Checks if the queue is full"""
        return (self._tail + 1) % self.size == self._head

    
    def enqueue(self, item: tuple[int, int]) -> None:
        """Add item at the end of the queue.

        Arguments
            - item
              The item to be added.

        Return
            None
        """
        if self.isFull():
            print("Queue is full!")
        elif self.isEmpty():
            self._head = 0
            self._tail = 0
            self._data[self._tail] = item
            
        

    def dequeue(self) -> tuple[int, int]:
        """Return the item at the head of the queue.

        Arguments
            None

        Return
            item
        """
        # Delete the line below and write your code here
        raise NotImplementedError("dequeue not implemented")


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python cq.py`
    pass
