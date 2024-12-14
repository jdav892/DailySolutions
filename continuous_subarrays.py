class MaxQueue:
    def __init__(self):
       self.queue = collections.deque()
       self.max_queue = collections.deque()

    def enqueue(self, x):
        while len(self.max_queue) > 0 and self.max_queue[-1] < x:
            self.max_queue.pop()
        self.max_queue.append(x)
        self.queue.append(x)

    def dequeue(self):
        v = self.queue[0]

        self.queue.popleft()

        if self.max_queue[0] == v:
            self.max_queue.popleft()

    def get_max(self):
        return self.max_queue[0]
    
class MinQueue:
    def __init__(self):
        self.queue = collections.deque()
        self.min_queue = collections.deque()

    def enqueue(self, x):
        while len(self.min_queue) > 0 and self.min_queue[-1] > x:
            self.min_queue.pop()
        self.min_queue.append(x)
        self.queue.append(x)

    def dequeue(self):
        v = self.queue[0]

        self.queue.popleft()
        
        if self.min_queue[0] == v:
            self.min_queue.popleft()

    def get_min(self):
        return self.min_queue[0]


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        INF = 10 ** 20
        N = len(nums)
        count = 0

        greater = MaxQueue()
        smaller = MinQueue()

        for i, num in enumerate(nums):
            greater.enqueue(num)
            smaller.enqueue(num)

            while len(greater.queue) > 0 and greater.get_max() > num + 2:
                greater.dequeue()
            while len(smaller.queue) > 0 and smaller.get_min() < num - 2:
                smaller.dequeue()

            count += min(len(greater.queue), len(smaller.queue))

        return count