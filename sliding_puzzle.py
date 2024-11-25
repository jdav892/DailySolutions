class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        adj = {
            0 : [1, 3],
            1 : [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        board = "".join([str(val) for row in board for val in row])
        que = deque([(board.index("0"), board, 0)])
        visit = set([board])
        
        while que:
            i, board, length = que.popleft()
            
            if board == "123450":
                return length
            
            board_arr = list(board)
            for j in adj[i]:
                new_board_arr = board_arr.copy()
                new_board_arr[i], new_board_arr[j] = board_arr[j], board_arr[i]
                new_board = "".join(new_board_arr)
                if new_board not in visit:
                    que.append((j, new_board, length + 1))
                    visit.add(new_board)
                    
        return -1
        