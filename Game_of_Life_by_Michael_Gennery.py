# BBC - TECHNICAL TEST STAGE - SOFTWARE ENGINEERING GRADUATE TRAINEE SCHEME
# Michael Gennery
# mike_gennery@yahoo.co.uk
# Tel: 07505 258570
# February 7th, 2019

# GAME OF LIFE


# FUNCTIONS

# Create Grid (CG)

def create_grid(cg_rows,cg_columns):
    """Create grid with given number of rows and columns as a 2D list"""
    cg_grid = []
    # Add an empty list for the row to the grid
    for cg_num_row in range(0,cg_rows):
        cg_grid.append([])
    # Create a list of values for each row in the grid
        for cg_num_col in range(0,cg_columns):
            cg_grid[cg_num_row].append([])
            cg_grid[cg_num_row][cg_num_col] = False
    return(cg_grid)

# Display Grid (DG)

def display_grid(dg_grid):
    """Display the current grid showing which cells are live and which are dead/inactive"""
    # For each row
    for dg_num_row in range(len(dg_grid)-1,-1,-1):
        # For each column in the row display the status
        dg_text = ''
        for dg_num_column in range(0,len(dg_grid[0])):
            if dg_num_row < 10:
                dg_num_text = '0'
            else:
                dg_num_text = ''
            if dg_grid[dg_num_row][dg_num_column] == True:
                dg_text = dg_text + dg_num_text + str(dg_num_row) + ':' + str(dg_num_column) + '=LIVE '
            else:
                dg_text = dg_text + dg_num_text + str(dg_num_row) + ':' + str(dg_num_column) + '=dead '
        print(dg_text)

# Add Row (AR)

def add_row(ar_grid):
    """Add a row to the end of the grid when the live cells get near to the edge"""
    ar_grid.append([])
    ar_len = len(ar_grid) - 1
    ar_width = len(ar_grid[0])
    # For each column in the grid, add a new entry in the grid in the new row
    for ar_col in range (0,ar_width):
        ar_grid[ar_len].append(False)
    return(ar_grid)

# Add Column (AC)

def add_col(ac_grid):
    """Add a column to the end of every row when the live cells get near the edge"""
    ac_len = len(gol_grid)
    for ac_num_row in range(0,ac_len):
        ac_grid[ac_num_row].append(False)
    return(ac_grid)
    
# Count Neighbours

def count_neighbours(cn_row,cn_col,cn_top,cn_right,cn_grid):
    """Count the number of neighbouring active cells for any given grid reference"""

    cn_neighbours = 0

    # Check if cell is on the edge of the grid
    
    if cn_col == 0:
        cn_edge_left = True
    else:
        cn_edge_left = False

    if cn_row == cn_top:
        cn_edge_top = True
    else:
        cn_edge_top = False

    if cn_col == cn_right:
        cn_edge_right = True
    else:
        cn_edge_right = False
        
    if cn_row == 0:
        cn_edge_bottom = True
    else:
        cn_edge_bottom = False
    
    # Move around the cell in a clockwise direction counting the active
    # cells but not non-existant cells outside the gird

    if cn_edge_top == False:
        if cn_grid[cn_row + 1][cn_col] == True: 
            cn_neighbours = cn_neighbours + 1

    if cn_edge_top == False and cn_edge_right == False:
        if cn_grid[cn_row + 1][cn_col + 1]:
            cn_neighbours = cn_neighbours + 1
                
    if cn_edge_right == False:        
        if cn_grid[cn_row][cn_col + 1] == True:
            cn_neighbours = cn_neighbours + 1

    if cn_edge_bottom == False and cn_edge_right == False:
        if cn_grid[cn_row - 1][cn_col + 1] == True:
            cn_neighbours = cn_neighbours + 1
                
    if cn_edge_bottom == False:
        if cn_grid[cn_row - 1][cn_col] == True:
            cn_neighbours = cn_neighbours + 1
                
    if cn_edge_bottom == False and cn_edge_left == False:
        if cn_grid[cn_row - 1][cn_col - 1] == True:
            cn_neighbours = cn_neighbours + 1
                
    if cn_edge_left == False:
        if cn_grid[cn_row][cn_col - 1] == True:
            cn_neighbours = cn_neighbours + 1
                
    if cn_edge_top == False and cn_edge_left == False:        
        if cn_grid[cn_row + 1][cn_col - 1] == True:
            cn_neighbours = cn_neighbours + 1
                
    return(cn_neighbours)

# Evolve Grid (EG)

def evolve_grid(eg_grid):
    """When the user presses ENTER, the grid will evolve according to the following rules: -

    Scenario 0: 0 neighbouring active cells - cell inactive
    Scenario 1: less than 2 neighbouring active cells - cell inactive
    Scenario 2: more the 3  neighbouring active cells - cell inactive
    Scenario 3: 2 or 3  neighbouring active cells - stay active
    Scenario 4: 3 neighbours - cell actived
    Scenario 5: no active cells - cells stay inactive"""

    eg_len = len(eg_grid)
    eg_width = len(eg_grid[0])
    eg_neighbours = 0
    eg_active_cells = []
    eg_row = 0
    eg_col = 0

    # For Each row in the grid
    for eg_row in range (0,eg_len):

        eg_col = 0
        
        # For each column in each row
        for eg_col in range(0,eg_width):

            # Add a row if at the edge of the grid and the cell is active
            
            if eg_row == eg_len -1 and eg_grid[eg_row][eg_col] == True:
                eg_grid = add_row(eg_grid)
                eg_len = len(eg_grid)
                eg_width = len(eg_grid[0])

            # Add a column if at the edge of the grid and the cell is active
            if eg_col == eg_width -1 and eg_grid[eg_row][eg_col] == True:
                eg_grid = add_col(eg_grid)
                eg_len = len(eg_grid)
                eg_width = len(eg_grid[0])
                        
            # Count the number of neighbouring active cells
            eg_neighbours = count_neighbours(eg_row,eg_col,eg_len-1,eg_width-1,eg_grid)
            
            # Scenario 3: 2 or 3  neighbouring active cells - stay active
            # Scenario 4: 3 neighbours - cell actived

            # If there are three neighbours, add this cell to the list of active cells
            if eg_neighbours == 3:
                eg_active_cells.append([eg_row,eg_col])
                
                # Scenario 0: 0 neighbouring active cells - make cell inactive
                # Scenario 1: less than 2 neighbouring active cells - make cell inactive
                # Scenario 2: more the 3  neighbouring active cells - make cell inactive
                # Scenario 5: no active cells - cells stay inactive
                
            elif eg_neighbours == 2:
                if eg_grid[eg_row][eg_col] == True:
                    # Tag cell to be made active
                    eg_active_cells.append([eg_row,eg_col])

    # Update the grid with the active cells

    # Reset cell status
    eg_grid = create_grid(eg_len,eg_width)
    
    eg_cell_num = len(eg_active_cells)

    # For each active cell, activate the cell on the grid
    for eg_update_num in range(0,eg_cell_num):
        eg_update_row = int(eg_active_cells[eg_update_num][0])
        eg_update_col = int(eg_active_cells[eg_update_num][1])
        eg_grid[eg_update_row][eg_update_col] = True

    return(eg_grid)

######################
#                    #
# GAME OF LIFE (GOL) #
#                    #
######################

# Global Variables

gol_grid = []
gol_no_of_rows = 0
gol_no_of_columns = 0
gol_qty_cells = 0
gol_row = 0
gol_col = 0
gol_enter = True
gol_exit = False

# Main code GOL)

print('BBC - TECHNICAL TEST STAGE - SOFTWARE ENGINEERING GRADUATE TRAINEE SCHEME')
print('\nby Michael Gennery')
print('\nTHE GAME OF LIFE')
print('\n\nWelcome to the Game of Life. In this game, you need to define a grid and activate cells. Cells and the grid they are on evolve depending on the cells around them. Then watch as the cells evolve every time you run the program.')

# Enter the number of rows for the grid
while gol_enter:
    gol_no_of_rows = input('\n\nHow many rows do you want your grid to have? (Recomended Max = 40) ')
    gol_no_of_rows = int(gol_no_of_rows)
    if gol_no_of_rows <= 0:
        print('You must have at least 1 row!')
    else:
        gol_enter = False
        
# Enter the number of columns for the grid
gol_enter = True
while gol_enter:
    gol_no_of_columns = input('\nHow man columns do you want your grid to have? (Recomended Max = 15) ')
    gol_no_of_columns = int(gol_no_of_columns)
    if gol_no_of_columns <= 0:
        print('You must have at least 1 column!')
    else:
        gol_enter = False

# Activate Cells
gol_enter = True
while gol_enter:
    gol_qty_cells = input('\nHow many cells do you wish to activate? ')
    gol_qty_cells = int(gol_qty_cells)
    if gol_no_of_columns < 0:
        print('Invalid Entry!')
    else:
        gol_enter = False

# Create grid with specified number of rows and columns
gol_grid = create_grid(gol_no_of_rows,gol_no_of_columns)

print('\nHere is you starting Grid -\n')
display_grid(gol_grid)

print('\nFor each cell you wish to activate, enter the row and column number.')
print('e.g. to change 3:4=dead to 3:4=LIVE enter 3 for row and 4 for column.')

# Ask user which row and column and then activate the cells
for gol_qty in range(1,gol_qty_cells + 1):
    gol_row = input('\nROW: ')
    gol_col = input('COLUMN: ')
    gol_row = int(gol_row)
    gol_col = int(gol_col)
    if gol_row > gol_no_of_rows - 1 or gol_col > gol_no_of_columns - 1 or gol_row < 0 or gol_col < 0:
        print('That reference is outside the range of your grid!')
    else:
        gol_grid[gol_row][gol_col] = True

print('\nHere is your Grid with your activated cells-\n')

display_grid(gol_grid)

# Iterate the grid
while not gol_exit:
    gol_iterate = input('\nPress ENTER to iterate or q and ENTER to quit \n')

    # Evolve the Grid
    gol_grid = evolve_grid(gol_grid)
    display_grid(gol_grid)

    if gol_iterate == 'q':
        gol_exit = True
        print('\nGOODBYE!')

