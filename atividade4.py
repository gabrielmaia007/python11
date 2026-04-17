print("========================================")
print("PROMOÇÃO - FRETE GRÁTIS")
print("========================================")

valor = float(input("Digite o valor da compra: R$ "))
vip = input("Você é cliente VIP? (s/n): ")

if valor > 100 or vip == "s":
    print("Parabéns! Você ganhou FRETE GRÁTIS!")
else:
    print("Você não tem direito ao frete grátis.")

print("========================================")
print("FIM DO PROGRAMA")