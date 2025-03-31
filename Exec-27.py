print("escreva 3 números DISTINTOS e verá qual é maior!")
n1 = int(input("escreva o primeiro número:"))
n2 = int(input("escreva o segundo número:"))
n3 = int(input("escreva o terceiro número:"))

if n1 == n2 or n1 == n3 or n2 == n3:
    print("os valores devem ser distintos! escreva os valores novamente.")
else:
    maior = max(n1, n2, n3)
    print(f"o maior valor é: {maior}")
