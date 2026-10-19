import math

def es_primo(numero):
    raiz_cuadrada = int(math.sqrt(numero))
    
    for i in range(2, raiz_cuadrada+1):
        if numero % i ==  0:
            return False       
    return True
  
def run():

    numero = int(input('Ingresa un número entero: '))
    if es_primo(numero):
        print(str(numero) + ' es un número primo')
    else:
        print(str(numero) + ' no es un número primo')

if __name__ == '__main__':
        run()
```
