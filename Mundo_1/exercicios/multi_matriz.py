def mult_matrix(A,B):
    nLinhasA = len(A)
    nColunasA = len(A[0])
    nColunasB = len(B[0])
    
    M = []
    
    for linha in range(nLinhasA):
        M.append([])
        for coluna in range(nColunasB):
            M[linha].append(0)
            for k in range(nColunasA):
                M[linha][coluna] += A[linha][k]*B[k][coluna]       
    return M
    
A = [[1,1,1],[2,2,2],[3,3,3]]
B = [[1,1,1],[1,1,1],[1,1,1]] # matrix identidade: [[1,0,0],[0,1,0],[0,0,1]]
print(mult_matrix(A,B))


from numpy import array
vetor1 = array([1, 2, 3, 4], dtype=int)
vetor2 = array([0, 0, 0, 0], dtype=int)
aux = 0
for elemento in vetor1:
    vetor2[aux] = elemento*10
    aux+=1
print(vetor2)

from numpy import array
matriz = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=int)
aux_linha = 0
aux_coluna = 0
for linha in matriz:
    for elemento in linha:
        if aux_linha == aux_coluna:
            print(elemento)
        aux_coluna += 1
    aux_linha += 1
    aux_coluna = 0