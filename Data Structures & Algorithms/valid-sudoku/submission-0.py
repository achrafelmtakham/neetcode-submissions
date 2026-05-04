class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_dict_line   = { line_number:line for line_number,line in enumerate(board) }
        board_dict_column = { column:[ board[row][column] for row in range(len(board)) ] for column in range(len(board)) }
        board_dict_boxe = { boxe:[board[row][column]
            for row in range((boxe//3)*3, (boxe//3)*3+3)
            for column in range((boxe%3)*3, (boxe%3)*3+3)
          ] for boxe in range(9)}

        for line_number, line in board_dict_line.items():
            line_set = set()
            for digit in line:
                if digit == ".":
                    continue 
                if digit in line_set:
                    return False
                else:
                    line_set.add(digit)
        
        for column_number, column in board_dict_column.items():
            column_set = set()
            for digit in column:
                if digit == ".":
                    continue 
                if digit in column_set:
                    return False
                else:
                    column_set.add(digit)
        
        for boxe_number, boxe in board_dict_boxe.items():
            boxe_set = set()
            for digit in boxe:
                if digit == ".":
                    continue 
                if digit in boxe_set:
                    return False
                else:
                    boxe_set.add(digit)
        
        return True