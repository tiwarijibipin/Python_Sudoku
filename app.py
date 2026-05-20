from flask import Flask, render_template, jsonify, request, make_response
from sudoku import Sudoku
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# --- THE KEY CHANGE IS HERE ---
@app.route('/generate-puzzle', methods=['POST']) # Changed from GET to POST
def generate_puzzle():
    # This logic is correct, it will now be forced to run every time.
    puzzle = Sudoku(3, seed=random.randint(1, 100000)).difficulty(0.5)
    debug_id = random.randint(100, 999)
    print(f"SERVER: New puzzle generated with ID: {debug_id}")
    
    payload = {
        'board': puzzle.board,
        'debug_id': debug_id
    }
    
    # We will keep the no-cache headers as an extra precaution
    response = make_response(jsonify(payload))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    
    return response

@app.route('/solve-puzzle', methods=['POST'])
def solve_puzzle():
    board = request.json['board']
    puzzle = Sudoku(3, 3, board=board)
    solution = puzzle.solve()
    return jsonify(solution=solution.board)

if __name__ == '__main__':
    app.run(debug=True)