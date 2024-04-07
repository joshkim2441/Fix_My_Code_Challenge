#!/usr/bin/python3

class square():
    """ Square class """
    width = 0
    height = 0


    def __init__(self, *args, **kwargs):
        """ Initialize the Square class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of the Square instance """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create the square instance """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
