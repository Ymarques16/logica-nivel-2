#28) Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.
print("Digite 3 valores DISTINTOS e veja a soma dos 2 maiores valores")
n1 = int(input("digite o primeiro valor:"))
n2 = int(input("digite o segundo valor:"))
n3 = int(input("digite o terceiro valor:"))

if n1 == n2 or n1 == n3 or n2 == n3:
    print("os valores devem ser distintos")
    
else: soma_dos_maiores = (n1+n2+n3) - min(n1,n2,n3)

print(f"a soma dos dois maiores valores é: {soma_dos_maiores}")
