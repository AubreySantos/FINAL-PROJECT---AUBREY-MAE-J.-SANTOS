matrix = [[1, 2, 3], 
          [4, 5, 6],
          [7, 8, 9]]
tld = sum([matrix[i][i] for i in range(len(matrix))])
bld = sum([matrix[len(matrix)-1-i][i] for i in range(len(matrix))])
print(f'{tld}\n{bld}')