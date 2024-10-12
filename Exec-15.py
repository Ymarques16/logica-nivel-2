num_macas = int(input("Digite o número de maçãs compradas: "))

if num_macas < 12:
    preco_por_maca = 1.30
else:
    preco_por_maca = 1.00

custo_total = num_macas * preco_por_maca

print(f"O custo total da compra é: R$ {custo_total:.2f}")
