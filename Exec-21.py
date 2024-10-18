horas = int(input("quantas horas regulares foram trabalhadas?"))
horasExtra = int(input("quantas horas extra foram trabalhadas?"))
horasDeTrabalho = horas
valorPorHora =35.45
extra = 17.725*horasExtra

if horasExtra >= 1:
    resultado = valorPorHora*horas+extra
    print("O salário atual será:", resultado)
else:
    print("o salário total será:", valorPorHora*horasDeTrabalho)
