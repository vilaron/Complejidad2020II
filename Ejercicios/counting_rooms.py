
#nota extra: no funciona con valores muy altos (por python)
def solucion():
    #n es el numero de filas y m es el numero de columnas 
    n , m = [int(x) for x in input().split()]
    
    #leemos la matriz
    matrix = [[] for x in range(n)]
    for i in range(n):
        matrix[i] = list(input())
    
    #creamos la matriz de los nodos visitados
    visitados = [[False for j in range(m)] for i in range(n)]
    
    #matriz[i][j] i es la fila y j es la columna
    def dfs(i , j):
        #print("Estoy en la posicion" , i , " " , j)
        visitados[i][j] = True
        if(i + 1 < n ):
            if( visitados[i + 1][j] == False and matrix[i + 1][j] == "."):
                #print("se cumple i + 1")
                dfs(i + 1 , j)
        if(i - 1 >= 0):
            if(visitados[i - 1][j] == False and matrix[i - 1][j] == "."):
                #print("se cumple i - 1")
                dfs(i - 1 , j)
        if(j + 1 < m):
            if(visitados[i][j + 1] == False and matrix[i][j + 1] == "."):
                #print("se cumple j + 1")
                dfs(i , j + 1)
        if(j - 1 >= 0):
            if(visitados[i][j - 1] == False and matrix[i][j - 1] == "."):
                #print("se cumple j- 1")
                dfs(i  , j - 1)
    
    #dfs(0 , 0)
    #print(matrix)
    #print(visitados)
    
    cantidad = 0
    for i in range(n):
        for j in range(m):
            if(visitados[i][j] == False and matrix[i][j] == "." ):
                dfs(i , j)
                cantidad += 1
    return cantidad
print(solucion()) 