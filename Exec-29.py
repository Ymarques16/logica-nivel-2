INACABADO
#30) Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.
print ("escreva 3 valores DIFERERNTES e será escrito em ordem crescente")
n1 = int(input("escreva o primeiro valor:"))
n2 = int(input("escreva o segundo valor:"))
n3 = int(input("escreva o terceiro valor:"))

if n1 == n2 or n1 == n3 or n2 == n3:
    print("os valores devem ser distintos")
    
else:
    numeros = [n1, n2, n3]
    numeros.sort()
print("os numeros em ordem crescente são:" numeros)
