a = [[2, 3],
     [4, 5]]

b = [[4, 5],
    [3, 2]]

#addition of two matrices

add_result = [[0, 0],
             [0, 0]]

for i in range (len(a)): #count of row
    for j in range (len(a[0])): #count of columns
        add_result[i][j] = a[i][j] + b[i][j]

for a in add_result:
    print ("Addition", a)

#subtraction of two matrix 

x = [[2, 3],
     [4, 5]]

y = [[4, 5],
    [3, 2]]

sub_result = [[0, 0],
              [0, 0]]

for i in range (len(x)): #count of rows
    for j in range (len(y[0])): #count of columns
        sub_result[i][j] = x[i][j] - y[i][j]

for s in sub_result:
    print ("Subtraction", s)

#Transpose of a matrix

m = [[4, 5],
    [3, 2]]

transpose_result = [[0, 0],
                    [0, 0]]

for i in range (len(m)):
    for j in range (len(m[0])):
        transpose_result [j][i] = m [i][j]

for t in transpose_result:
    print("Transpose", t)

#Multiplication of two matrix

p = [[2, 3],
     [4, 5]]

q = [[4, 5],
    [3, 2]]

mul_result = [[0, 0],
              [0, 0]]

for i in range (len(p)):
    for j in range (len(p[0])):
        mul_result [i][j] = p [i][j] * q [i][j]

for m in mul_result:
    print("Multiplication", m)