def display_board(data):
    ''' Function displays the board on the console '''
    print('-------------')
    for row in data:
        print(f'| {row[0]} | {row[1]} | {row[2]} |')
        print('-------------')

def check_winner(data):
    ''' analyze the current game data to determine
        if there is a winner or if the game is a
        draw.
        Return an O or X for a winner
        Return 'Draw' for a draw
        Return an empty string otherwise
    '''

    # there are 8 possible ways to win, a complete
    # row is already available in the data, but need
    # to create complete columns, and the two diags
    col1 = [data[0][0],data[1][0],data[2][0]]
    col2 = [data[0][1],data[1][1],data[2][1]]
    col3 = [data[0][2],data[1][2],data[2][2]]
    posDiag = [data[2][0],data[1][1],data[0][2]]
    negDiag = [data[0][0],data[1][1],data[2][2]]

    # put all the lists into one large list to iterate through
    allChecks = [col1,col2,col3,posDiag,negDiag,data[0],data[1],data[2]]

    # keep a boolean to track if there are any empty cells
    anyEmpty = False

    # loop through all the possible winning combinations
    for check in allChecks:
        # first keep track if any of the sets contains an empty square
        if ' ' in check:
            anyEmpty = True

        # check if any set is all 'O' or all 'X'
        if set(check) == set('O'):
            return 'O'
        elif set(check) == set('X'):
            return 'X'

    if not anyEmpty:
        return 'Draw'

    return ''

def get_value(valueType):
    ''' Loop until the player enters a number 
        between 1 and 3 inclusive
    '''
    while True:
        numIn = input(f'Enter a {valueType} number (1-3): ')
        if numIn.isdigit():
            if int(numIn) in range(1,4):
                return int(numIn)
            else:
                print('Enter a number between 1 and 3 please.')
        else:
            print("Please input a number.")


def get_input(playerID, data):
    ''' Show who's turn it is and then loop
        until the player chooses a valid location
        to place an X or O
    '''
    print(f'It is {playerID}\'s turn!')  
    output = [0,0]

    while True:
        output[0] = get_value('row')
        output[1] = get_value('column')
        if data[output[0]-1][output[1]-1] == ' ':
            data[output[0]-1][output[1]-1] = playerID
            break
        else:
            print('That square is already taken, please enter a new location.')

    return data

def swap_player(playerID):
    if playerID == 'O':
        return 'X'
    else:
        return 'O'

def get_starting_player():
    ''' Prompt the player to input and X or O
        only allow upper or lower case x or o
    '''
    while True:
        player = input('Choose starting player: (X or O): ')
        if player.upper() == 'X' or player.upper() == 'O':
            return player.upper()
        else:
            print('Please only enter X or O')

def start_again():
    ''' Prompt to continue, allowing only
        upper or lower case y or n
    '''
    while True:
        response = input('Do you want to play again? (Y/N): ')
        if response.upper() == 'Y' or response.upper() == 'N':
            return response.upper() == 'Y'
        else:
            print('Please enter Y or N.')

def reset_data():
    return [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def main():
    # the games data and current player
    data = reset_data()
    player = get_starting_player()

    while True:
        display_board(data)
        data = get_input(player, data)
        player = swap_player(player)
        currentWinner = check_winner(data)

        if currentWinner == 'Draw' or currentWinner != '':
            display_board(data)
            if currentWinner == 'Draw':
                print('Game is a draw!')
            else:
                print(f'Congratulation {currentWinner}!  You won the game!')

            if start_again():
                data = reset_data()
                player = get_starting_player()
            else:
                break

    print('Thank you for playing!\n')

if __name__ == '__main__':    
    main()