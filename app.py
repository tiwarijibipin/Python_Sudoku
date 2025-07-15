from flask import Flask, render_template, jsonify, request
from sudoku import Sudoku

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-puzzle')
def generate_puzzle():
    # Generate a new Sudoku puzzle with a certain difficulty
    # The difficulty is a value between 0 and 1, where 0.5 means half the cells are empty
    puzzle = Sudoku(3).difficulty(0.5)
    return jsonify(board=puzzle.board)

@app.route('/solve-puzzle', methods=['POST'])
def solve_puzzle():
    # Get the board from the request
    board = request.json['board']
    
    # Create a Sudoku instance with the provided board
    puzzle = Sudoku(3, 3, board=board)
    
    # Solve the puzzle
    solution = puzzle.solve()
    
    return jsonify(solution=solution.board)

if __name__ == '__main__':
    app.run(debug=True)