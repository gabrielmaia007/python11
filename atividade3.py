print("========================================")
print("ACESSO AO CINEMA")
print("========================================")

idade = int(input("Digite sua idade: "))
carteirinha = input("Você tem carteirinha de estudante? (s/n): ")

if idade >= 12 and carteirinha == "s":
    print("Entrada permitida com meia-entrada!")
else:
    print("Entrada permitida somente com ingresso inteiro")

print("========================================")
print("FIM DO PROGRAMA")