

class Board():
    def __init__(self, height, width, cell_size, bo: list):
        self.height = height
        self.width = width
        self.cell_size = cell_size
        self.board = bo

    def print_board_gui(self):
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(col*self.cell_size, row*self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(window, color, rect)

    def print_board(self):
        for row in range(len(self.board)):
            if row % 3 == 0 and row != 0:
                print("- - - - - - - - - - - -")

            for col in range(len(self.board[0])):
                if col % 3 == 0 and col != 0:
                    print(" | ", end="")

                if col == 8:
                    print(self.board[row][col])
                else:
                    print(str(self.board[row][col]) + " ", end="")

    def _find_empty_cell(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    return (row, col)

        return None

    def _check_valid_input(self, num, pos):
        # Check row
        for col in range(len(self.board[0])):
            # pos[1] != 0 to check if it isn't the cell we just inserted
            if self.board[pos[0]][col] == num and pos[1] != col:
                return False

        # Check column
        for row in range(len(self.board)):
            if self.board[row][pos[1]] == num and pos[0] != row:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for row in range(box_y * 3, box_y*3 + 3):
            for col in range(box_x * 3, box_x*3 + 3):
                if self.board[row][col] == num and (row, col) != pos:
                    return False

        return True

    def solve(self):
        print("solving")
        print("-")
        empty_cell = self._find_empty_cell()
        if empty_cell:
            row, col = empty_cell
        else:
            return True

        for num in range(1, 10):  # Generate random number between 1 & 9
            if self._check_valid_input(num, (row, col)):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False