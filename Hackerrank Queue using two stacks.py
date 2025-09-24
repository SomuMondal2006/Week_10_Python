# Hackerrank: Queue using two stacks
# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem



import io
import sys

sample_input = """
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2
"""

sys.stdin = io.StringIO(sample_input.strip())


class MyQueue:
    """
    A queue implementation using two stacks.
    stack_enqueue: for handling enqueue operations.
    stack_dequeue: for handling dequeue and peek operations.
    """
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def _transfer_if_needed(self):
        """
        If the dequeue stack is empty, transfer all elements from the
        enqueue stack to the dequeue stack. This reverses the order,
        placing the oldest element at the top of the dequeue stack.
        """
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

    def enqueue(self, value):
        """
        Adds an element to the rear of the queue.
        This is always done by pushing to the enqueue stack.
        """
        self.stack_enqueue.append(value)

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.
        """
        self._transfer_if_needed()
        return self.stack_dequeue.pop()

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.
        """
        self._transfer_if_needed()
        return self.stack_dequeue[-1]

if __name__ == '__main__':
    queue = MyQueue()

    num_queries = int(input())

    for _ in range(num_queries):
        query_parts = list(map(int, input().split()))
        query_type = query_parts[0]
        
        if query_type == 1:
            value_to_enqueue = query_parts[1]
            queue.enqueue(value_to_enqueue)
        elif query_type == 2:
            queue.dequeue()
        elif query_type == 3:
            front_element = queue.peek()
            print(front_element)