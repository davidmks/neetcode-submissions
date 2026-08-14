class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. solution (sets)
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit == ".":
                    continue
                box = (r // 3, c // 3)
                if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                    return False
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)
        return True

        # ---

        # # 2. solution (same but with bitmas - efficient storage)
        # rows = [0] * 9
        # cols = [0] * 9
        # boxes = [0] * 9

        # for r in range(9):
        #     for c in range(9):
        #         digit = board[r][c]
        #         if digit == ".":
        #             continue
        #         bit = 1 << (int(digit) - 1)
        #         box = (r // 3) * 3 + (c // 3)
        #         if bit & rows[r] or bit & cols[c] or bit & boxes[box]:
        #             return False
        #         rows[r] |= bit
        #         cols[c] |= bit
        #         boxes[box] |= bit
        # return True
