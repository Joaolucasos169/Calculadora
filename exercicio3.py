#Somar
#Subtrair
#Dividir
#Multiplicar

#Essas funções recebem dois valores distintos e retornam o resultado de uma operação matemática

#Construa uma aplicação Calculadora que pede dois números e exibe um menu com as operações matemáticas mencionadas acima. 
#O programa deverá exibir o resultado da operação escolhida pelo usuário.
#O programa deverá repetir o processo até que o usuário digite 0 para encerrar.

def soma(num1, num2):
    return num1 + num2
        
def Subtrair(num1, num2):
    return num1 - num2
        
def divisao(num1, num2):   
    return num1 / num2        
        
def Multiplicar(num1, num2):     
    return num1 * num2        
         
while True:
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input('''Escolha uma operação:
    Somar (+)
    Subtrair (-)
    Dividir (/)
    Multiplicar (*)
    Sair (0)
    ''')       
    
    if (operacao == "+"):
        print("O valor da sua soma é", soma(num1, num2))

    elif (operacao == "-"):
        print("O valor da sua subtração é", Subtrair(num1, num2))

    elif (operacao == "/"):
        print("O valor da sua divisão é", divisao(num1, num2))

    elif (operacao == "*"):
        print("O valor da sua multiplicação é", Multiplicar(num1, num2))
        
    elif (operacao == "0"):
        print("Saindo...")
        break
    else:
        print("Operação inválida")
