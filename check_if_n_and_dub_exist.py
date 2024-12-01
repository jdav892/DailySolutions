class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        val_dict = collections.defaultdict(int)
        
        for num in arr:
            val_dict[num] += 1
            
        for num in arr:
            if num != 0 and 2 * num in val_dict:
                return True
            if num == 0 and val_dict[num] > 1:
                return True
            
        return False