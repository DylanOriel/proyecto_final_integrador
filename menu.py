import utilidades
from colorama import Back, Style, Fore, init 
init()

def menu_registro_productos():
    """ Muestra del menu """
    print("\n" + "=" * 50)
    print("             SISTEMA DE GESTION DE PRODUCTOS ")
    print("=" * 50)
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Buscar productos")
    print("4. Eliminar productos")
    print("5. Generar reporte stock bajo")
    print("6. Modificar productos")
    print("7. Salir")

def pedir_busqueda():

    return input("Elegí una opción para buscar: ('1' para buscar por categoría | '2' para buscar por nombre)")

def pedir_opcion_menu():

    return input("Elegí una opción (1-7): ")

def pedir_opcion_modificar():

    return input("Elegí una opción (1-6): ")

def confirmar_continuar(accion):
    
    return utilidades.confirmacion(f"¿Queres {accion} otro producto")

def mostrar_producto(producto):

    print(Back.LIGHTYELLOW_EX + f"ID : {producto['id']} | nombre : {producto['nombre']} | descripcion : {producto['descripcion']} | cantidad : {producto['cantidad']} | precio :$ {producto['precio']} | categoria : {producto['categoria']}" + Style.RESET_ALL)
    
def mostrar_productos_todos(lista_productos):
    if not lista_productos:
        print(Back.LIGHTBLUE_EX + "\nNo hay productos cargados." + Style.RESET_ALL)
        return
    
    #Defino ancho de las columnas para que sea mas facil de ajustar
    w_id = 6
    w_nom = 20
    w_des = 35
    w_can = 15
    w_pre = 15
    w_cat = 35

    ancho_total = w_id + w_nom + w_des + w_can + w_pre + w_cat + 5 # +5 para espacios entre col

    header = (
        f"{'ID':<{w_id}}"
        f"{'NOMBRE':<{w_nom}}"
        f"{'DESCRIPCION':<{w_des}}"
        f"{'CANTIDAD':<{w_can}}"
        f"{'PRECIO':<{w_pre}}"
        f"{'CATEGORIA':<{w_cat}}"
    )
    print(Back.BLUE + Style.BRIGHT + Fore.WHITE + header + Style.RESET_ALL)

    print("\n" + "-" * ancho_total)

    for p in lista_productos:
        desc = p['descripcion'] if p['descripcion'] else "Sin descripción"
        if len(desc) > w_des:
            desc = desc[:w_des-3] + "..."

        fila = (
            f"{p['id']:<{w_id}} "
            f"{p['nombre'][:w_nom-1]:<{w_nom}} "
            f"{desc:<{w_des}} "
            f"{p['cantidad']:<{w_can}} "
            f"${p['precio']:<{w_pre-1}.2f} "
            f"{p['categoria'][:w_cat-1]:<{w_cat}}"
        )
        print(fila)

    print("-" * ancho_total)
    print(Back.LIGHTBLUE_EX + Style.BRIGHT + f" TOTAL DE PRODUCTOS: {len(lista_productos)} " + Style.RESET_ALL)
    print("=" * ancho_total)

def pedir_id(accion):

    return utilidades.validad_digit(f"\nIngresá el ID del producto a {accion}: ", minimo=1)

def confirmar_eliminacion(nombre):

    return utilidades.confirmacion(f"\n¿Estás seguro de eliminar '{nombre}'? ")

def pedir_nombre_busqueda():

    return utilidades.validad_str("\nIngresá el nombre a buscar: ", campo="nombre del producto")

def pedir_categoria_busqueda():

    return utilidades.validad_str("\nIngresá la categoria a buscar: ")

def menu_modificar_producto():
    """ Muestra del menu """
    print("\n" + "=" * 50)
    print("             SISTEMA DE GESTION PARA MODIFICAR PRODUCTOS ")
    print("=" * 50)
    print("1. Nombre")
    print("2. Descripcion")
    print("3. Cantidad")
    print("4. Precio")
    print("5. Categoria")
    print("6. Salir")