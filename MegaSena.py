import random

n = int(input("Quantas dezenas deseja sortear?"))
print("Sorteei para você os seguintes números.")

sorteio = []

for i in range(0,n):
  x = random.randint(1,60)
  while x not in sorteio: # enquanto x nao estiver na variavel ele adiciona 
    x = random.randint(1,60)
    sorteio.append(x)

print(sorted(sorteio))
