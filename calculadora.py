# este es el archivo python en el cual mis compañeros y yo trabajaremos para 
# crear una calculadora de manera colaborativa

def sumar(num1,num2):
    resultado=num1+num2
    return resultado
def restar(num1,num2):
    resultado = num1-num2
    return resultado
def multilicar(num1,num2):
    resultado = num1*num2
    return resultado

def division (num1,num2):
    try:
        resultado = num1/num2
        return resultado
    except ZeroDivisionError as e:
        print("no se púede dividir entre 0");