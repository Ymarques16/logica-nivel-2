numero_da_conta = float(input("Digite o número da sua conta bancária:"))
saldo = float(input("Digite seu saldo atual:"))
debito  = float(input("Digite o saldo DEVEDOR:"))
credito = float(input("Digite quanto é seu crédito:"))
resultado = saldo-debito+credito

if resultado <=0:
   print("O seu saldo está negativo. Economize!")
   
else:
    print("O seu saldo está positivo. Parabéns!")
