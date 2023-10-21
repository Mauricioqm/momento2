class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = None  # El precio de venta se calculará más tarde

    def calcular_precio_venta(self, margen_de_venta):
        if margen_de_venta <= 0:
            print("El margen de venta debe ser mayor que cero.")
            return
        self.precio_de_venta = self.costo / (1 - margen_de_venta)

class RegistroProductos:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar los productos

    def registrar_producto(self, producto, callback):
        if producto.id in self.productos:
            print(f"El producto con ID {producto.id} ya está registrado.")
        else:
            callback(producto)
            self.productos[producto.id] = producto
            print(f"Producto {producto.nombre} registrado con éxito.")

    def imprimir_listado_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
        else:
            print("Listado de productos registrados:")
            for producto_id, producto in self.productos.items():
                print(f"ID: {producto_id}, Nombre: {producto.nombre}, Precio de venta: {producto.precio_de_venta:.2f}")

# Callback para calcular el precio de venta
def calcular_precio_de_venta(producto):
    margen_de_venta = int(input("Ingrese el margen de venta: ")) / 100
    producto.calcular_precio_venta(margen_de_venta)

# Crear una instancia de RegistroProductos
registro = RegistroProductos()

# Crear un producto y registrar usando el callback para calcular el precio de venta
producto1 = Producto(
    int(input("Ingrese el id del producto: ")),
    input("Ingrese el nombre del producto: "),
    input("Ingrese la descripción del producto: "),
    int(input("Ingrese la cantidad del producto: ")),
    float(input("Ingrese el precio de venta del producto: ")),
)

registro.registrar_producto(producto1, calcular_precio_de_venta)

# Imprimir el listado de productos
registro.imprimir_listado_productos()