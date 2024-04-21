from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/make_move', methods=['POST'])
def make_move():
    data = request.get_json()
    board = data['board']

    move = find_best_move(board)

    return jsonify({'move': move})

def find_best_move(board):
    # Implement the AI logic using the minimax algorithm
    move = minimax(board, 'O')['position']
    return move

def minimax(board, player):
    if check_winner(board) == 'O':
        return {'score': 1}
    elif check_winner(board) == 'X':
        return {'score': -1}
    elif is_board_full(board):
        return {'score': 0}

    if player == 'O':
        best_move = {'score': float('-inf')}
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    score = minimax(board, 'X')['score']
                    board[i][j] = ''
                    if score > best_move['score']:
                        best_move['score'] = score
                        best_move['position'] = (i, j)
        return best_move
    else:
        best_move = {'score': float('inf')}
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    score = minimax(board, 'O')['score']
                    board[i][j] = ''
                    if score < best_move['score']:
                        best_move['score'] = score
                        best_move['position'] = (i, j)
        return best_move

def check_winner(board):
    for i in range(3):
        if board[i][0] != '' and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != '' and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] != '' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != '' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return ''

def is_board_full(board):
    for row in board:
        if '' in row:
            return False
    return True

if __name__ == '__main__':
    app.run(debug=True)
