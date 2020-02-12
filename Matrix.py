
import numpy as np

# create 2x2 matrix
a = np.matrix([[1, 2], [3, 4]])  # using array of array
print('2x2 matrix is:\n', a)
# using shape attribute to get the tuple describing matrix shape
print('The dimension of the matrix is :', a.shape)

# using MatLab syntax in string
b = np.matrix('[1,2;3,4;5,6]', dtype=np.int32)  # limiting the data-type to int
print('\n3x2 matrix is:\n', b)
# using shape attribute to get the tuple describing matrix shape
print('The dimension of the matrix is :', b.shape)

# using numpy.random.rand(row, column) to generate array of random element
c = np.matrix(np.random.rand(3, 3), dtype=np.float32)  # considering the data-type as float
print('\n3x3 random element matrix is:\n', c)
# using shape attribute to get the tuple describing matrix shape
print('The dimension of the matrix is :', c.shape)
