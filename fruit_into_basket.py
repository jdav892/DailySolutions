class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_hash = collections.Counter()
        maxi = 0
        left = 0
        
        for right in range(len(fruits)):
            fruit_hash[fruits[right]] += 1
            
            while len(fruit_hash) > 2:
                fruit_hash[fruits[left]] -= 1
                if fruit_hash[fruits[left]] == 0:
                    del fruit_hash[fruits[left]]

                left += 1

            maxi = max(maxi, right - left + 1)
        return maxi
                