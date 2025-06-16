# Pre-entrega 1 - Gestión de Productos
productos = []

def agregar_producto():
    """Agregar un nuevo producto a la lista con validación"""
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            break
        print(" El nombre no puede estar vacío.")
    
    while True:
        stock  = int(input("Ingrese el stock del producto: "))
        if stock:
            break
        print("El stock no puede estar vacío.")
    
    while True:
        
            precio = int(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
                continue
            break
        
    
    productos.append([nombre, stock, precio])
    print(f" Producto agregado: {nombre} - {stock} - ${precio}")




def mostrar_productos():
    """Muestra todos los productos registrados"""
    if not productos:
        print("\n No hay productos registrados.")
        return
    print("\n Lista de productos:")
    for i, p in enumerate(productos, 1):
        print(f"{i}. Nombre: {p[0]} | Stock: {p[1]} | Precio: ${p[2]}")






def buscar_producto():
    """Busca productos por nombre"""
    termino = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    encontrados = [p for p in productos if termino in p[0].lower()]
    
    if encontrados:
        print("\n Productos encontrados:")
        for p in encontrados:
            print(f"- Nombre: {p[0]} | Stock: {p[1]} | Precio: ${p[2]}")
    else:
        print(" No se encontraron productos con ese nombre.")





def eliminar_producto():
    """Elimina un producto según su número en la lista"""
    mostrar_productos()
    if not productos:
        return
    try:
        numero = int(input("Ingrese el número del producto a eliminar: "))
        if 1 <= numero <= len(productos):
            eliminado = productos.pop(numero - 1)
            print(f"Producto eliminado: {eliminado[0]}")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Ingrese un número válido.")

#------ Menú principal  bucle-----
while True:
    print("\n-----MENÚ DE GESTIÓN DE PRODUCTOS-------")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1-5): ").strip()
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("\n Gracias por usar el sistema de gestión de productos.")
        break
    else:
        print("Opción inválida. Es del 1 al 5 amigo.")
