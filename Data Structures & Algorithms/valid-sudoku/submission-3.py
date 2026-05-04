class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                d = board[r][c]
                if d == ".":
                    continue
                b = (r // 3) * 3 + (c // 3)
                if (("row", r, d) in seen or
                    ("col", c, d) in seen or
                    ("box", b, d) in seen):
                    return False
                seen.add(("row", r, d))
                seen.add(("col", c, d))
                seen.add(("box", b, d))
        return True