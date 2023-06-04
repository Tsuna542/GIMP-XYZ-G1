def draw_line(Pi, Pf):
    x1, y1 = Pi
    x2, y2 = Pf

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dx == 0 and dy == 0:  # Los puntos son iguales
        print("No se puede representar una línea. Los puntos son iguales.")
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
        print("No se puede representar una línea recta.")

def main():
    try:
        x1, y1 = map(int, input("Ingrese las coordenadas del punto inicial (Pi): ").split(','))
        x2, y2 = map(int, input("Ingrese las coordenadas del punto final (Pf): ").split(','))

        Pi = (x1, y1)
        Pf = (x2, y2)

        draw_line(Pi, Pf)
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar números enteros separados por coma.")

if __name__ == "__main__":
    main()
