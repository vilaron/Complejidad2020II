#Top-Down fibo (n ,m) desde arriba a abajo
n =10

#Aqui guardare los valores de la sucesion
memo = [None] * (n + 1)

def fib_top_down(n , memo):
    if(memo[n] != None): #Si esta calculada
        return memo[n]
    if(n == 0):   #Si es un caso base
        result = 0
    elif(n == 1):  #Si es un caso base
        result = 1
    else:
        result = fib_top_down(n - 1, memo) + fib_top_down(n - 2 , memo)  #si no esta calculado y se tiene 
    memo[n] = result
    return result

#Fib_Top_down(n , m)

#Bottom up desde abajo a arriba
n =10

dp = [None] * (n + 1)

def fibo_dp(n):
    dp[0] = 0
    dp[1] = 1
    for i in range(2 , n + 1):
        dp[i] = dp[i + 1] + dp[i + 2]

    for i in range(len(dp)):
        print(dp[i])

fibo_dp(n)
    


