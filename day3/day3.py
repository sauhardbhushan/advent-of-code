import numpy as np

with open('./day3.txt', 'r') as f1:
    lines = f1.read().split()
    forest = []

    for i, r in enumerate(lines):
        forest.append([char for char in r])

    forest = np.asarray(forest)
    nrows, ncols = forest.shape


def move(arr, current_row, current_col, right=0, down=0, n_trees_found=0):
    current_col = (current_col + right) % (ncols)

    current_row += down
    if current_row >= nrows:
        return n_trees_found

    if arr[current_row][current_col] == '#':
        n_trees_found += 1

    return move(arr, current_row, current_col, right=right, down=down, n_trees_found=n_trees_found)


moves_dict = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total_trees = []

for right, down in moves_dict:
    n_trees_found = move(forest, 0, 0, right=right, down=down,
                         n_trees_found=0)
    total_trees.append(n_trees_found)


print(np.prod(total_trees))
