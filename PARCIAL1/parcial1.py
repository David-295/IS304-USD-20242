'''
Escribir un programa en Python que permita clasificar triángulos (isósceles, escaleno, equilatero, rectángulo) a partir de tres valores float o double ingresados desde el teclado.
Definir y utilizar al menos una referencia de herencia que incluya encapsulamiento.
El programa debe repetirse contínuamente hasta que uno de los supuetos triángulos no lo sea.
'''
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self._lado1 = lado1 #Aquí hay encapsulamiento
        self._lado2 = lado2
        self._lado3 = lado3

    def es_valido(self):
        return (self._lado1 + self._lado2 > self._lado3 and
                self._lado1 + self._lado3 > self._lado2 and
                self._lado2 + self._lado3 > self._lado1)

class ClasificadorTriangulos(Triangulo): #Aquí hay herencia, hereda de la clase Triángulo 
    def __init__(self, lado1, lado2, lado3):
        super().__init__(lado1, lado2, lado3)

    def clasificar(self):
        if not self.es_valido():
            return "No es un triángulo válido"

        if self._lado1 == self._lado2 == self._lado3:
            return "Equilátero"
        elif self._lado1 == self._lado2 or self._lado1 == self._lado3 or self._lado2 == self._lado3:
            tipo = "Isósceles"
        else:
            tipo = "Escaleno"

        if self.es_rectangulo():
            tipo += " y Rectángulo"

        return tipo

    def es_rectangulo(self):
        lados = sorted([self._lado1, self._lado2, self._lado3])
        return round(lados[0]**2 + lados[1]**2, 5) == round(lados[2]**2, 5)

def main():
    while True:
        try:
            lado1 = float(input("Ingrese el primer lado del triángulo: "))
            lado2 = float(input("Ingrese el segundo lado del triángulo: "))
            lado3 = float(input("Ingrese el tercer lado del triángulo: "))

            triangulo = ClasificadorTriangulos(lado1, lado2, lado3)
            tipo = triangulo.clasificar()

            if tipo == "No es un triángulo válido":
                print(tipo)
                break

            print(f"El triángulo es: {tipo}")
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()


