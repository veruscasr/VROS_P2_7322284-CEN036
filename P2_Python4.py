#!usr/bin/env python3

contador = 10
total = 0

i = 1
while i <= contador:
  nota = float(input("Nota " + str(i) + ": "))
  total += nota
  i+=1
  
print("Média: " + str(total/contador))
