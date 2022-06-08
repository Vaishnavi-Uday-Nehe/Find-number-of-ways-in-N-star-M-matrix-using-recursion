def matrix_recur(n,m):
    if n == 1 or m == 1 :
        return 1

    else:
        return matrix_recur(m-1,n) + matrix_recur(m,n-1)

m = 3
n = 3
print(matrix_recur(m,n))
