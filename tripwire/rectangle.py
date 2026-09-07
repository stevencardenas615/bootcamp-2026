class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
   
    def area(self):
        return self.width * self.height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width has to be greater than 0")
        self._width = value

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height has to be greater than 0")
        self._height = value

def main():
    first_rectangle = Rectangle(5, 10)
    print(f"Area: {first_rectangle.area()}")

if __name__ == "__main__":
    main()
    