################
# Juan Ignacio Bruni @Juanbruni
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def largo_texto(texto):
    largo_texto=len(texto)
    return largo_texto
    
def cesar(texto):
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    num=["0","1","2","3","4","5","6","7","8","9"]
    texto_cif=texto
    largo_texto=len(texto)
    contador=0
    j=0
    for i in (0,largo_texto):
        if texto_cif:
                print("Texto encontrado")
                    
    
def prueba():
    mensaje="César"
    
    texto=input("Ingrese el texto que desea cifrar: ")
    largo_texto(texto)
    texto_len=largo_texto(texto)
    
    cesar(texto)
    print(f"El texto ingresado es: {texto}")
    print(f"Largo del texto es: {texto_len}")
    
if __name__ == "__main__":
    prueba()