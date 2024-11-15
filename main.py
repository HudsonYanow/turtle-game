import copy

def make_grid(cols, rows):
    grid = []
    for _ in range(rows):
        row = [0] * cols
        grid.append(row)
    return grid
    
def print_grid(grid):
    for row in grid:
        row_str = " ".join(map(str, row))
        print(row_str)
# print_grid(grid)

def check_grid(grid):
    valid=False
    for row  in grid:
        if len(row)==len(grid):
            valid=True
        else:
            valid=False
    return valid 
            

def create_turtle(grid, counter=0):
    updated_grid=grid
    updated_grid[-1][0]=1 # GOOD JOB!
    counter+=1
    return counter,updated_grid

def create_cross(grid, point):
    updated_grid=grid
    if (point[0]<len(grid)and point[0]>=0) and point[1]<len(grid)and point[1]>=0:
        updated_grid[point[1]][point[0]]="X" # AWESOME!
    # WHAT HAPPENS IF THE POINT IS OUTSIDE THE GRID?
    return updated_grid

def move_turtule(grid, counter=1, direction="right"): # THE FIRST ARGUMENT SHOULD BE grid nor updated_grid since it wasn't updated yet
    updated_grid=copy.deepcopy(grid)
    updated_counter=counter+1
    while counter>=1:
        for x,row in enumerate(updated_grid): # google "python for loop enumerate" to see how to loop through a list and get the index
            for y,col in enumerate(row):
                if updated_grid[x][y]==counter:
                    updated_grid[x][y]+=1
                    counter-=1
                    if counter==1:
                        if direction=="right":
                            if y<=len(grid)-2:
                                if updated_grid[x][y+1]==0:
                                    updated_grid[x][y+1]=1
                                else:
                                    return updated_counter-1, grid
                            else:
                                return updated_counter-1, grid
                        elif direction=="left":
                            if y>0:
                                if updated_grid[x][y-1]==0:
                                    updated_grid[x][y-1]=1
                                else:
                                    return updated_counter-1, grid
                            else:
                                return updated_counter-1, grid
                        elif direction=="up":
                            if x>0:
                                if updated_grid[x-1][y]==0:
                                    updated_grid[x-1][y]=1
                                else:
                                    return updated_counter-1, grid
                            else:
                                return updated_counter-1, grid
                        elif direction=="down":
                            if x<=len(grid)-2:
                                if updated_grid[x+1][y]==0:
                                    updated_grid[x+1][y]=1
                                else:
                                    return updated_counter-1, grid
                            else:
                                return updated_counter-1, grid
    return updated_counter, updated_grid

def start_game(directions):
    grid=make_grid(3,3)
    print("grid made")
    valid=check_grid(grid)
    print("grid checked")
    if valid:
        foundCross=False
        cross=(2,1)
        grid=create_cross(grid, cross)
        print("made ross")
        counter,grid=create_turtle(grid)
        print("made turtle")
        for direction in directions:
            counter,grid=move_turtule(grid, counter, direction)
            print("moved turtle")
        for x,row in enumerate(grid): # google "python for loop enumerate" to see how to loop through a list and get the index
            for y,col in enumerate(row):
                if grid[x][y]==1:
                    if x==cross[0]and y==cross[1]:
                        foundCross=True

    return counter, grid, foundCross

def print_game(counter, grid, foundCross):
    print(f"The counter was equal to {counter}")
    print_grid(grid)
    if foundCross==True:
        print("The turtle found the cross")

counter, grid, foundCross=start_game(['right', 'right', 'down', 'down', 'left', 'left', 'up', 'up'])
print_game(counter, grid, foundCross)