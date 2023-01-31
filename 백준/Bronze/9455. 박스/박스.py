T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    
    matrix = []
    for _ in range(m):
        num_list = list(map(int, input().split()))
        matrix.append(num_list)

    new_matrix = [[0]*m for _ in range(n)] 

    N = len(matrix)
    M = len(matrix[0])

    for i in range(M):
        for j in range(N):
            new_matrix[i][j] = matrix[j][i]
 
    result = 0
    for mat in new_matrix:
    
        for _ in range(len(mat)):
            if mat[0] == 1:
               cnt = mat.count(0)
               result += cnt
               del mat[0]
            elif mat[0] == 0:
                del mat[0]

    print(result)
