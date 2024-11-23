class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        X, Y = len(box), len(box[0])
        
        res = [["."] * X for _ in range(Y)]
        
        for r in range(X):
            i = Y - 1
            for c in reversed(range(Y)):
                if box[r][c] == "#":
                    res[i][X - r - 1] = "#" 
                    i -= 1
                elif box[r][c] == "*":
                    res[c][X - r - 1] = "*"
                    i = c - 1
                    
        return res
                
                