# Declare a class named Complex to represent and work with complex numbers.
# Objects of this class must be created with the command:
#
# cm = Complex(real, img)
#
# where real is the real part of the complex number (integer or real value);
# img - imaginary part of a complex number (integer or real value).
#
# Declare the following property objects in this class:
#
# real - for writing and reading a real value;
# img - for writing and reading an imaginary value.
#
# When writing new values, it is necessary to check the type of the transmitted data. If the type does not correspond
# to an integer or a real number, then throw an exception with the command:
#
# raise ValueError('Invalid data type.')
#
# Also, with objects of the Complex class, the following function should be supported:
#
# res = abs(cm)
#
# returning the modulus of a complex number (calculated by the formula: sqrt(real*real + img*img) -
# the square root of the sum of the squares of the real and imaginary parts of the complex number).
#
# Create a cmp object of the Complex class for a complex number with real = 7 and img = 8. Then, through the real and
# img property objects, change these values ​​to real = 3 and img = 4. Calculate the modulus
# of the resulting complex number (save the result in the c_abs variable) .


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __check(self, numeric):
        if type(numeric) in (float, int):
            return numeric
        else:
            raise ValueError("Invalid data type.")

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.__check(value)
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.__check(value)
        self.__img = value

    def __abs__(self):
        return (self.real*self.real + self.img*self.img) ** 0.5


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)
