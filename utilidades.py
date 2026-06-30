from colorama import Back, Style, init
init()


def validar_datos(mensaje, obligatorio=True, validar_precio=False):
        '''
        Esta funcion no la termino usando, la use de base para crear las otras dos principales
        '''
        while True:
            dato = input(mensaje).strip()
            if not dato and obligatorio:
                print(Back.LIGHTRED_EX + "\n [ERROR] Este campo es obligatorio." + Style.RESET_ALL)
                continue
            if not validar_precio and dato.isdigit():
                print(Back.LIGHTRED_EX + "\n [ERROR] No puede ser número." + Style.RESET_ALL)
                continue
            if validar_precio:
                try:
                    valor = float(dato)
                    if valor < 0:
                        print(Back.LIGHTRED_EX + "\n [ERROR] El precio no puede ser menor que cero." + Style.RESET_ALL)
                        continue
                except ValueError:
                    print(Back.LIGHTRED_EX + "\n [ERROR] Debe ingresar un número válido." + Style.RESET_ALL)
            return dato
        
def validad_str(msj, campo = "campo"):
        '''
        Valido el contenido de un campo si esta vacio y si el tipo de dato correcto
        '''
        while True:
                    dato = input(msj).strip().lower()
                    if dato:
                          return dato
                    print(f"El {campo} no puede estar vacio. Intente nuevamente.")

def validad_digit(msj, minimo = 1):
        '''
        Valido si el contenido esta vacio y si el tipo en este caso es un digito
        '''
        while True:
                    dato = input(msj).strip()
                    try:
                        valor = int(dato)
                        if valor < minimo:
                              print(f"El valor debe ser mayor o igual a {minimo}.")
                        else:
                            return valor
                    except ValueError:
                        print(f" {dato} No es un numero valido. Intente nuevamente")

def confirmacion(msj):
      '''
      Pregunto si o no al usuario para continuar con la accion actual en la que esta
      '''
      while True:
            respuesta = input(f"{msj} (S/N): ").strip().lower()
            if respuesta == "s" or respuesta == "si":
                return True
            elif respuesta == "n" or respuesta == "no":
                return False
            else: 
                print(Back.LIGHTBLUE_EX + "Ingresa 'si' o 'no' para validar." + Style.RESET_ALL)