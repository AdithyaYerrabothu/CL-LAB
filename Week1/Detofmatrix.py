def dett(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    elif len(matrix)==2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    else:
        det=0
        for j in range(len(matrix)):
            minor=[row[:j]+row[j+1:] for row in matrix[1:]]
            det=det+(-1)**j *matrix[0][j]*dett(minor)
        return det
        
matrix = [[55,25,15],[30,44,2],[11,45,77]]

det=dett(matrix)
print("det=",det)