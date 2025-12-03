# Backtracking

## What is Backtracking?

**Backtracking** is a problem-solving algorithmic technique that involves finding a solution incrementally by trying different options and undoing them if they lead to a dead end. It is commonly used in situations where you need to explore multiple possibilities to solve a problem, like searching for a path in a maze or solving puzzles like Sudoku. When a dead end is reached, the algorithm backtracks to the previous decision point and explores a different path until a solution is found or all possibilities have been exhausted.

> **Backtracking** can be defined as a general algorithmic technique that considers searching every possible combination in order to solve a computational problem.

## Types of Backtracking Problems

Problems associated with backtracking can be categorized into 3 categories:

- Decision Problems: Here, we search for a feasible solution.
- Optimization Problems: For this type, we search for the best solution.
- Enumeration Problems: We find set of all possible feasible solutions to the problems of this type.

## Pseudocode for Backtracking

The best way to implement backtracking is through recursion, and all backtracking code can be summarised as per the given Pseudocode:

```python
def FIND_SOLUTIONS(parameters):

    if (valid solution):
        store the solution
        return

    for (all choice):
        if (valid choice):
            APPLY(choice)

            FIND_SOLUTIONS(parameters)

            BACKTRACK(remove choice)

    return
```

---

© Credits: [GeeksforGeeks](https://www.geeksforgeeks.org/)
