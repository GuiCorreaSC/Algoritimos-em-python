s0 = float(input("Digite a posição inicial: "))
v = float(input("Digite a velocidade:"))
print("Tabela posição x tempo para este móvel")
print("Tempo(s)---Posição(m)")
for t in range(0,26):
  print(f'{t:<8.2f}---{s0 + v*t:<10.2f}') #s = s0 + v*t
