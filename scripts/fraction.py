class Fraction:
    def __init__(self, num, denom):
        self.num = num
        if denom == 0:
            raise ValueError("Fractions can't have a denominator of zero")
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __sub__(self, other):
        new_num = self.num * other.denom - other.num * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __truediv__(self, other):
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        return Fraction(new_num, new_denom)

    def __float__(self):
        return self.num / self.denom

    def reciprocal(self):
        return Fraction(self.denom, self.num)

    def reduce(self):
        if self.denom == 1:
            return self.num

        def gcd(a, b):
            while b != 0:
                b, a = a % b, b
            return a

        GCD = gcd(self.num, self.denom)
        new_num = self.num // GCD
        new_denom = self.denom // GCD
        return Fraction(new_num, new_denom)
