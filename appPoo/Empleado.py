from Persona import Persona


class Empleado(Persona):
    def __init__(self, id, nombre, apellido, correo, contrasena, cargo, salario):
        super().__init__(id, nombre, apellido, correo, contrasena)
        self._cargo = cargo
        self._salario = salario

    @property
    def cargo(self):
        return self._cargo
    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self, salario):
        self._salario = salario

    def registrar(self):
        super().registrar()
        self.cargo = input("Ingresar el cargo: ")
        self.salario = float(input("Ingresar salario: "))

    def ver_registro(self):
        super().ver_registro()
        print(f"Cargo: {self._cargo} Salario: {self._salario}")

    def iniciar_sesion(self):
        correo_reg = input("Ingrese el correo registrado: ")
        contras_reg = input("Ingresa la contraseña registrada: ")

        if correo_reg == self.correo and contras_reg == self.contrasena:
            print(f"Bienvenido {self.nombre}")
            return True
        else:
            print("Valide sus credeciales")
            return False

    def iniciar_negocio_empleado(self, iniciar_sesion, ver_registro):
        init = iniciar_sesion()

        while init == True:
            print("1: Ver datos usuario 2:hacer otra cosa 3: Salir")
            opc=int(input("Selecciones una opcion"))

            if opc == 1:
                print("Ver datos usuario")
                ver_registro()
            elif opc == 2:
                print("Hacer cosa")
            elif opc == 3:
                print("Salir")
