#Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa de R$ 700,00 para cada carro vendido e mais 5% do valor das vendas por 
#ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o saláriofixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor. 

salarioFixo = int(input("Qual o salário fixo do vendedor? "))
comissaoFixo = 700
quantidadeCarrosVendidos = int(input("Quantos carros foram vendidos? "))
totalComissaoFixo = comissaoFixo * quantidadeCarrosVendidos

salarioSemComissao = float(salarioFixo + totalComissaoFixo)
adicional_5 = salarioSemComissao * 0.05
salarioFinal = salarioSemComissao + adicional_5

print("O salário final do vendedor é: ", salarioFinal)
