# maze-solver

## Description

This project was an exercise for me to get a deeper understanding of working with search algorithms. Here I mainly used 
depth-first search algorithms, but the project can be extended to other search algorithms as well. Perhaps you would 
like to try a breadth-first search algorithm to solve the maze?

## Installation

To install the project on MacOS or Linux be sure to have a Python version installed, either globally or as virtual 
environment. The run the following commands:
```BASH
git clone https://github.com/langer-net/maze-solver
cd maze-solver
```

## Usage

To run the project use the following command:
```BASH
python main.py
```
The program displays a window in which a grid is rendered. This grid is then transformed into a maze using a **recursive 
depth-first algorithm**. Another **recursive depth-first algorithm** then attempts to solve the maze. A **red line** 
shows the correct path through the maze, while **gray lines** indicate failed attempts.

## Versions

This project was written in Python v3.11.7, but should run with Python versions v3.8 or higher.

## Dependencies

There are no external dependencies for this project.

## Testing

To execute the tests run:
```BASH
python -m unittest tests/test_maze.py
```

## License

This project is licensed under MIT licence.