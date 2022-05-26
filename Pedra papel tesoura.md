import math
print("Cada Jogador escolhe seu simbolo utilizando o codigo a seguir: Pedra: r,Tesoura: t,Papel: p")
j1 = input("Jogador 1 digite p,t ou r: ")
j2 = input("Jogador 2 digite p,t ou r: ")
if j1 != 'p' or j1 != 'r' or j1 !='t' and j2 != 'p' or j2 != 'r' or j2 !='t':
  print("Voce digitou letras invalidas")
else:
  if j1 == 'r' and j2 == 't' or j1 == 't' and j2 == 'p' or j1 == 'p' and j2 == 'r':
   print("Jogador 1 venceu")
  elif j1 == 't' and j2 == 'r' or j1 == 'p' and j2 == 't' or j1 == 'r' and j2 == 'p':
    print("Jogador 2 venceu")
#elif j1 == 't' and j2 == 'p':
#  print("Jogador 1 venceu")
#elif j1 == 'p' and j2 == 't':
#  print("Jogador 2 venceu")
#elif j1 == 'p' and j2 == 'r':
#  print("Jogador 1 venceu")
#elif j1 == 'r' and j2 == 'p':
#  print("Jogador 2 venceu")
  elif j1 == j2:
   print("empate")
