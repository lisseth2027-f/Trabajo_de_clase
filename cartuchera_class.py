class Cartuchera:
    def __init__(self, color, forma):
        self.color = color
        self.forma = forma

    def saludar(self):
        print(f"Hola, busco cartuchera de color {self.color} y es {self.forma}")