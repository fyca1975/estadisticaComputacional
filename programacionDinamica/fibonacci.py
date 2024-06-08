

# solucion de fibonacci con recursividad solo funciona para numeros pequeños
# con numeros grandes se demora demasiado
import sys


def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1 
    
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n -2)


# Esta solucion la genera super rapido, en programacion dinamica se cambia tiempo por espacio de maquina  
def fibonnacci_dinamico(n, memo= {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        resultado = fibonnacci_dinamico(n - 1, memo) + fibonnacci_dinamico(n -2, memo )
        memo[n] = resultado

        return resultado


if __name__ == '__main__':
        # para evitar el maximo de recursos se puede manejar importando sys
        sys.setrecursionlimit(10002)
        n = int(input('Escoge un numero  -> '))
        #resultado = fibonacci_recursivo(n)
        resultado = fibonnacci_dinamico(n)
        print(resultado)