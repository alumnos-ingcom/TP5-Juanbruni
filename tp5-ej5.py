################
# Juan Ignacio Bruni - @Juanbruni
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio


def cadena (texto):
    lista_texto=list(texto)
    listacambiada=[]
    
    for letra in lista_texto:
        
        if letra.islower():
            
            listacambiada.append(letra.upper())

        elif letra.isupper():
            listacambiada.append(letra.lower())
            
    listacambiada="".join(listacambiada)
    return listacambiada

def prueba():
    texto=input("introduzca su texto ")
    print (cadena(texto))
  

if __name__ == "__main__":
    prueba()

