#Hecho por Daniela Calderon

from random import choice  #codigo para seleccion aleatoria de palabras

def escoger_palabra(lista_palabras):
    palabra_escogida = choice(lista_palabras)
    return palabra_escogida.upper()

palabras = ["amarillo", "tulipan", "esperanza", "rinoceronte", "dinamarca", "uruguay", "refrigerador", "puntualidad", "python", "culebra", "comarca"]
palabra_adivinar = escoger_palabra(palabras)
letras_adivinar = set(palabra_adivinar)
aciertos = set()
vidas = 5

print("Juguemos a adivinar la palabra")  #Mensaje de Inicio
print(f"Ingresa tu nombre: ") 
nombre = input()

print(f"¡Bienvenido/a {nombre}!\n") #Mensaje de bienvenida

def listo_empezar():
    while True:
        eleccion = input("¿Listo/a para jugar? Si / No\n")
        if eleccion in ["si", "Si", "SI", "sí"]:
            return eleccion
        else:
            print("Regresa cuando estes listo para jugar")

eleccion_usuario = listo_empezar()

print("\nEmpecemos\n")  #inicio del juego

print("Palabra a adivinar: ", end="")  #pisitos para cada letra de la palabra
for char in palabra_adivinar:
    print("_", end =" ")
print("\n")

#---------------condiciones del juego-----------------------------------------
while vidas > 0:
    error = 0
    mostrar_palabra = ""

    for char in palabra_adivinar:
        if char in aciertos:
           mostrar_palabra += char + " "
        else:
            mostrar_palabra += "_ "
            error += 1
    
    print(mostrar_palabra)

    if error == 0:
       print("¡Ganaste!\n\n")
       break

    acierto = input("Ingresa una letra: ").upper()

    if acierto in letras_adivinar:
       aciertos.add(acierto)
    else:
       vidas -= 1
       print("Error")

    print(f"Tienes {vidas} vida/s,\n")
    
    if vidas == 0:
       print("¡Perdiste! Mejor suerte en la proxima")
