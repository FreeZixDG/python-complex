from math import sqrt, atan2, cos, sin


class Complex:
    def __init__(self, rel, img):
        self._rel = rel
        self._img = img

    def imag(self):
        return self._img

    def reel(self):
        return self._rel

    def __eq__(self, other):
        return self._rel == other.reel() and self._img == other.imag()

    def __add__(self, other):
        return Complex(self._rel + other.reel(), self._img + other.imag())

    def __sub__(self, other):
        return Complex(self._rel - other.reel(), self._img - other.imag())

    def __mul__(self, other):
        return Complex(self._rel * other.reel() - self._img * other.imag(),
                       self._img * other.reel() + self._rel * other.imag())

    def norm(self):
        return sqrt(self._rel ** 2 + self._img ** 2)

    def conjugate(self):
        return Complex(self._rel, -self._img)

    def arg(self):
        return atan2(self._img, self._rel)

    def __pow__(self, power, modulo=None):
        return Complex(self.norm() ** power * cos(power * self.arg()), self.norm() ** power * sin(power * self.arg()))

    def __repr__(self):
        a = "%.15g" % round(self._rel, 15)
        b = "%.15g" % round(self._img, 15)

        return f"({a}{'+' if float(b) >= 0 else ''}{b}i)"


if __name__ == '__main__':
    z = Complex(0, 1)
    z_c = complex(0, 1)

    a = Complex(9., -5.)
    a_c = complex(9, -5)

    print(z ** 2)

    print(a ** 2)
    print(a_c ** 2)

    print(Complex(45., 12.) ** 48)
    print((45. + 12.j) ** 48)
