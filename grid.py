
#self class represents the current world
import copy
from enum import Enum
class ShipTypes(Enum):
    CARRIER = 5
    BATTLESHIP = 4
    SUBMARINE = 3
    CRUISER = 3
    DESTROYER = 2
class Ship:
    ship_left = 0
    ship_right = 0
    ship_up = 0
    ship_down = 0
    def __init__(self, r, c):
        """Creates a default ship of length 1
        Args:
            r, c - row and column
        Return:
            ship
        """
        self.ship_left = r
        self.ship_right = r
        self.ship_up = c
        self.ship_down = c
        self.ship_type = ShipTypes.DESTROYER
    def __init__(self, ship_type, ship_left, ship_right, ship_up, ship_down):
        """Creates a default ship of length 1
        Args:
            r, c - row and column
        Return:
            ship
        """
        self.ship_type = ship_type
        self.ship_left = ship_left
        self.ship_right = ship_right
        self.ship_up = ship_up
        self.ship_down = ship_down

class Grid:

    row_max = 10
    col_max = 10
    hit_grid = None
    ship_grid = None
    def __init__(self):
        """Creates a default 10x10 matrix grid
        Args:
            None
        Return:
            None, but the internal state of the grid class is changed.
        """
        self.row_max = 10
        self.col_max = 10
        self.hit_grid = [[0 for x in range(self.col_max)] for y in range(self.row_max)]
        self.ship_grid = [[0 for x in range(self.col_max)] for y in range(self.row_max)]

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

    def is_within_grid_range(self, r, c):
        """Checks if a given row and column are within the grid's range
        Args:
            row, column
        Return:
            True or false
        """
        if r >= 0 and r < self.row_max and c >=0 and c < self.col_max:
            return True
        return False
    def place_ship(self, ship):
        """Places the ship on the grid
        Args:
            Ship
        Return:
            True if the ship has successfully been placed
        """
        print(ship)
        if ship.ship_left == ship.ship_right:
            col = ship.ship_left
            for r in xrange(ship.ship_up, ship.ship_down, 1):
                self.hit_grid[r][col] = 1
                self.ship_grid[r][col] = ship.ship_type
        else:
            row = ship.ship_up
            for c in xrange(ship.ship_left, ship.ship_right, 1):
                self.hit_grid[row][c] = 1
                self.ship_grid[row][c] = ship.ship_type
        return True

    def avaliable_to_place(self, ship_left, ship_right, ship_up, ship_down):
        """Checks if you can place the ship on the grid
        Args:
            Ship coordinates 
        Return:
            True if the ship can be places
        """
        print()
        if ship_left == ship_right:
            col = ship_left
            for r in xrange(ship_up, ship_down, 1):
                if self.hit_grid[r][col] == 1:
                    return False
        else:
            row = ship_up
            for c in xrange(ship_left, ship_right, 1):
                if self.hit_grid[row][c] == 1:
                    return False
        return True  

    def is_within_grid_range(self, left_r, right_r, up_c ,down_c):
        """Checks if a given row and column are within the grid's range
        Args:
            left_row right_row left_column, right_column
        Return:
            True or false
        """
        if left_r >= 0 and left_r < self.row_max and up_c >=0 and up_c < self.col_max and \
            right_r >= 0 and right_r < self.row_max and down_c >=0 and down_c < self.col_max:
            return True
        return False

    def print_hit_grid(self):
        """Prints the places that have been hit, which are marked by one
        Args:
            None
        """
        for row in xrange(0, self.row_max, 1):
            row_line = ""
            for col in xrange(0, self.col_max, 1):
                row_line += str(self.hit_grid[row][col]) + " "
            print(row_line)
