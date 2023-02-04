# Funcion para dividir dos numeros enteros
def dividir_dos_enteros(x, y):
    try:
        # Retorna el resultado de la división si no tiene errores
        return x/y
    
    # Retorna None, muestra el mensaje con el error y el tipo de error que se da (si es el caso).
    except ZeroDivisionError as ze:
        print(f'No se permite la división por cero: {ze}\n{type(ze)}')
    except Exception as ex:
        print(f'Los datos ingresados no son validos: {ex}\n{type(ex)}')
