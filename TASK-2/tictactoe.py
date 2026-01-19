def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def is_winner(board, player):
    win_combos = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combos)

def is_terminal(board):
    return is_winner(board, 'X') or is_winner(board, 'O') or ' ' not in board

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'): return 10 - depth
    if is_winner(board, 'X'): return depth - 10
    if ' ' not in board: return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval_score = minimax(board, depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval_score = minimax(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval_score)
        return min_eval

def ai_move(board):
    best_score = -float('inf')
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

# Main game loop
board = [' '] * 9
print("Positions: 1|2|3\n           4|5|6\n           7|8|9")
current_player = 'X' # Human starts

while not is_terminal(board):
    print_board(board)
    if current_player == 'X':
        try:
            move = int(input("Your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
            else:
                print("Invalid move!")
                continue
        except:
            print("Invalid input!")
            continue
    else:
        ai_move(board)
        print("AI made move.")
    
    current_player = 'O' if current_player == 'X' else 'X'

print_board(board)
if is_winner(board, 'X'): 
    print("You win!")
elif is_winner(board, 'O'): 
    print("AI wins!")
else: 
    print("Tie!")
