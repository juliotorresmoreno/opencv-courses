

class Producto:
    nombre: str
    precio: float
    cantidad: int

    def __init__(self, nombre: str, precio: float, cantidad: int):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        
        self.nombre = nombre

        self.actualizar_precio(precio)
        self.actualizar_cantidad(cantidad)

    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio debe ser mayor o igual que 0")
        self.precio = nuevo_precio
    
    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0")
        self.cantidad = nueva_cantidad

    def __str__(self):
        return f"Producto {self.nombre}, precio: {self.precio}, cantidad: {self.cantidad}"

class Inventario:
    productos: list[Producto]

    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre: str):
        if not nombre.strip():
            return None
        for producto in self.productos:
            if nombre.lower() == producto.nombre.lower():
                return producto
        return None

    def calcular_valor_inventario(self):
        return sum(
            producto.precio * float(producto.cantidad) 
            for producto in self.productos
        )
    
    def listar_productos(self):
        for producto in self.productos:
            print(producto)

def menu_principal():
    inventario = Inventario()
    while True:
        print("Bienvenido al sistema de inventario")
        print("Opciones")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

        opcion = input("Seleccione la opcion: ")
        if opcion == "1":
            nombre = input("Por favor digite el nombre del producto:")
            precio = float(input("Digite el precio"))
            cantidad = int(input("Cantidad"))
            inventario.agregar_producto(Producto(nombre, precio, cantidad))
        elif opcion == "2":
            nombre = input("Por favor digite el nombre del producto:")
            resultado = inventario.buscar_producto(nombre)
            print(resultado)
        elif opcion == "3":
            inventario.listar_productos()
        elif opcion == "4":
            resultado = inventario.calcular_valor_inventario()
            print("El valor del inventario es de: " + str(resultado))
        elif opcion == "5":
            break
        else:
            continue

if __name__ == "__main__":
    menu_principal()
