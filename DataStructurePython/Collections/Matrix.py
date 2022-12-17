
import numpy

matrix = numpy.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(matrix.shape)

for row in matrix:
    for column in row:
        print(column)
        
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        print(matrix[i][j])