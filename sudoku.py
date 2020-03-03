from itertools import chain


class SudokuSolver:
    def __init__(self, fn: str):
        self.grid = self.load_puzzle(fn)
        # Square positions in form ((x1, x2), (y1, y2)) to show where squares start and end on each axis
        self.sq_pos = [
            (((0, 2), (0, 2)), ((3, 5), (0, 2)), ((6, 8), (0, 2))),
            (((0, 2), (3, 5)), ((3, 5), (3, 5)), ((6, 8), (3, 5))),
            (((0, 2), (6, 8)), ((3, 5), (6, 8)), ((6, 8), (6, 8))),
        ]
        self.completed_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __str__(self):
        return "\n".join([
            " ".join([f"{str(letter)} |" if (l_pos + 1) % 3 == 0 and l_pos + 1 < 9 else str(letter)for l_pos, letter in enumerate(row)])
            + ("\n" + "- " * 3 + "+ " + "- " * 3 + "+ " + "- " * 3 if (r_pos + 1) % 3 == 0 and r_pos + 1 < 9 else "")
            for r_pos, row in enumerate(self.grid)
        ])

    @staticmethod
    def load_puzzle(file_name: str) -> list:
        """
        Loads the sudoku puzzle from txt file
        :param file_name: Name of the txt file to load from
        :return: 2D list of the puzzle
        """
        with open(file_name) as f:
            return [list(map(lambda x: int(x), list(line.replace("\n", "")))) for line in f.readlines()]

    def check_row(self, row_y: int, num: int=None) -> bool:
        """
        Checks if the row has the numbers up to 9
        :param row_y: Y coord of row
        :param num: Decides whether number is being checked or entire row
        :return: True if has numbers else false
        """
        return sorted(self.grid[row_y]) == self.completed_numbers if num is None else num in self.grid[row_y]

    def check_col(self, row_x: int, num: int=None) -> bool:
        """
        Checks if the column has the numbers up to 9
        :param row_x: X coord of column
        :param num: Decides whether number is being checked or entire column
        :return: True if has numbers else false
        """
        col = [self.grid[i][row_x] for i in range(9)]
        return sorted(col) == self.completed_numbers if num is None else num in col

    def check_square(self, num_pos: tuple) -> bool:
        """
        Checks if the square has the numbers up to 9
        :param num_pos: The (y, x) coords of pos in the square
        :return: True if has numbers else false
        """
        sq_x, sq_y = self.sq_pos[num_pos[0] // 3][num_pos[1] // 3]
        return sorted(chain.from_iterable(
            [row[sq_x[0]:sq_x[1] + 1] for p, row in enumerate(self.grid) if sq_y[0] <= p <= sq_y[1]]
        )) == self.completed_numbers

    def solve(self):
        x, y = 0, 0
        while True:
            pass


if __name__ == '__main__':
    s = SudokuSolver("sudoku_puzzle.txt")
    print(s.check_row(0, 3))
