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
    
    ship_list = [ShipTypes.CARRIER, ShipTypes.BATTLESHIP, ShipTypes.CRUISER, ShipTypes.DESTROYER, ShipTypes.SUBMARINE]
    generate_ships_on_a_grid(grid, ship_list)
    grid.print_hit_grid()

def generate_ships_on_a_grid(grid, ship_list):
    """Generates ships on a grid by updating the hit grid 
        Args:
            TBD
        Return:
            None
        """
    max_cols = grid.get_col_max()
    max_rows = grid.get_row_max()
   
    
    while(len(ship_list) > 0):
        r = randint(0, max_cols)
        c = randint(0, max_rows)
        direction = randint(0, 4)
        ship_left = r
        ship_right = r
        ship_up = c
        ship_down = c

        
        if direction == 0:
            ship_left = r - ship_list[0].value
        elif direction == 1:
            ship_right = r + ship_list[0].value
        elif direction == 2:
            ship_up = c - ship_list[0].value
        else:
            ship_down = c + ship_list[0].value
        
        withinRange = False
        withinRange = grid.is_within_grid_range(ship_left, ship_right, ship_up, ship_down)
        
        ship = Ship(ship_list[0], ship_left, ship_right, ship_up, ship_down)
        print(withinRange)
        if withinRange:
            avaliable = grid.avaliable_to_place(ship_left, ship_right, ship_up, ship_down)
            if avaliable:
                grid.place_ship(ship)
                del ship_list[0]


if __name__ == '__main__':
    main()
