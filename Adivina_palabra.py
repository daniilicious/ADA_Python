#Hecho por Daniela Calderon

from random import choice  #codigo para seleccion aleatoria de palabras

def escoger_palabra(lista_palabras):
    palabra_escogida = choice(lista_palabras)
    return palabra_escogida.upper()

palabras = ["amarillo", "tulipan", "esperanza", "rinoceronte", "dinamarca", "uruguay", "refrigerador", "puntualidad", "python", "culebra"]
palabra_adivinar = escoger_palabra(palabras)
letras_adivinar = set(palabra_adivinar)
aciertos = set()
vidas = 4

print("Juguemos a adivinar la palabra")  #Mensaje de Inicio
print(f"Ingresa tu nombre: ") 
nombre = input()

print(f"Bienvenido/a {nombre}!\n") #Mensaje de bienvenida

