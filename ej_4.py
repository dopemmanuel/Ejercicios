"""Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
try:
    celcius = int(input("Ingresa los grados °C: "))

    
    Fahrenheit = celcius * 9 / 5 + 32
    print(celcius," °C son en °F ", Fahrenheit)
except ValueError:
    print("Solo caracter numerico para esto.")
"""

celcius = int(input("Ingresa los grados °C: "))

Fahrenheit = celcius * 9 / 5 + 32
print(celcius," °C son en °F ", Fahrenheit)