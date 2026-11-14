class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            if not isValid(board[r]):
                return False
        print("Rows valid")

        for c in range(9):
            col = [board[r][c] for r in range(9)]
            if not isValid(col):
                return False
        print("Cols valid")

        for r in range(3):
            for c in range(3):
                area = [board[i][j] for i in range(r*3, r*3+3) for j in range(c*3, c*3+3)] 
                if not isValid(area):
                    return False
        return True
        

def isValid(area: list(str)) -> bool:
    found = [False]*9
    for n in area:
        if n == '.':
            continue
        if found[int(n)-1]:
            return False
        found[int(n)-1] = True
    return True