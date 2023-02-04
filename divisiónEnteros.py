# Funcion para dividir dos numeros enteros
def dividir_dos_enteros(x, y):
    try:
        return x/y
    except ZeroDivisionError as ze:
        print('No se permite la división por cero: ', ze)
    except Exception as ex:
        print('Los datos ingresados no son validos: ', ex)

print(dividir_dos_enteros(11,4))