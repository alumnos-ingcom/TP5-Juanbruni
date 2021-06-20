################
# Juan Ignacio Bruni - @Juanbruni
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def capicua(num):
    un_numero = num
    if un_numero>=10000:
        return 1
    if un_numero<10000 and (un_numero-un_numero%100)//100==un_numero%10:
        return 2
    if un_numero<10000 and (un_numero-un_numero%100)//100!=un_numero%10:
        return 3
def prueba():
    num=int (input ('Ingresa el valor de un numero: '))
    capicua(num)
    resultado=capicua(num)
    if resultado==1:
        print (f"El numero {num} tiene mas de 3 digitos.")
    elif resultado==2:
        print (f'El numero {num} si es capicua.')
    elif resultado==3:
        print (f"El numero {num} no es capicua.")
        
if __name__ == "__main__":
    prueba()

