class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def count_swaps(nums) -> int:
            swaps = 0
            sorted_nums = sorted(nums)
            index_map = {n:i for i, n in enumerate(nums)}
            
            for i in range(len(nums)):
                if nums[i] != sorted_nums[i]:
                    swaps += 1
                    
                    j = index_map[sorted_nums[i]]
                    nums[i], nums[j] = nums[j], nums[i]

                    index_map[nums[j]] = j
            return swaps
        
        que = deque([root])
        
        result = 0
        
        while que:
            level = []
            size = len(que)
            
            for _ in range(size):
                node = que.popleft()
                level.append(node.val)
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
            result += count_swaps(level)
        return result