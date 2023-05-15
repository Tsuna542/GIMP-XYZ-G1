# Codigo Referencial de un rectangulo basico

rows = int(input("Numero de filas: "))
columnas = int(input("Numero de columnas: "))

for i in range(rows) :
  for j in range(columnas) :
    if i == 0 or i == (rows-1) or j == 0 or j == (columnas-1) :
      print("*", end='')
    else :
      print(" ", end='')
  print()