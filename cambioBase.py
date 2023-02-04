
# Función de cambio de base, empezando desde base 10 con un numero dado x y llevarlo a base k
def cambioBase(x, k):
    
    resultado = x
    residuo = 0
    representacion = ''

    # Manejo de excepciones, si ocurre una excepción devuelve: none
    try:
        if k<=1:
            raise ValueError(f'No se permite la operación con la base ingresada: {k}')

        # Uso de la función de conversión a Hexadecimal de python en caso de base 16
        if k==16:
            return hex(x)

        while resultado/k > 0 :
            residuo = resultado%k
            resultado = resultado//k
            representacion = representacion + str(residuo)

        # Inversión del orden en el que se dieron los residuos en las divisiones
        representacion = int(representacion[::-1])
        return representacion
    
    # Manejo de excepción general
    except Exception as ex:
        print(f'Datos ingresados erroneos:\n{ex}\n{type(ex)}')

