fmax = lambda x, y: x if x > y else y

class SegmentTree:
    def __init__(self, arr):
        self.INF = 10 ** 18
        self.N = len(arr)
        self.arr = arr
        self.tree = [self.INF] * (4 * self.N)
        self.build(1, 0, self.N - 1)
    
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return
        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1
        self.build(left_child, start, mid)
        self.build(right_child, mid + 1, end)
        self.tree[node] = fmax(self.tree[left_child], self.tree[right_child])

    def update(self, node, start, end, idx, value):
        if start == end:
            self.arr[start] = value
            self.tree[node] = value
            return
        
        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1
        if start <= idx <= mid:
            self.update(left_child, start, mid, idx, value)
        else:
            self.update(right_child, mid + 1, end, idx, value)
        self.tree[node] = fmax(self.tree[left_child], self.tree[right_child])

    def _query(self, node, start, end, x):
        left_child = 2 * node
        right_child = 2 * node + 1
        
        if x > self.tree[node]:
            return -1
        
        if start == end:
            return start
        

        left_child = 2 * node
        right_child = 2 * node + 1

        mid = (start + end) // 2
        if self.tree[left_child] >= x:
            return self._query(left_child, start, mid, x)
        else:
            return self._query(right_child, mid + 1, end, x)

    def query(self, x):
        return self._query(1, 0, self.N - 1, x)
        
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        N = len(fruits)
        st = SegmentTree(baskets)

        count = 0
        for f in fruits:
            index = st.query(f)
            if index == -1:
                count += 1
                continue
            st.update(1, 0, N - 1, index, 0)
        return count