def main():
    
    n = int(input("Digite a quantidade de números inteiros que você deseja inserir: "))
    
    
    numeros = []
    
    
    for i in range(n):
        numero = int(input(f"Digite o {i + 1}º número: "))
        numeros.append(numero)
    
    
    print("\nNúmeros na ordem inversa:")
    for numero in reversed(numeros):
        print(numero)
    
    
    numeros.sort(reverse=True)
    print("\nNúmeros em ordem decrescente:")
    for numero in numeros:
        print(numero)


if __name__ == "__main__":
    main()