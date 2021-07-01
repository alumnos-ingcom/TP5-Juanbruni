################
# Juan Ignacio Bruni @Juanbruni
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
    

def balanceo(cadena_de_parentesis):
    
    aperturas = 0
    
    balanceo = True

    for caracter in cadena_de_parentesis:
        
        if aperturas >= 0:
        
            if caracter == "[" or caracter == "{" or caracter == "(" :
        
                aperturas = aperturas + 1
        
            elif caracter == "]" or caracter == "}" or caracter == ")" :
        
                aperturas = aperturas - 1
            
        elif aperturas < 0:
            
            balanceo = False
    
    if aperturas > 0:
        
        balanceo = False
        
    return balanceo
            
    

def prueba():
    testeo = input("ingrese una cadena con parentesis \n")
    
    haver = balanceo(testeo)
    
    if haver:
        print(f"la lista {testeo} esta balanceada")
    
    elif not haver:
        print(f"la lista {testeo} no esta balanceada")
        
    
if __name__ == "__main__":
    prueba()

