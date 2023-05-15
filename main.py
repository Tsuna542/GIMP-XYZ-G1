def frame() :
  rows = 22
  columnas = 22

  for i in range(rows) :
    for j in range(columnas) :
      if i == 0 or i == (rows-1) or j == 0 or j == (columnas-1) :
        if i == 0 or i == (rows-1) :
          if j == 0 or j == (columnas-1) :
            print("      ", end='')
          else :
            print(f" {j}", end='')
        elif j == 0 or j == (columnas-1) :
          if i >= 10 :
            if j == columnas - 1 :
              print(f" {i}", end='')
            else :
              print(f"{i}", end='')
          else :
            print(f" {i}", end='')
      else :
        print(" ", end='  ')
    print()





def main() :
  initialize = "X"

  while not initialize == "init" :
    initialize = input("")

  print("Welcome to the GYMP XYZ of team 1 :D")

  frame()












if __name__ == "__main__" :
  main()