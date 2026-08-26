class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # rows
        for i in range(9) :
            s = set()
            for j in range(9) :
                if board[i][j] != '.' and board[i][j] in s :
                    # print("row", i, j, board[i][j])
                    return False
                s.add(board[i][j])

        # columns
        for i in range(9) :
            s = set()
            for j in range(9) :
                if board[j][i] != '.' and board[j][i] in s :
                    # print("col", i, j, board[j][i])
                    return False
                s.add(board[j][i])

        # 3x3 boxes
        for i in range(3) :
            for j in range(3) :
                s = set()
                for k in range(3) :
                    for l in range(3) :
                        if board[i * 3 + k][j * 3 + l] != '.' and board[i * 3 + k][j * 3 + l] in s :
                            # print("box", i * 3 + k, j * 3 + l, board[i * 3 + k][j * 3 + l])
                            return False
                        s.add(board[i * 3 + k][j * 3 + l])
        return True
                    
            
