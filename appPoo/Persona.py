class Persona:

    def __init__(self, id, nombre, apellido, correo, contrasena):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._contrasena = contrasena

    # Getter and Setter

    @property  # Getter
    def id(self):
        return self._id
    @id.setter  # Setter
    def id(self, id):
        self._id = id

    @property  # Getter
    def nombre(self):
        return self._nombre
    @nombre.setter  # Setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property  # Getter
    def apellido(self):
        return self._apellido
    @apellido.setter  # Setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property  # Getter
    def correo(self):
        return self._correo
    @correo.setter  # Setter
    def correo(self, correo):
        self._correo = correo

    @property  # Getter
    def contrasena(self):
        return self._contrasena
    @id.setter  # Setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena

    def registrar(self):
        self._id = input("Indique el id: ")
        self._nombre = input("Ingresar nombre: ")
        self._apellido = input("Ingresar apellido: ")
        self._correo = input("Ingresar correo: ")
        self._contrasena = input("Ingresar contraseña: ")

    def ver_registro(self):
        print(f"Id: {self._id} Nombre: {self._nombre} Apellido: {self._apellido} Correo: {self._correo}")