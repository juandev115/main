#declarar matriz}

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
 ]
print(f"Matriz A:{A}")
print(f"Tipo de A: {type(A)}")
print((A[2][2]))
print((A[1][0]))
print((A[0][2]))
A[2][2] = 10
for filas in A:
    for elementos in filas:
        print(f"elementos:{elementos}")

import numpy as np
B = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]
              ]
              )
print (type(B))
B[2][2] = 10
c = np.array([[2, 4, 6],
            [3,5,7],
            [10,1,8]]
            )
print(type(c))

print(B.shape)
print(c.shape)

suma = B+c

print(f"suma\n{suma}")

print(f"resta\n{B-c}")
print(f"resta\n{B*c}")
print(f"resta\n{B/c}")
#MODIFICAR ELEMENTOS
