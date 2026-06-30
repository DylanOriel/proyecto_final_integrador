import menu
import productos as produc
import persistencia as query
import utilidades
from colorama import Back, Style, init
init()

def accion_agregar(lista_productos: list):
    while True:
        nuevo_producto = produc.registrar_productos()
        
        producto_sql = query.insertar_productos_sql(
            nuevo_producto['nombre'],
            nuevo_producto['descripcion'],
            nuevo_producto['cantidad'],
            nuevo_producto['precio'],
            nuevo_producto['categoria']
        )

        nuevo_producto['id'] = producto_sql['id']
        
        lista_productos.append(nuevo_producto)
        query.guardar_en_txt(lista_productos)
        print(Back.LIGHTGREEN_EX + f"\nProducto '{nuevo_producto['nombre']}' agregado con éxito. (ID: {nuevo_producto['id']})" + Style.RESET_ALL)
        
        if not menu.confirmar_continuar("agregar"):
            break

def accion_mostrar(lista_productos: list):
    print("\n=== Lista de Productos ===")
    menu.mostrar_productos_todos(lista_productos)

def accion_buscar_nombre(lista_productos: list):
    while True:
        nombre      = menu.pedir_nombre_busqueda()
        resultados  = produc.buscar_por_nombre(lista_productos, nombre)

        if resultados:
            print(Back.LIGHTBLUE_EX + f"\n Se encontraron {len(resultados)} resultados:" + Style.RESET_ALL)
            menu.mostrar_productos_todos(resultados)
        else:
            print(Back.LIGHTBLUE_EX + f"\n No se encontraron productos con '{nombre}'." + Style.RESET_ALL)
        
        if not menu.confirmar_continuar("buscar nombre"):
            break

def accion_buscar_categoria(lista_productos: list):
    while True:
        categoria   = menu.pedir_categoria_busqueda()
        resultados  = produc.buscar_por_categoria(lista_productos, categoria)

        if resultados:
            print(Back.LIGHTBLUE_EX + f"\n Se encontraron {len(resultados)} resultados:" + Style.RESET_ALL)
            menu.mostrar_productos_todos(resultados)
        else:
            print(Back.LIGHTBLUE_EX + f"\n No se encontraron productos con '{categoria}'." + Style.RESET_ALL)
        
        if not menu.confirmar_continuar("buscar categoria"):
            break

        
def accion_eliminar(lista_productos: list): 
    if not lista_productos:
        print(Back.LIGHTBLUE_EX + "La lista de productos está vacía. No hay nada para borrar. \n" + Style.RESET_ALL)
        return None
    
    menu.mostrar_productos_todos(lista_productos)

    print("==== ELIMINAR PRODUCTOS ====")
    while True:
        id_buscar = menu.pedir_id("eliminar")
        producto_eliminar = produc.buscar_por_id(lista_productos, id_buscar)

        if not producto_eliminar:
            print(Back.LIGHTRED_EX + f"\n [ERROR] No se encontró ningún producto con el ID {id_buscar}." + Style.RESET_ALL)
        else:
            print(Back.LIGHTBLUE_EX + f"\nSe encontro el producto: {producto_eliminar['nombre']} - ID: {producto_eliminar['id']}" + Style.RESET_ALL)
            menu.mostrar_producto(producto_eliminar)

            if menu.confirmar_eliminacion(producto_eliminar["nombre"]):
                salida_sql = query.eliminar_producto_sql(id_buscar)
                if salida_sql:
                    produc.eliminar_por_id(lista_productos, id_buscar)
                    query.guardar_en_txt(lista_productos)
                    print(Back.LIGHTGREEN_EX + f"\n [ÉXITO] El producto '{producto_eliminar['nombre']}' ha sido eliminado." + Style.RESET_ALL)
                else:
                    print(Back.LIGHTBLUE_EX + "[ERROR] No se pudo eliminar de la base de datos." + Style.RESET_ALL)

            else:
                print(Back.LIGHTBLUE_EX + "\n [AVISO] Operacíon cancelada. El producto no fue eliminado." + Style.RESET_ALL)

        if not menu.confirmar_continuar("eliminar"):
            break

def accion_generar_reporte():
    print("\n==== GENERAR REPORTE ====")
    while True:
            limite = utilidades.validad_digit("\nIngrese la cantidad minima para el reporte de stock: ")
            resultados = query.reporte_stock_sql(limite)

            if resultados:
                print(Back.LIGHTBLUE_EX + f"\nProductos con stock menor o igual a {limite}:" + Style.RESET_ALL)
                menu.mostrar_productos_todos(resultados)
            else:
                print(Back.LIGHTBLUE_EX + f"\nNo hay productos con el stock minimo solicitado." + Style.RESET_ALL)
            
            if not menu.confirmar_continuar("reporte de stock"):
                break

def accion_modificar_producto(lista_productos: list):
    if not lista_productos:
        print(Back.LIGHTBLUE_EX + "La lista de productos está vacía. No hay nada para borrar. \n" + Style.RESET_ALL)
        return None
    
    menu.mostrar_productos_todos(lista_productos)
    
    print("\n==== MODIFICAR PRODUCTO ====")
    while True:
        id_modificar = menu.pedir_id("modificar")
        producto_modificiar = produc.buscar_por_id(lista_productos, id_modificar)

        if not producto_modificiar:
            print(Back.LIGHTRED_EX + f"\n [ERROR] No se encontró ningún producto con el ID {id_modificar}." + Style.RESET_ALL)
        else:
            print(Back.LIGHTBLUE_EX + f"\nSe encontro el producto: {producto_modificiar['nombre']} - ID: {producto_modificiar['id']}" + Style.RESET_ALL)
            menu.mostrar_producto(producto_modificiar)
        
        campos = {
            "1": ("Nombre", "nombre", "str"),
            "2": ("Descripción", "descripcion", "str"),
            "3": ("Cantidad", "cantidad", "digit"),
            "4": ("Precio", "precio", "digit"),
            "5": ("Categoria", "categoria", "str")
        }

        while True:
            print("\n ¿Qué campo quiere modificar?")
            menu.menu_modificar_producto()

            opcion = menu.pedir_opcion_modificar()

            if opcion == "6":
                break
            
            if opcion in campos:
                nombre_campo, nombre_columna_sql, tipo_dato = campos[opcion]

                

                if tipo_dato == "str":
                    nuevo_valor = utilidades.validad_str(f"Ingrese el nuevo {nombre_campo}: ")
                elif tipo_dato == "digit":
                    nuevo_valor = utilidades.validad_digit(f"Ingrese el nuevo {nombre_campo}: ")

                if query.modificar_producto_sql(id_modificar, nombre_columna_sql, nuevo_valor):
                    for p in lista_productos:
                        if p['id'] == id_modificar:
                            p[nombre_columna_sql] = nuevo_valor
                            break
                    query.guardar_en_txt(lista_productos)
                    print(Back.LIGHTGREEN_EX + f"\n [ÉXITO] {nombre_campo} actualizado correctamente." + Style.RESET_ALL)
                else:
                    print(Back.LIGHTRED_EX + "\n [ERROR] No se pudo actualizar en la base de datos." + Style.RESET_ALL)
            else:
                print(Back.LIGHTRED_EX + "\n [ERROR] Opción no válida." + Style.RESET_ALL)
        
        if not menu.confirmar_continuar("modificar"):
            break


def main():

    query.crear_tabla_sql()
    lista_productos = query.mostrar_todo_sql()
    print(Back.LIGHTBLUE_EX + "\n Sistema iniciado." + Style.RESET_ALL)

    while True:
        menu.menu_registro_productos()
        opcion = menu.pedir_opcion_menu()

        if opcion   == "1":
            accion_agregar(lista_productos)
        elif opcion == "2":
            accion_mostrar(lista_productos)
        elif opcion == "3":
            buscar_por = menu.pedir_busqueda()
            if buscar_por   == "1":
                accion_buscar_categoria(lista_productos)
            elif buscar_por == "2":
                accion_buscar_nombre(lista_productos)
            else:
                print(Back.LIGHTRED_EX + "[ERROR] Opción no valida. Intentá nuevamente." + Style.RESET_ALL)
        elif opcion == "4":
            accion_eliminar(lista_productos)
        elif opcion == "5":
            accion_generar_reporte()
        elif opcion == "6":
            accion_modificar_producto(lista_productos)
        elif opcion == "7":
            print("Hasta pronto!")
            break
        else:
            print(Back.LIGHTRED_EX + "\n [ERROR] Opción no valida. Ingresá una opcion valida (1-5)." + Style.RESET_ALL)

if __name__ == "__main__":
    main()