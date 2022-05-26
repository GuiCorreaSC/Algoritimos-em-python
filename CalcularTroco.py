total = float(input("Digite o valor da compra: R$"))

n50 = int(input("Digite a quantidade de notas de R$50,00: "))
n20 = int(input("Digite a quantidade de notas de R$20,00: "))
n10 = int(input("Digite a quantidade de notas de R$10,00: "))
n5 = int(input("Digite a quantidade de notas de R$5,00: "))

entreg = (n50*50+n20*20+n10*10+n5*5)
troco = total-(n50*50+n20*20+n10*10+n5*5)
if total < entreg:
  print(f"Prezado cliente sua compra foi de R$ {total:.2f}, você entregou R$ {entreg:.2f} \n e seu troco é de R$ {troco:.2f}. ")
else:
  print("ta faltando dinheiro ainda burrao")
