def ordenar_numeros(num1, num2, num3): 
    
    numeros = [num1, num2, num3]
    
    numeros.sort()

    print("Números em ordem crescente:", numeros)


try:
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))
    numero3 = int(input("Digite o terceiro número inteiro: "))
    
    
    ordenar_numeros(numero1, numero2, numero3)
except ValueError:
    print("Por favor, insira apenas números inteiros.")