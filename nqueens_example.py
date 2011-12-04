##############################################################################
# a script to solve the n queen problem in which n queens are to be placed on
# an nxn chess board in a way that none of the n queens is in check by any other
#queen using backtracking'''
##############################################################################
import sys
import time
import array

solution_count = 0

def queen(current_row, num_row, solution_list):
    if current_row == num_row:
        global solution_count 
        solution_count = solution_count + 1
    else:
        current_row += 1
        next_moves = gen_nextpos(current_row, solution_list, num_row + 1)
        if next_moves:
            for move in next_moves:
                '''make a move on first legal move of next moves'''
                solution_list[current_row] = move
                queen(current_row, num_row, solution_list)
                '''undo move made'''
                solution_list[current_row] = 0
        else:
            return None

def gen_nextpos(a_row, solution_list, arr_size):
    '''function that takes a chess row number, a list of partially completed 
    placements and the number of rows of the chessboard. It returns a list of
    columns in the row which are not under attack from any previously placed
    queen.
    '''
    cand_moves = []
    '''check for each column of a_row which is not in check from a previously
    placed queen'''
    for column in range(1, arr_size):
        under_attack =  False
        for row in range(1, a_row):
            '''
            solution_list holds the column index for each row of which a 
            queen has been placed  and using the fact that the slope of 
            diagonals to which a previously placed queen can get to is 1 and
            that the vertical positions to which a queen can get to have same 
            column index, a position is checked for any threating queen
            '''
            if (abs(a_row - row) == abs(column - solution_list[row]) 
                    or solution_list[row] == column):
                under_attack = True
                break
        if not under_attack:
            cand_moves.append(column)
    return cand_moves

def main():
    '''
    main is the application which sets up the program for running. It takes an 
    integer input,N, from the user representing the size of the chessboard and 
    passes as input,0, N representing the chess board size and a solution list to
    hold solutions as they are created.It outputs the number of ways N queens
    can be placed on a board of size NxN.
    '''
    #board_size =  [int(x) for x in sys.stdin.readline().split()]
    board_size = [15]
    board_size = board_size[0]
    solution_list = array.array('i', [0]* (board_size + 1))
    #solution_list =  [0]* (board_size + 1)
    queen(0, board_size, solution_list)
    print(solution_count)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(time.time()) 
