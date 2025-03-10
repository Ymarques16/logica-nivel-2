quantidade_estoque = int(input("Quantos itens têm no estoque?"))
maximo_do_produto = 100
minimo_do_produto = 20
quantidade_media_necessaria = (maximo_do_produto+minimo_do_produto)/2

if quantidade_estoque >= quantidade_media_necessaria:
    print("NÃO EFETUAR COMPRA!")
elif quantidade_estoque <=20:
    print("REPOR ESTOQUE URGENTEMENTE!")
    
else:
    print("EFETUAR COMPRA")
