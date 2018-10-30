from grid import Grid
from grid import ShipTypes
from grid import Ship
from random import randint
import sys
def main():

    #print welcome message

    #decide between 1 player or 2 player

    #if 2 player: instruct players to modify the text files while they are not looking

    grid = Grid()
    grid.print_hit_grid()
    max_cols = grid.get_col_max()
    max_rows = grid.get_row_max()
    r = randint(0, max_cols)
    c = randint(0, max_rows)
    direction = randint(0, 4)
    ship_left = r
    ship_right = r
    ship_up = c
    ship_down = c

    ship_list = [ShipTypes.CARRIER]
    if direction == 0:
        ship_left = r - ship_list[0].value
    elif direction == 1:
        ship_right = r + ship_list[0].value
    elif direction == 2:
        ship_up = c - ship_list[0].value
    else:
        ship_down = c + ship_list[0].value
    print(ship_left)
    print(ship_right)
    print(ship_up)
    print(ship_down)
    withinRange = grid.is_within_grid_range(ship_left, ship_right, ship_up, ship_down)
    ship = Ship(ship_list[0], ship_left, ship_right, ship_up, ship_down)
    print(withinRange)
    if(withinRange):
        grid.place_ship(ship)
    grid.print_hit_grid()
if __name__ == '__main__':
    main()
