################
# Juan Ignacio Bruni @Juanbruni
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def factorial(numero):
    if numero>=1:
 
        f=numero
        while numero>=2:
            numero=numero-1
            f=f*(numero)
        return f
    if numero==0:
        return 1
 
def prueba():
    mensaje="factoriones"
    
    numero=int(input(f"Ingrese numero: "))
    factorial(numero)
    print(f"El factorial es: {factorial(numero)}")

if __name__ == "__main__":
    prueba()

