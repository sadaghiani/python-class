# 1: write python program to transpose given matrix
# https://repl.it/@RezaSadaghiani/transposeGivenMatrix

def transpose(m):
    result = [[[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]]
    for row in result:
        return row

print("result=",transpose([[1, 3, 5], [2, 4, 6]]))
print("result=",transpose([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))
print("result=",transpose([[1, 4, 9]]))

---------------------
# 2: write python program to add two matrix with same dimensions
# https://repl.it/@RezaSadaghiani/twoMatrixWithSameDimensions

def addTwoMatrix(a, b):
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j]+b[i][j])
        res.append(row)
    return res

print(addTwoMatrix([[1,2,3], [4 ,5,6], [7 ,8,9]],[[1,2,3], [4 ,5,6], [7 ,8,9]] ))
