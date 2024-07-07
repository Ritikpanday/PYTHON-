class Complex:
    def __init__(self, real_part, imag_part):
        self.real = real_part
        self.img = imag_part

    def __repr__(self):
        return f'Complex({self.real}, {self.img})'

    def __str__(self):
        return f'{self.real} + i{self.img}'


x = Complex(2, 5)
print(str(x))
print(repr(x))


class Cat:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def __repr__(self):
        return "Cat, breed: sphynx, name: Kitty"

    def __str__(self):
        return "My sphynx cat's name is Kitty"


lucy = Cat('siamese', 'Lucy')
print(str(lucy))
print(repr(lucy))
