################
# Juan Ignacio Bruni @Juanbruni
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def distancia(valorA, valorB):
    distanciaAB=valorB-valorA
    if distanciaAB<0:
        distanciaAB=distanciaAB*-1
    else:
        pass
    return distanciaAB

def prueba():
    mensaje="Distancias"
    
    valorA=float(input("Ingrese valor A: "))
    valorB=float(input("Ingrese valor B: "))
    distancia(valorA,valorB)
    print(f"La distancia entre {valorA} y {valorB} es:  {distancia(valorA, valorB)}")

if __name__ == "__main__":
    prueba()

