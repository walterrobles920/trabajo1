def factorial_normal(n):
    r=1
    i=2




def factorial_recursivo(n):
     if n == 1:
            return 1
     else:
         return n* factorial_recursivo(n-1) 

valor = factorial_recursivo(5)
print(f"el factorial de 5! es: {valor}")