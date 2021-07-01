################
# Juan Ignacio Bruni @Juanbruni
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def comparar(lista1,lista2):
    lista1.sort()
    lista2.sort()
    if lista1==lista2:
        return True
    else:
        return False
    
def prueba():
    mensaje="comparación de listas"
    
    
    lista1=[]
    lista2=[]
    ingreso1=0
    ingreso2=0
    
    while ingreso1 != "":
        ingreso1=input("Ingrese contenido de la lista 1: ")
        lista1.append(ingreso1)
    else:
        lista1.pop()
    
    while ingreso2 != "":
        ingreso2=input("Ingrese contenido de la lista 2: ")
        lista2.append(ingreso2)
    else:
        lista2.pop()
    
    comparar(lista1, lista2)
    
    resultado=comparar(lista1,lista2)
    if resultado==True:
        print(f"{resultado}")
    else:
        print(f"{resultado}")
    


if __name__ == "__main__":
    prueba()
    

