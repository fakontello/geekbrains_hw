# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


from math import sqrt


class Triangle:
    ab = 0
    xa = 1
    ya = 2
    xb = 3
    yb = -1
    xc = 2
    yc = 5
    bc = 0
    ac = 0
    h = 0
    p = 0
    s = 0

    def sides(self):
        self.ab = sqrt((self.xb - self.xa) ** 2 + (self.yb - self.ya) ** 2)
        self.bc = sqrt((self.xc - self.xb) ** 2 + (self.yc - self.yb) ** 2)
        self.ac = sqrt((self.xc - self.xa) ** 2 + (self.yc - self.ya) ** 2)
        print(self.ab, self.bc, self.ac)

    def height(self):
        self.p = 1/2 * (self.ab + self.bc + self.ac)
        self.h = 2*sqrt(self.p*(self.p - self.ab)*(self.p - self.bc)*(self.p - self.ac)) / self.ab
        print(self.h)

    def square(self):
        self.s = 1/2 * self.ab * self.h
        print(self.s)

    def perimeter(self):
        self.p = self.ab + self.bc + self.ac
        print(self.p)


triangle_sq = Triangle()
triangle_sq.sides()
triangle_sq.height()
triangle_sq.square()
triangle_sq.perimeter()
		

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

from math import sqrt as sq


class IsoscelesTrapezoid:

    c = 0
    d = 0
    a = 0
    b = 0
    h = 0
    s = 0

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def test(self):
        c = sq(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = sq(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))

        if c == d:
            print("Трапеция равнобокая")
        else:
            print("Трапеция неравнобокая")

    def side_lenght(self):
        c = sq(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = sq(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        a = sq(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        b = sq(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        print("Длина сторон: " + "\nAB: ", a, "\nBC: ", c, "\nCD: ", d, "\nDC: ", b)

    def height(self):
        h = 1/2 * sq(4 * self.c ** 2 - (self.a - self.b ** 2))
        print(h)

    def square(self):
        s = self.a + self.b / 4 * sq(4 * self.c ** 2 - (self.a - self.b ** 2))
        print(s)

    def perimeter(self):
        c = sq(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        d = sq(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        a = sq(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        b = sq(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        print(a + b + c + d)