board = [
    [0,0,0,0,0,0,0,0,0],
    [2,0,6,0,0,0,1,0,3],
    [3,0,0,1,7,6,0,0,8],
    [0,6,0,0,0,0,0,4,0],
    [0,0,0,0,9,0,0,0,0],
    [0,9,8,0,0,0,7,3,0],
    [9,1,0,0,3,0,0,6,5],
    [0,0,0,4,2,5,0,0,0],
    [0,0,3,0,6,0,4,0,0]
]

board = [
    [0,0,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,0,0,0,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board = [
    [4,6,0,0,0,0,0,3,2],
    [9,0,5,0,6,0,1,0,8],
    [0,8,0,1,0,2,0,5,0],
    [6,0,0,0,0,0,0,0,3],
    [0,0,0,5,2,9,0,0,0],
    [0,1,0,0,0,0,0,9,0],
    [2,0,7,0,1,0,8,0,5],
    [0,3,0,0,0,0,0,2,0],
    [0,0,0,0,9,0,0,0,0],
    ]

def print_board(board):
    '''Prints the Sudoku board
        list -> None'''
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print('---------------------')
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print('| ', end='')
            print(board[i][j], end=' ')
        print()

def find_empty(board):
    '''Finds an empty cell to be filled.
        list -> (int, int)'''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j)

def valid(board, n, pos, track):
    '''Returns true if the number filled in the particular cell is valid
        list, int, (int, int), list -> bool'''
    x,y = pos

    #if the cell was filled earlier, then return False for the given number
    if track and track[-1][0] == pos and track[-1][1]<=n:
        track.pop()
        return False

    #check the validity in row
    for i in range(len(board[x])):
        if board[x][i]==n:
            return False

    #check the validity in column
    for i in range(len(board)):
        if board[i][y]==n:
            return False
    #check the validity in the particular cell
    for i in range(3):
        for j in range(3):
            u = i+3*(x//3)
            v = j+3*(y//3)
            if board[u][v]==n:
                return False
    return True

def solve(board):
    '''solves the given sudoku board
        list -> list'''
    track=[] 
    #assuming that the last row has at least one empty cell
    while board[-1].count(0)>0:
        empty = find_empty(board)
        flag = 0
        for i in range(1,10):
            if valid(board, i, empty, track):
                board[empty[0]][empty[1]] = i
                track.append([empty,i])
                flag=1
                break
        if flag==0:
            x,y = track[-1][0]
            board[x][y]=0

print("The given board:\n")
print_board(board)
solve(board)
print('\nSolution:\n')
print_board(board)
