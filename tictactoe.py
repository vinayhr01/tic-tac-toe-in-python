board = {
    'topl': ' ', 'topm': ' ', 'topr': ' ',
    'midl': ' ', 'midm': ' ', 'midr': ' ',
    'lowl': ' ', 'lowm': ' ', 'lowr': ' '
}
def printBoard(board):
    print(board['topl'] + '|' + board['topm'] + '|' + board['topr'])
    print('-+-+-')
    print(board['midl'] + '|' + board['midm'] + '|' + board['midr'])
    print('-+-+-')
    print(board['lowl'] + '|' + board['lowm'] + '|' + board['lowr'])

def logic(board):
    if board['topl'] == board['topm'] == board['topr'] != ' ':
        printBoard(board)
        print(board['topl'] + ' is the winner!')
        exit()
    elif board['midl'] == board['midm'] == board['midr'] != ' ':
        printBoard(board)
        print(board['midl'] + ' is the winner!')
        exit()
    elif board['lowl'] == board['lowm'] == board['lowr'] != ' ':
        printBoard(board)
        print(board['lowl'] + ' is the winner!')
        exit()
    elif board['topl'] == board['midl'] == board['lowl'] != ' ':
        printBoard(board)
        print(board['topl'] + ' is the winner!')
        exit()
    elif board['topm'] == board['midm'] == board['lowm'] != ' ':
        printBoard(board)
        print(board['topm'] + ' is the winner!')
        exit()
    elif board['topr'] == board['midr'] == board['lowr'] != ' ':
        printBoard(board)
        print(board['topr'] + ' is the winner!')
        exit()
    elif board['topl'] == board['midm'] == board['lowr'] != ' ':
        printBoard(board)
        print(board['topl'] + ' is the winner!')
        exit()
    elif board['topr'] == board['midm'] == board['lowl'] != ' ':
        printBoard(board)
        print(board['topr'] + ' is the winner!')
        exit()
    else:
        return

turn = 'X'
for i in range(9):
    printBoard(board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input().lower()
    if board[move] == 'X' or board[move] == 'O':
        print('Space already taken')
        continue
    board[move] = turn
    logic(board)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(board)
print('Tie!')