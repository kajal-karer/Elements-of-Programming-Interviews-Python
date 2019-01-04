from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    scale_factor = 2
    def __init__(self, capacity):
        self.circular_queue = [None]*capacity
        self.rear, self.front, self.num_ele_in_queue = 0, 0, 0

    def enqueue(self, x):
        if (self.rear + 1) % len(self.circular_queue) == self.front:
            self.circular_queue = (self.circular_queue[self.front:]+self.circular_queue[:self.front])
            self.front, self.rear = 0, self.num_ele_in_queue
            self.circular_queue += [None]*(len(self.circular_queue)*Queue.scale_factor-len(self.circular_queue))
        self.circular_queue[self.rear] = x
        self.rear = (self.rear + 1) % len(self.circular_queue)
        self.num_ele_in_queue+=1

    def dequeue(self):
        if not self.num_ele_in_queue:
            raise IndexError('empty queue')
        self.num_ele_in_queue-=1
        ret = self.circular_queue[self.front]
        self.front = (self.front + 1) % len(self.circular_queue)
        return ret

    def size(self):
        return self.num_ele_in_queue


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
