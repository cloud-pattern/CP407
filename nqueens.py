#Robert Florance
#N-Queens Backtracking Algorithm | 11.30.11 | CP407
import array, math, time, sys, csv, random
from decimal import Decimal

solution_count = 0
nodes_visited = 0

def nqueen(current_row, num_row, solution_list):
    global solution_count, nodes_visited
    nodes_visited +=1 #we are visiting a new 'node'
    if current_row == num_row: #if we are at the last row, we are done!  we found another solution
        solution_count = solution_count + 1
        if sys.argv[2] == 'p': print solution_list.tolist()[1:]
    else:
        current_row += 1
        next_moves = gen_next_moves(current_row, solution_list, num_row + 1) #pass: CURRENT ROW, PARTIALLY COMPL. SOLUTION LIST, NUMBER OF ROWS
        if next_moves:
            for move in next_moves: #for each column in the list of possible placements
                solution_list[current_row] = move
                nqueen(current_row, num_row, solution_list) #recursively call on next row + updated solution list
                solution_list[current_row] = 0 #reset list
        else:
            return None #Here is where we are eliminating steps: if there were no next moves for that row, then we give up 

def gen_next_moves(a_row, solution_list, num_of_rows):
    possible_moves = [] # list of columns in row which are not 'under attack'
    for column in range(1, num_of_rows): #Check all of the columns of the given row
        under_attack =  False
        for row in range(1, a_row): #Check prev rows of that column up to the current row 
            if (abs(a_row - row) == abs(column - solution_list[row]) or solution_list[row] == column): #Check Diagonals, Check Vertically
                under_attack = True 
                break #this column in the row is under attack... no need to check the rest of prev rows 
        if not under_attack:
            possible_moves.append(column)
    return possible_moves #return a list of all possible columns for the given row

board_size = int(sys.argv[1])
solution_list = array.array('i', [0]* (board_size + 1)) #create an array of rows/colums, which will store the value of the # row/column that the queen is placed in
t0 = time.clock()
nqueen(0, board_size, solution_list) #pass: START ROW, NUMBER OF ROWS, SOLUTION LIST
timer = time.clock() -t0
total_nodes = ((board_size**(board_size+1)-1)/(board_size-1))/1.0
print '# of solutions', solution_count
print 'Process time', timer
print 'Nodes visited', nodes_visited
print 'Total nodes', total_nodes
print '% visited', (nodes_visited/total_nodes)*100
