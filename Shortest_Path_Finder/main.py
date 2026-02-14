import curses
from curses import wrapper
import queue
import time

maze = [
        ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
        ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
    ]


# print the maze
def print_maze(maze, stdscr, path=[]):
    BLUE=curses.init_pair(1) # this is maze color
    RED=curses.init_pair(2) # this is color of path we have to find

    for i,row in enumerate(maze):
        for j, value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,"X",RED)
            else:
                stdscr.addstr(i,j*2,value, BLUE)  # here is j*2 for the space, blue to highlight maze as blue

                     
# finder the starter element
def find_start(maze, start):
    
    for i,row in enumerate(maze):
        for j, value in enumerate(row):
            return i,j # return the index where it is present
        
    
    return None


# path finder(bfs)
def find_path(maze, stdscr):
    
    start="O"
    end="X"
    start_pos=find_start(maze,start)

    q=queue.Queue()
    q.put((start_pos, [start_pos]))

    visited=set()  # show which node are visited

    while not q.empty():

        current_pos, path=q.get()
        row, col=current_pos

        # add new screen
        stdscr.clear() 
        print(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()


        if maze[row][col]==end:
            return path
        
        # negihbours

        neighbors=find_neighbor(maze, row, col)

        for neighbor in neighbors:
             if neighbor in visited:
                 continue
             

             r,c=neighbor

             if maze[r][c]=="#":
                 continue
             
             new_path= path + [neighbor]
             q.put((neighbor, new_path))
             visited.add(neighbor)




# find meighbour (check the number(up,down,left,right))
def find_neighbor(maze, row, col):

    neighbors=[]

    if row> 0: # up
        neighbors.append((row -1 ,col))

    if row+1 < len(maze): # Down
        neighbors.append((row+1, col))

    if col>0: # left
        neighbors.append((row ,col - 1))

    if col < len(maze): #right
        neighbors.append((row, col+1))
    

    return neighbors


# main method
def  main(stdscr): #  make a standard output screen,

    # apply the color
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE) # here is (1) is id, blue here is text color, and white is background color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)


    # call the functions
    find_path(maze, stdscr)
    stdscr.getch() # here is getch to get character just work like a input()


wrapper(main)





