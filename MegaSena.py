import random

n = int(input("Quantas dezenas deseja sortear?"))
print("Sorteei para você os seguintes números.")

sorteio = [] # cria uma lista para essa variavel

for i in range(0,n): # limita os numeros de inicio a fim
  x = random.randint(1,60) # escolhe um numero random a cada fez que o range rodar
  sorteio.append(x) # adiciona o numero sorteado na variavel 

print(sorted(sorteio)) # sorted ordena os numeros do menor pro maior
