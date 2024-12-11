class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        
        for i in range(numRows - 1):
            new_arr = [0] + result[-1] + [0]
            row = []
            for j in range((len(result[-1])) + 1):
                row.append(new_arr[j] + new_arr[j + 1])
            result.append(row)
        return result