class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {}
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue

                b = (r//3)*3 + c //3

                row_key = f"row {r}"
                col_key = f"col {c}"
                box_key = f"box {b}"

                if not row_key in seen.keys():
                    seen[row_key] = []
                
                if not col_key in seen.keys():
                    seen[col_key] = []
                
                if not box_key in seen.keys():
                    seen[box_key] = []
                
                if num in seen[row_key] or num in seen[col_key] or num in seen[box_key]:
                    return False

                seen[row_key].append(num)
                seen[col_key].append(num)
                seen[box_key].append(num)
        
        return True