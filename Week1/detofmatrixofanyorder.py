from sympy import Matrix

def determinant(matrix):
    return matrix.det()
    
matrix=Matrix([[1,2,3,4],[5,2,6,2],[5,2,5,4],[3,5,7,2]])

det=determinant(matrix)
print("det=",det)'''