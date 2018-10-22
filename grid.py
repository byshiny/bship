
#self class represents the current world
import copy
class Grid:
    
    row_max = 10
    col_max = 10
    grid = None
    def __init__(self):
        """Creates a default 10x10 matrix grid
        Args:
            None
        Return:
            None, but the internal state of the grid class is changed.
        """
        self.row_max = 10
        self.col_max = 10
        self.grid = [[0 for x in range(self.col_max)] for y in range(self.row_max)] 

    def get_row_max(self):
        """Returns maximum row size of the grid
        Args:
            None
        Return:
            Maximum row size of the grid.
        """
        return self.col_max;

    def get_col_max(self):
        """Returns maximum column size of the grid
        Args:
            None
        Return:
            Maximum column size of the grid.
        """
        return self.row_max;

    def print_grid(self):
        for row in xrange(0, self.row_max, 1):
            row_line = ""
            for col in xrange(0, self.col_max, 1):
                row_line += str(self.grid[row][col]) + " "
            print(row_line)
