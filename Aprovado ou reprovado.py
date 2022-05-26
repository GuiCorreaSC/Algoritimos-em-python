import math
n1 = float(input("Digite a nota da primeira prova:"))
n2 = float(input("Digite a nota da primeira prova:"))
n3 = float(input("Digite a nota da primeira prova:"))

calc = (n1+n2+n3)/3
print(f"Sua média foi de: {calc:.1f}")
if calc > 70:
  print("Você foi aprovado!")
else:
  print("Você foi reprovado!")
