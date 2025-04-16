string = input("Digite a string: ")
caracter = input("Digite o caracter: ")

if len(caracter) != 1:
    print("Por favor, insira apenas um único caracter.")
else:
    
    indice = string.find(caracter)
    
    
    print(indice)