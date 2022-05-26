import random
x = int(input("Quantas dezenas deseja apostar (De 6 a 15)? "))
for a in range(0,x):
 r = random.randint(1,60)
 print(f'{r}--',end = '')
 
