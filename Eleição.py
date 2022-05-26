c1= 0; c2= 0; c3= 0; null=0; v=0;
while(v != -1):
  v = int(input("Vote digitando o numero do candidato 1, 2 ou 3:"))
  if (v == 1):
    c1= c1 + 1
  elif (v == 2):
    c2= c2 + 1
  elif (v == 3):
    c3= c3 + 1
  elif (v != -1):
    null = null + 1
print("Eleição finalizada, o resultado é:")
print(f"Candidato 1: {c1} votos")
print(f"Candidato 2: {c2} votos")
print(f"Candidato 3: {c3} votos") 
print(f"Votos nulos: {null} votos")
if(c1 > c2 and c1 > c3):
  print("Candidato 1 venceu!")
elif(c2 > c1 and c2 > c3):
  print("Candidato 2 venceu!")
elif(c3 > c1 and c3 > c2):
  print("Candidato 3 venceu!")
else:
  print("Empate, te vejo no segundo turno ;) ")
