#Robert Florance
#N-Queens Monte Carlo Algorithm | 12.12.11 | CP407
import array, math, time, sys, csv, random
from decimal import Decimal

numnodes = 1
m = 1
mprod = 1

total = 0

board_size = int(sys.argv[1])
solution_list = array.array('i', [0]* (board_size + 1)) 

def nqueen(current_row, num_row, solution_list):
    global mprod, numnodes, m, total
    if current_row == num_row: 
        total += numnodes
        print 'reached end, numnodes =', numnodes
    else:
        current_row += 1
        num_promising, chosen_child = gen_next_moves(current_row, solution_list, num_row + 1) 
        if chosen_child != None:
            
            mprod = mprod*num_promising
            numnodes = numnodes + mprod*num_row
            
            solution_list[current_row] = chosen_child #instead of adding a list, like we normally would have gotten
            nqueen(current_row, num_row, solution_list) 
            solution_list[current_row] = 0 
        else:
            total += numnodes
            print 'no child returned, numnodes =', numnodes 

#Generate all the promising children, return how many there are + only one of them
def gen_next_moves(a_row, solution_list, num_of_rows):
    possible_moves = [] 
    for column in range(1, num_of_rows): 
        under_attack =  False
        for row in range(1, a_row): 
            if (abs(a_row - row) == abs(column - solution_list[row]) or solution_list[row] == column): 
                under_attack = True 
                break 
        if not under_attack:
            possible_moves.append(column)
    if len(possible_moves) > 0:
        return len(possible_moves), random.choice(possible_moves) 
    else:
        return None, None

REPEAT = int(sys.argv[2])

for i in range(REPEAT):
    nqueen(0, board_size, solution_list) #pass: START ROW, NUMBER OF ROWS, SOLUTION LIST

    #Reset Values:
    numnodes = 1
    m = 1
    mprod = 1

    board_size = int(sys.argv[1])
    solution_list = array.array('i', [0]* (board_size + 1)) 


prediction = total/REPEAT
print 'avg nodes_visited', prediction

if sys.argv[3] == 'r':
        writer = csv.writer(open('nqmc.csv', 'a'))
        writer.writerows([ (board_size, prediction) ])
