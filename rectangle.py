class Rectangle():
    pass 
    def area(self):
        return self.width * self.height

rect1 = Rectangle()
rect1.width = int(input('entrez la largeur du rectangle : '))
rect1.height = int(input('entrez la longueur du rectangle : '))
print(f"L'aire du rectangle est égale à {rect1.area()}")
