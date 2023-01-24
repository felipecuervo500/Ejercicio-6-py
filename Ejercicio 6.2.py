class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def status(self):
        if self.nota < 6:
            print(f"{self.nombre} ha reprobado la materia")
        else:
            print(f"{self.nombre} ha aprobado la materia")

if __name__ == "__main__":
    alumno1 = Alumno("Elvira", 7.5)
    alumno2 = Alumno("Eduardo", 5.8)
    alumno1.mostrar()
    alumno1.status()
    alumno2.mostrar()
    alumno2.status()
    