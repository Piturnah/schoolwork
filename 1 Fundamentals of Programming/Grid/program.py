def Draw_Grid(xPos, yPos):
    grid = [["x" for x in range(4)] for y in range(6)]
    grid[xPos][yPos] = "O"
    return grid
    
print(Draw_Grid(0,0))

while True:
    coords = input("Enter pos (x,y)\n> ").split(",")
    newGrid = Draw_Grid(int(coords[0]), int(coords[1]))
    for i in range (0,len(newGrid[0])):
        print(newGrid[i])
