class Piramide:

    def __init__(self, pisos=5):
        self.piramide = [[True for i in range(nivel + 1)] for nivel in range(pisos)]

    def __repr__(self):
        return '\n'.join(str(fila) for fila in self.piramide)

    def esta_tachado(self, nivel, posicion):
        return self.piramide[nivel][posicion] == False

    def tachar_palito(self, nivel, posicion):
        self.piramide[nivel][posicion] = False

    def tachar_palitos(self, nivel, desde, hasta):
        if any(self.esta_tachado(nivel, x) for x in range(desde, hasta+1)):
            raise ValueError(f"Ya hay un palito tachado en el rango en el nivel {nivel}")

        for posicion in range(desde, hasta+1):
            self.tachar_palito(nivel, posicion)


if __name__ == '__main__':
    piramide = Piramide()

    print(piramide)
