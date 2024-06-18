import numpy as np
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

row_sums = matrix.sum(axis=1)
col_sums = matrix.sum(axis=0)

print("Row Sums:", row_sums)
print("Column Sums:", col_sums)
