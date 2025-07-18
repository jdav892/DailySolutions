class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        N3 = N // 3

        left = []
        right = []

        for i in range(N3):
            left.append(-nums[i])
            right.append(nums[-1 - i])

        heapq.heapify(left)
        heapq.heapify(right)

        leftsum = -sum(left)
        rightsum = sum(right)

        q = collections.deque(nums[N3:N3 * 2])
        best = leftsum - rightsum

        prefix = [leftsum]

        for i in range(N3):
            current = nums[N3 + i]
            leftc = -left[0]

            if current < leftc:
                leftsum = leftsum - leftc + current
                heapq.heappush(left, -current)
                heapq.heappop(left)
            prefix.append(leftsum)

        suffix = [rightsum]
        for i in range(N3):
            current = nums[N3 + N3 - i - 1]
            rightc = right[0]
            
            if current > rightc:
                rightsum = rightsum - rightc + current
                heapq.heappush(right, current)
                heapq.heappop(right)
            suffix.append(rightsum)
        suffix.reverse()

        for x, y in zip(prefix, suffix):
            best = min(best, x - y)
        return best