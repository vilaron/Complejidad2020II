#fibonacci con programacion dinamica

#F es un arreglo
def fibo(n: int):
    t = [-1] * (n + 1) #Desde 0 hasta n hay n + 1 elementos
    def f(n: int):
        #si n es uno o cero
        if( n < 2 ):
            t[0] = 0
            t[1] = 1
        else:
            f(n - 1)
            t[n] = t[n - 1] + t[n -2]
    
    f(n)
    return t[n]
            