#Hecho por Daniela Calderon

print("Juguemos a adivinar la palabra")  #Mensaje de Inicio
print(f"Ingresa tu nombre: ") 
nombre = input()


print(f"Bienvenido {nombre}!") #Mensaje de bienvenida

def listo_empezar():
    while True:
        eleccion = input("¿Listo para jugar? Si / No ")
        if eleccion in ["si", "Si", "SI"]:
            return eleccion
        else:
            print("Regresa cuando estes listo para jugar")
eleccion_usuario = listo_empezar()
print(f"Empecemos")  #inicio del juego
