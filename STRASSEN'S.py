import numpy as np

def partition(matrix):

    l = len(matrix)
    if(l % 2 != 0):
        stack = []
        for x in range(l + 1):
            stack.append(float(0))
        l += 1
        matrix = np.insert(matrix, len(matrix), values=0, axis=1)
        matrix = np.vstack([matrix, stack])

    d = (l // 2)
    matrix = matrix.reshape(l, l)
    complete = [matrix[:d, :d], matrix[d:, :d], matrix[:d, d:], matrix[d:, d:]]

    return complete


def strassen(mA, mB, n):
    n1 = len(mA)
    n2 = len(mB)

    if(n1 and n2 <= n):
        return (mA * mB)

    else:

        print(mA)
        A = partition(mA)
        B = partition(mB)
        c = np.matrix([0 for i in range(len(mA))]for j in range(len(mB)))
        C = partition(c)

        a11 = np.array(A[0])
        a12 = np.array(A[2])
        a21 = np.array(A[1])
        a22 = np.array(A[3])

        b11 = np.array(B[0])
        b12 = np.array(B[2])
        b21 = np.array(B[1])
        b22 = np.array(B[3])

        m1 = np.array(strassen((a11 + a22), (b11 + b22)))
        m2 = np.array(strassen((a21 + a22), b11))
        m3 = np.array(strassen(a11, (b12 - b22)))
        m4 = np.array(strassen(a22, (b21 - b11)))
        m5 = np.array(strassen((a11 + a12), b22))
        m6 = np.array(strassen((a21 - a11), (b11 + b12)))
        m7 = np.array(strassen((a12 - a22), (b21 + b22)))

        C[0] = np.array((m1 + m4 - m5 + m7))
        C[2] = np.array((m3 + m5))
        C[1] = np.array((m2 + m4))
        C[3] = np.array((m1 - m2 + m3 + m6))

        return np.array(C)


matrixA = []
matrixB = []
n = int(input("Enter the no of rows and columns of A : "))
print("Enter matrix A : ")

for i in range(n):
    s = input()
    s = s.split()
    s = list(map(float, s))
    matrixA.append(s)

m = int(input("Enter the no of rows and columns of A : "))
print("Enter matrix B : ")

for i in range(m):
    s = input()
    s = s.split()
    s = list(map(float, s))
    matrixB.append(s)

matrixA = np.matrix(matrixA)
matrixB = np.matrix(matrixB)

matrixC = [[0 for i in range(n)]for j in range(n)]

print("C = ")
print(strassen(matrixA, matrixB, n))