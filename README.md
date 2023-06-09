
# Sudoku Solver Documentation


##Introduction

The Sudoku Solver is a Python program that uses recursive programming and backtracking techniques to solve Sudoku puzzles. Sudoku is a logic-based puzzle game in which you must fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids contains all of the digits from 1 to 9.

The Sudoku Solver utilizes a depth-first search algorithm, where it places a digit in an empty cell and recursively attempts to solve the puzzle. If the chosen digit leads to an unsolvable puzzle, the algorithm backtracks and tries a different digit until a valid solution is found.

## Installation


1) Ensure you have Python installed on your system (version 3 or above).

2) Download the Sudoku Solver source code from the repository or copy it from this documentation.

3) install the requirements.txt

       pip install -r requirements.txt
      
4) you can try soliving it youself with running the GUI.py

       python3 GUI.py
       
5) or run the main.py to have the soled puzzel in Terminal
      
       python3 main.py
       
