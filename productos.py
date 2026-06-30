from utilidades import *

def registrar_productos():
    '''
    Como indica el nombre, pido al usuario ingresar los campos correspondientes para generar un nuevo producto
    que luego sera guardado en la tabla de la bd
    '''
    print("=== INGRESO DE PRODUCTOS ===")
    print("Ingresar los productos llenando los campos correspondientes. (No pueden estar vacios)")
    nombre = validad_str(" Nombre : ", campo = "nombre")  
    descripcion = validad_str(" Descripción : ", campo = "descripcipón")
    cantidad = validad_digit(" Cantidad : ", minimo = 1)
    precio = validad_digit(" Precio :$ ", minimo = 1)
    categoria = validad_str(" Categoría : ", campo = "caegoría")

    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "cantidad": cantidad,
        "precio": precio,
        "categoria": categoria,
    }

    return producto

def buscar_por_nombre(lista_productos, nombre):
    '''
    Esta y las demas funciones de abajo reciben una lista y un tipo de dato
    que generan otra lista con el tipo de dato pedido, es un filtro para buscar por nombre
    categoria
    '''
    resultados = []

    for p in lista_productos:
        if nombre in p["nombre"]:
            resultados.append(p)
    
    return resultados

def buscar_por_categoria(lista_productos, categoria):
    resultados = []

    for p in lista_productos:
        if categoria in p["categoria"]:
            resultados.append(p)

def buscar_por_id(lista_productos, buscar_id):
    '''
    Verifico que en la lista actual de la BD exista el id que me pide el usuario
    '''
    for producto in lista_productos:
        if producto["id"] == buscar_id:
            return producto
    return None

def eliminar_por_id(lista_productos: list, eliminar_id):
    '''
    En caso de que exista el id pedido, busco en la lista para eliminarlo
    '''
    for i, producto in enumerate(lista_productos):
        if producto["id"] == eliminar_id:
            lista_productos.pop(i)
            return True
    return False
   