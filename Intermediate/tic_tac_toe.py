'''
Objectives
The program should work as follows:

Get the 3x3 grid from the input as in the previous stages.
Output this 3x3 grid as in the previous stages.
Prompt the user to make a move.
The user should input 2 numbers that represent the cell where they want to place their X. (the 9 symbols representing the field will be the first line of input, and the 2 coordinate numbers will be the second line of input)
Analyze user input and show messages in the following situations:
This cell is occupied! Choose another one! if the cell is not empty.
You should enter numbers! if the user enters non-numeric symbols in the coordinates input.
Coordinates should be from 1 to 3! if the user enters coordinates outside the game grid.
Update the grid to include the user's move and print the updated grid to the console.
'''
enter_cells = input()

print('---------')
print('|', enter_cells[0], enter_cells[1],  enter_cells[2], '|')
print('|', enter_cells[3], enter_cells[4],  enter_cells[5], '|')
print('|', enter_cells[6], enter_cells[7],  enter_cells[8], '|')
print('---------')

amount_x = 0
amount_o = 0
for i in enter_cells:
    if i == 'X':
        amount_x += 1
    elif i == 'O':
        amount_o += 1

if abs(amount_x - amount_o) > 1:
    print('Impossible')
else:
    win_o = False
    win_x = False
    # horizontal
    for y in range(0, 9, 3):
        sum_ = ''
        for x in range(3):
            sum_ += enter_cells[y + x]
        if sum_ == 'XXX':
            win_x = True
        elif sum_ == 'OOO':
            win_o = True

    # vertical
    if not win_x and not win_o:
        sum_ = ''
        for y in range(3):
            sum_ = ''
            for x in range(0, 9, 3):
                sum_ += enter_cells[y + x]
            if sum_ == 'XXX':
                win_x = True
            elif sum_ == 'OOO':
                win_o = True
    # Diagonal
    if not win_x and not win_o:
        sum_ = ''
        for x in range(0, 9, 4):
            sum_ += enter_cells[x]
        if sum_ == 'XXX':
            win_x = True
        elif sum_ == 'OOO':
            win_o = True
    if not win_x and not win_o:
        sum_ = ''
        for x in range(2, 7, 2):
            sum_ += enter_cells[x]
        if sum_ == 'XXX':
            win_x = True
        elif sum_ == 'OOO':
            win_o = True

    if not win_x and not win_o:
        if (amount_x + amount_o) == 9:
            print('Draw')
        else:
            print('Game not finished')

    if win_o and win_x:
        print('Impossible')
    elif win_o ^ win_x:
        print('X' if win_x else 'O', 'wins')