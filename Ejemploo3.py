
def area_rectangulo(a, b):
    result = a * b
    return result

def area_triangulo(b, h):
    r = 0.5 * b * h
    return r


def principal():
    dato1 = 4
    dato2 = 6

    print("Área del rectángulo:", area_rectangulo(dato1, dato2))

    base = 5
    altura = 8

    print("Área del triángulo:", area_triangulo(base, altura))

principal()
