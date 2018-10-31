from grid import Grid
from grid import ShipTypes
from grid import Ship
from random import randint
import sys
def main():

    #print welcome message

    #decide between 1 player or 2 player

    #if 2 player: instruct players to modify the text files while they are not looking - to be implemented
    turns = 0
    grid = Grid()  
    ship_list = [ShipTypes.CARRIER, ShipTypes.BATTLESHIP, ShipTypes.CRUISER, ShipTypes.DESTROYER, ShipTypes.SUBMARINE]
    generate_ships_on_a_grid(grid, ship_list)
    print("Welcome to battleship! Your grid size is" + "r: " + str(grid.row_max) + "," +  "c:" + str(grid.col_max) )
    print("Comrade you need to sink 5 ships of 5, 4, 3, 3, 2. The game begins NOW!")
    grid.print_hit_grid()
    grid.print_player_grid()
    while(grid.total_hits_left > 0):
        try:
            r,c = input('Coordinates please (with a comma in between, -1, -1 to quit =( ): ')
            if r == -1 and c == -1:
                grid.total_hits_left = -9000
                print("Turns taken: " + str(turns))
                #print("Ships sunk: " + )
            else:
                grid.is_point_within_grid_range(r,c)
                grid.evaluate_hit(r,c)
                turns +=1
        except:
            print("You probably made an input error. Try again")
    print("Congratulations! You destroyed all the ships! You took " + str(turns) + " Turns.")

def generate_ships_on_a_grid(grid, ship_list):
    """Generates ships on a grid by updating the hit grid 
        Args:
            TBD
        Return:
            None
        """
    max_cols = grid.get_col_max()
    max_rows = grid.get_row_max()
   
    ship_id = 0
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
        withinRange = grid.is_four_coords_within_grid_range(ship_left, ship_right, ship_up, ship_down)
        if withinRange:
            avaliable = grid.avaliable_to_place(ship_left, ship_right, ship_up, ship_down)
            if avaliable:
                ship = Ship(ship_list[0], ship_left, ship_right, ship_up, ship_down, ship_id)
                grid.place_ship(ship)
                ship_id +=1
                del ship_list[0]


if __name__ == '__main__':
    main()
