class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == '.':
                    continue

                b = (r // 3)*3 + c // 3

                key_row = f"row {r} {value}"
                key_col = f"col {c} {value}"
                key_box = f"box {b} {value}"

                if (key_row in seen or 
                    key_col in seen or 
                    key_box in seen):
                    return False
                seen.add(key_row)
                seen.add(key_col)
                seen.add(key_box)
                


        return True
                

