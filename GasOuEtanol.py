import math
eta = float(input("Digite o preço do etanol: "))
gas = float(input("Digite o preço da gasolina: "))

calc = (eta/gas)*100

print(f"O preço do etanol está {calc:.2f}% do preço da gasolina!")

if calc > 70:
  print("Abasteça com gasolina")
else:
  print("Abasteça com etanol")
