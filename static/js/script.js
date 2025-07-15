document.addEventListener('DOMContentLoaded', () => {
    const boardElement = document.getElementById('sudoku-board');
    const newGameBtn = document.getElementById('new-game-btn');
    const solveBtn = document.getElementById('solve-btn');

    function generateBoard(board) {
        boardElement.innerHTML = '';
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                const cell = document.createElement('input');
                cell.classList.add('cell');
                cell.type = 'text';
                cell.maxLength = 1;
                cell.value = board[i][j] || '';
                cell.disabled = board[i][j] !== null;
                boardElement.appendChild(cell);
            }
        }
    }

    newGameBtn.addEventListener('click', () => {
        fetch('/generate-puzzle')
            .then(response => response.json())
            .then(data => generateBoard(data.board));
    });

    solveBtn.addEventListener('click', () => {
        const cells = Array.from(boardElement.getElementsByClassName('cell'));
        const board = [];
        for (let i = 0; i < 9; i++) {
            const row = [];
            for (let j = 0; j < 9; j++) {
                const value = cells[i * 9 + j].value;
                row.push(value ? parseInt(value) : null);
            }
            board.push(row);
        }

        fetch('/solve-puzzle', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ board: board })
        })
            .then(response => response.json())
            .then(data => generateBoard(data.solution));
    });

    // Initial board generation
    newGameBtn.click();
});