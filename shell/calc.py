#!usr/bin/python3
import sys
def calc_usage():
    print ("The input is 3 or None")
def calc(num1,oper,num2):
    if oper == "+":
        return int(num1) + int(num2)
    if oper == "-":
        return int(num1) - int(num2)
    if oper == "*":
        return int(num1) * int(num2)
    if oper == "/":
        return int(num1) / int(num2)
def no_argv():
    print("Calculadora sovietica      0.1",end="\n")
    print("Ingrese el Primer Numero\nRespuesta:  ",end="")
    num1 = int (input())
    print ("Ingrese el segundo numero\nRespuesta:  ",end="")
    num2 = int (input())
    print ("Ingrese operacion\n1-Suma\n2-Resta\n3-Multiplicacion\n4-Division\nRespuesta:  ",end="")
    oper = int (input())
    if oper == 1:
        print (num1+num2)
    elif oper == 2:
        print (num1-num2)
    elif oper == 3:
        print (num1*num2)
    elif oper == 4:
        print (num1/num2)
        
    else:
        print ("Error al optener operador")
        sys.exit(1)
    
def main(num1,oper,num2):
    print ("The result is: ", end="")
    result = calc(num1,oper,num2)
    print (result)

if __name__ == "__main__":
    asd = len(sys.argv) 
    if  asd == 1:
        no_argv()
    elif asd == 4:
        main(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        calc_usage()
