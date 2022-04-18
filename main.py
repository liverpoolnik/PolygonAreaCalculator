class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        # Rectangle(width=5, height=10)
        rectangle = f"Rectangle(width={self.width}, height={self.height})"
        return rectangle

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        c = '*' * self.width
        picture = ''
        if self.width > 50 or self.height > 50:
            picture = "Too big for picture."
            return picture
        else:
            for _ in range(self.height):
                picture += c + '\n'
            return picture

    def get_amount_inside(self, o):
        amount_inside = self.get_area() // o.get_area()
        return amount_inside


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        Rectangle.width = self.side
        Rectangle.height = self.side

    def __str__(self):
        # Square(side=9)
        square = f"Square(side={self.side})"
        return square

    def set_width(self, width):
        self.side = width
        Rectangle.width = width
        Rectangle.height = width

    def set_height(self, height):
        self.side = height
        Rectangle.width = height
        Rectangle.height = height

    def set_side(self, side):
        self.side = side
        Rectangle.width = self.side
        Rectangle.height = self.side


# Starter code by nik

rect = Rectangle(8, 4)
print(rect)
print(rect.get_diagonal())
sq = Square(9)
sq.set_side(2)
sq.set_width(4)
print(rect.get_amount_inside(sq))
