#guzman guzman 
("")
("guzman jared")
# asignar el diccionario en una variable
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

# Solicitar al usuario que ingrese una divisa
divisa_input = input("Introduce una divisa (Euro, Dollar, Yen): ")

# Mostrar el símbolo o un mensaje de error
if divisa_input in divisas:
    print(f"El símbolo de {divisa_input} es: {divisas[divisa_input]}")
else:
    print("La divisa no está en el diccionario.")
