# Python Sudoku Web Application

A browser-based Sudoku game built using Python and the Flask web framework. This application allows users to play new Sudoku puzzles of medium difficulty and see the solution with the click of a button.



---

## Core Features

*   **Dynamic Puzzle Generation:** Generates a new, unique Sudoku puzzle every time the "New Game" button is clicked.
*   **Interactive Grid:** Users can type their answers directly into the empty cells on the board.
*   **Instant Solver:** The "Solve" button will automatically compute and display the full solution for the current puzzle.
*   **Simple Interface:** A clean and intuitive user interface that runs smoothly in any modern web browser.

---

## Technologies Used

*   **Backend:** Python, Flask
*   **Frontend:** HTML, CSS, JavaScript
*   **Sudoku Logic:** `py-sudoku` library

---

## How to Run This Project Locally

To set up and run this application on your own machine, please follow these steps.

**Prerequisites:**
*   Python 3 must be installed on your system.

**Step 1: Get the Project Files**

Unzip the project file (`SudokuProject-YourName.zip`) into a folder of your choice. Open a terminal or command prompt and navigate into that folder.

```bash
cd path/to/your/sudoku-app
**Step 2: Create and Activate a Virtual Environment**
It is highly recommended to use a virtual environment to manage project dependencies without affecting your system's global Python installation.

For Windows (Command Prompt):
python -m venv venv
.\venv\Scripts\activate

For macOS / Linux:
python3 -m venv venv
source venv/bin/activate

**Step 3: Install Required Dependencies**
The project's dependencies are listed in the requirements.txt file. Install them using pip:
pip install -r requirements.txt

**Step 4: Run the Flask Application**
With the dependencies installed, you can now start the Flask development server:
python app.py

**Step 5: View the Game in Your Browser**
You will see output in the terminal indicating that the server is running on http://127.0.0.1:5000. Open your web browser and go to this address.
You should now be able to see and play the Sudoku game!
