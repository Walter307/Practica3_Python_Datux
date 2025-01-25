# Realice un programa que pueda gestionar tickets de buses
# las clases a usar seran buses  , conductores
# 1. Un menu iteractivo con las siguiente opciones: agregar bus , agregar ruta a bus, 
# registrar horario a bus, agregar conductor , agregar horario a conductor(*) y asignar bus a conductor(**)
# (*) consideremos que el horario de los conductores solo es a nivel de horas mas no dias ni fechas
# (**) validar que no haya conductores en ese horario ya asignados

### SOLUCIÓN

class Conductor:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.horarios = []  # Lista de horarios asignados al conductor

    def asignar_horario(self, horario):
        if not self._validar_horario(horario):
            raise ValueError("El horario ingresado no es válido. Debe estar en el formato HH:MM y dentro del rango 00:00 a 23:59.")
        if horario in self.horarios:
            raise ValueError("El horario ya está asignado a este conductor.")
        self.horarios.append(horario)

    def _validar_horario(self, horario):
        try:
            horas, minutos = map(int, horario.split(':'))
            return 0 <= horas < 24 and 0 <= minutos < 60
        except ValueError:
            return False

    def __str__(self):
        return f"Conductor: {self.nombre}, Cédula: {self.cedula}, Horarios: {self.horarios}"

class Bus:
    def __init__(self, id_bus, capacidad):
        self.id_bus = id_bus
        self.capacidad = capacidad
        self.ruta = None
        self.horarios = []  # Lista de horarios del bus
        self.conductor_asignado = None

    def asignar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, horario):
        if not self._validar_horario(horario):
            raise ValueError("El horario ingresado no es válido. Debe estar en el formato HH:MM y dentro del rango 00:00 a 23:59.")
        if horario in self.horarios:
            raise ValueError("El horario ya está registrado para este bus.")
        self.horarios.append(horario)

    def _validar_horario(self, horario):
        try:
            horas, minutos = map(int, horario.split(':'))
            return 0 <= horas < 24 and 0 <= minutos < 60
        except ValueError:
            return False

    def asignar_conductor(self, conductor, horario):
        if horario not in self.horarios:
            raise ValueError("El horario no está registrado para este bus.")
        if conductor.horarios.count(horario) > 0:
            raise ValueError("Este conductor ya está asignado en este horario.")

        self.conductor_asignado = conductor
        conductor.asignar_horario(horario)

    def __str__(self):
        return f"Bus: {self.id_bus}, Capacidad: {self.capacidad}, Ruta: {self.ruta}, Horarios: {self.horarios}, Conductor: {self.conductor_asignado.nombre if self.conductor_asignado else 'Ninguno'}"

class Admin:
    def __init__(self):
        self.conductores = []
        self.buses = []

    def agregar_conductor(self, nombre, cedula):
        for conductor in self.conductores:
            if conductor.cedula == cedula:
                raise ValueError("Ya existe un conductor con esta cédula.")
        nuevo_conductor = Conductor(nombre, cedula)
        self.conductores.append(nuevo_conductor)

    def agregar_bus(self, id_bus, capacidad):
        for bus in self.buses:
            if bus.id_bus == id_bus:
                raise ValueError("Ya existe un bus con este ID.")
        nuevo_bus = Bus(id_bus, capacidad)
        self.buses.append(nuevo_bus)

    def asignar_ruta_a_bus(self, id_bus, ruta):
        bus = self._buscar_bus(id_bus)
        bus.asignar_ruta(ruta)

    def registrar_horario_a_bus(self, id_bus, horario):
        bus = self._buscar_bus(id_bus)
        bus.registrar_horario(horario)

    def asignar_horario_a_conductor(self, cedula, horario):
        conductor = self._buscar_conductor(cedula)
        conductor.asignar_horario(horario)

    def asignar_bus_a_conductor(self, id_bus, cedula, horario):
        bus = self._buscar_bus(id_bus)
        conductor = self._buscar_conductor(cedula)
        bus.asignar_conductor(conductor, horario)

    def _buscar_conductor(self, cedula):
        for conductor in self.conductores:
            if conductor.cedula == cedula:
                return conductor
        raise ValueError("No se encontró un conductor con esta cédula.")

    def _buscar_bus(self, id_bus):
        for bus in self.buses:
            if bus.id_bus == id_bus:
                return bus
        raise ValueError("No se encontró un bus con este ID.")

    def mostrar_buses(self):
        return "\n".join(str(bus) for bus in self.buses)

    def mostrar_conductores(self):
        return "\n".join(str(conductor) for conductor in self.conductores)

def menu():
    admin = Admin()
    while True:
        print("\nMenú:")
        print("1. Agregar bus")
        print("2. Agregar ruta a bus")
        print("3. Registrar horario a bus")
        print("4. Agregar conductor")
        print("5. Asignar horario a conductor")
        print("6. Asignar bus a conductor")
        print("7. Mostrar buses")
        print("8. Mostrar conductores")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_bus = input("Ingrese el ID del bus: ")
                capacidad = int(input("Ingrese la capacidad del bus: "))
                admin.agregar_bus(id_bus, capacidad)
                print("Bus agregado correctamente.")

            elif opcion == "2":
                id_bus = input("Ingrese el ID del bus: ")
                ruta = input("Ingrese la ruta del bus: ")
                admin.asignar_ruta_a_bus(id_bus, ruta)
                print("Ruta asignada correctamente.")

            elif opcion == "3":
                id_bus = input("Ingrese el ID del bus: ")
                horario = input("Ingrese el horario (formato HH:MM): ")
                admin.registrar_horario_a_bus(id_bus, horario)
                print("Horario registrado correctamente.")

            elif opcion == "4":
                nombre = input("Ingrese el nombre del conductor: ")
                cedula = input("Ingrese la cédula del conductor: ")
                admin.agregar_conductor(nombre, cedula)
                print("Conductor agregado correctamente.")

            elif opcion == "5":
                cedula = input("Ingrese la cédula del conductor: ")
                horario = input("Ingrese el horario (formato HH:MM): ")
                admin.asignar_horario_a_conductor(cedula, horario)
                print("Horario asignado correctamente al conductor.")

            elif opcion == "6":
                id_bus = input("Ingrese el ID del bus: ")
                cedula = input("Ingrese la cédula del conductor: ")
                horario = input("Ingrese el horario (formato HH:MM): ")
                admin.asignar_bus_a_conductor(id_bus, cedula, horario)
                print("Bus asignado correctamente al conductor.")

            elif opcion == "7":
                print("Buses:")
                print(admin.mostrar_buses())

            elif opcion == "8":
                print("Conductores:")
                print(admin.mostrar_conductores())

            elif opcion == "9":
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    menu()