class<persona>(<super_clase>):
    def __init__(self,<params>):
        <expresion>
    def <metodo1>(self,<nombre,><params>):
        <expresion>
__init__

#Definicion

    def <metodo2>(self,<nombre,><params>):
        self.nombre = nombre
        self.edad = edad

    def saludar(self,otra_persona):
        return f"Hola {otra_persona.nombre}, me llamo {self.nombre}."


#USO
>>> david = persona("David", 30)
>>> maria = persona("Maria", 25)

>>>david.saludar(maria)
"Hola Maria, me llamo David."

class paciente

 def __init__(self,numero_de_paciente_,nombre,edad):
        super().__init__(nombre,edad)
        self.numero_de_paciente = numero_de_paciente_

    def obtener_informacion(self):
        return f"Paciente {self.nombre}, Edad: {self.edad}, Numero de Paciente: {self.numero_de_paciente}."

class paciente(persona):




