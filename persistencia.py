import sqlite3
from colorama import Back, Style, init
init()


#-----------SQL--------------
def conectar_sql():
    conexion = sqlite3.connect("inventario.db")
    conexion.row_factory = sqlite3.Row
    return conexion

def crear_tabla_sql():
    query = """
            CREATE TABLE IF NOT EXISTS productos( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad REAL NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
            )
    """
    try:
        with conectar_sql() as con:
            con.execute(query)
        return True
    
    except Exception as e:
        print(Back.LIGHTRED_EX + f"[ERROR] No se pudo crear la tabla: {e}" + Style.RESET_ALL)

def insertar_productos_sql(nombre, descripcion, cantidad, precio, categoria):
    query = """
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
    """
    with conectar_sql() as con:
        cursor = con.execute(query, (nombre, descripcion, cantidad, precio, categoria))
    return {"id": cursor.lastrowid, "nombre": nombre, "descripcion": descripcion, "cantidad": cantidad, "precio": precio, "categoria": categoria}

def eliminar_producto_sql(id_eliminar):
    query = """
            DELETE FROM productos WHERE id = ?
    """
    with conectar_sql() as con:
        cursor = con.execute(query, (id_eliminar,))
    return cursor.rowcount > 0

def mostrar_todo_sql():
    query = """
            SELECT * FROM productos ORDER BY id
    """
    try:
        with conectar_sql() as con:
            cursor = con.execute(query)
            filas = cursor.fetchall()

            productos = [dict(fila) for fila in filas]
            return productos
    except Exception as e:
        print(Back.LIGHTRED_EX + f"[ERROR] No se pudieron obtener los productos: {e}" + Style.RESET_ALL)
        return []
    
def reporte_stock_sql(limite):
    query = """
            SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad ASC
    """
    try:
        with conectar_sql() as con:
            cursor = con.execute(query,(limite,))
            filas = cursor.fetchall()
            return [dict(fila) for fila in filas]
    except Exception as e:
        print(Back.LIGHTRED_EX + f"[ERROR] No se pudo generar el reporte: {e}" + Style.RESET_ALL)
        return []
def modificar_producto_sql(id_modificar, columna, nuevo_valor):
    query = f"""
            UPDATE productos SET {columna} = ? WHERE id = ?
    """
    try:
        with conectar_sql() as con:
            cursor = con.execute(query,(nuevo_valor, id_modificar))
            con.commit()
            return cursor.rowcount > 0
    except Exception as e:
        print(Back.LIGHTRED_EX + f"[ERROR] No se pudo actualizar: {e}" + Style.RESET_ALL)
        return False


#-----------ARCHIVO TXT------------

def guardar_en_txt(lista_productos):
    try:
        with open("inventario.txt", "w") as archivo_inventario:
            for producto in lista_productos:
                linea = f"\n{producto['id']}|{producto['nombre']}|{producto['descripcion']}|{producto['cantidad']}|{producto['precio']}|{producto['categoria']}"
                archivo_inventario.write(linea)
            print(Back.LIGHTGREEN_EX + "\nProducto guardado con éxito en el archivo." + Style.RESET_ALL)
    except Exception as e:
        print(Back.LIGHTRED_EX + f"\n [ERROR] No se pudo guardar la informacion: {e}" + Style.RESET_ALL)

def id_producto(lista_productos):
    if not lista_productos:
        return 1
    
    id_maximo = 0
    for p in lista_productos:
        if p["id"] > id_maximo:
            id_maximo = p["id"]
    
    return id_maximo + 1


