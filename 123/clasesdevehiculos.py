#Crear clase persona
class Vehiculo:
    #Constructor
    def __init__(self, marca,modelo, color, placa,año, tipo, combustible):
        #Atributos
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.placa = placa
        self.año = 2024
        self.tipo = "Sedan"
        self.combustible = "diesel"

    

    #Metodo para mostrar datos
    def mostrar_datos(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color} Placa: {self.placa} año: {self.año}, tipo: {self.tipo} Combustible: {self.combustible}")

    def caracteristicas(self):
        print(f"el vehiculo es de marca {self.marca}, y modelo {self.modelo}, con un color {self.color} y placa {self.placa} de año {self.año} y tipo {self.tipo} y combustible {self.combustible}")



#Llamar clase
Toyota = Vehiculo("Toyota", "hilux", "Rojo", "ABC123",2022, "Camioneta", "Gasolina")
honda = Vehiculo("Honda", "Civic", "Azul", "XYZ789",2020, "Sedan", "Gasolina")
#Llamar metodos
Toyota.mostrar_datos()
Toyota.caracteristicas()
honda.mostrar_datos()
honda.caracteristicas()

