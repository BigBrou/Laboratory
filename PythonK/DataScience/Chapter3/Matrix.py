A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 2], [3, 4], [5, 6]]

def shape(Matrix):
    num_rows = len(Matrix)
    num_cols = len(Matrix[0]) if A else 0
    return num_rows, num_cols

print(shape(A))
print(shape(B))

def get_row(Matrix, AIdx):
    return Matrix[AIdx]

def get_column(Matrix, AIdx):
    return [Matrix_i[AIdx] for Matrix_i in Matrix]

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(x, y) for y in range(num_cols)] for x in range(num_rows)]

def is_diagonal(i, j):
        return 1 if i == j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)
print(identity_matrix)

#print(get_row(A, 1))
#print(get_column(A, 2))
