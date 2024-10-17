#guzman guzman 
("")
("guzman jared")
("")
# Diccionario con precios de frutas
# precio por kilo
precios_frutas = {
    'manzana': 2.5,  
    'plátano': 1.2,
    'naranja': 1.8,
    'fresa': 3.0
}

# Solicitar al usuario que introduzca una fruta
fruta_input = input("Introduce una fruta (manzana, plátano, naranja, fresa): ").lower()

# Solicitar el número de kilos
kilos = float(input("Introduce el número de kilos: "))

# Calcular ye imprimir el precio o un mensaje de error
if fruta_input in precios_frutas:
    precio = precios_frutas[fruta_input] * kilos
    print(f"El precio de {kilos} kilos de {fruta_input} es: ${precio:.2f}")
else:
    print("La fruta no está en el diccionario.")

