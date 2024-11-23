class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        X, Y = len(box), len(box[0])
        
        for r in range(X):
            i = Y - 1
            for c in reversed(range(Y)):
                if box[r][c] == "#":
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                elif box[r][c] == "*":
                    i = c - 1
                    
        res = []
       
        for c in range(Y):
            col = []
            for r in reversed(range(X)):
                col.append(box[r][c])
            
            res.append(col) 
        return res
                
                