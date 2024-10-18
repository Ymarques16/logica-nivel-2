horaInicio = int(input("Em que horário a partida iniciou?"))
horaFinal = int(input("Em que horário a partida terminou?"))

if horaFinal < horaInicio:
    horaParcial1 = 24 - horaInicio
    resultado = horaParcial1 + horaFinal
    print(resultado)
else:
   print("A partida durou:", horaFinal-horaInicio)
