def dibujar_linea(Pi, Pf):
    x1, y1 = Pi
    x2, y2 = Pf

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dx == 0 and dy == 0:  # Los puntos son iguales
        print("Invalid Operation")
    elif dx == 0:  # La línea es vertical
        for y in range(min(y1, y2), max(y1, y2) + 1):
            print("*")
    elif dy == 0:  # La línea es horizontal
        print("*" * (dx + 1))
    elif dx == dy:  # La línea es diagonal
        for i in range(dx + 1):
            if x1 < x2 and y1 < y2:
                print(" " * i + "*")
            elif x1 > x2 and y1 > y2:
                print(" " * (dx - i) + "*")
            elif x1 < x2 and y1 > y2:
                print(" " * (dx - i) + "*")
            elif x1 > x2 and y1 < y2:
                print(" " * i + "*")
    else:  # La línea no es recta
        print("Invalid Operation")

def main():
    try: # Solicitar datos
        x1, y1 = map(int, input("Puntos Iniciales (Pi): ").split(','))
        x2, y2 = map(int, input("Puntos Finales (Pf): ").split(','))

        Pi = (x1, y1)
        Pf = (x2, y2)

        dibujar_linea(Pi, Pf)
    except ValueError:
        print("Invalid Operation")

if __name__ == "__main__":
    main()
