# este es el archivo python en el cual mis compañeros y yo trabajaremos para 
# crear una calculadora de manera colaborativa


def sumar(num1,num2):
    resultado=num1+num2
    return resultado
def restar(num1,num2):
    resultado = num1-num2
    return resultado
def multiplicar(num1,num2):
    resultado = num1*num2
    return resultado

def division (num1,num2):
        resultado = num1/num2
        return resultado
    

while True:
    numero1 = int(input("Ingrese el primer numero: "));
    op = int(input("Ingrese la accion que desea realizar \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir\n "));
    numero2 = int(input("Ingrese el segundo numero: "));
    if op == 1:
        print(sumar(numero1,numero2))
    if op == 2:
        print(restar(numero1,numero2))
    if op == 3:
        print(multiplicar(numero1,numero2))
    if op == 4:
        try:
            print(division(numero1,numero2))
        except ZeroDivisionError as e:
            print("no se púede dividir entre 0");
    menu = str(input("¿Desea continuar?(S/N)"))
    if menu.upper() == "S":
        continue
    else:
        break
print("Adios")
