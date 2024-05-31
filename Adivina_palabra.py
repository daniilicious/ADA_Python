#Mensaje de Inicio
print("Juguemos a adivinar la palabra")  
print(f"Ingresa tu nombre: ") 
nombre = input()

#Mensaje de bienvenida
print(f"Bienvenido {nombre}!")

def listo_empezar():
    while True:
        eleccion = input("¿Listo para jugar? Si / No ")
        if eleccion in ["si", "Si", "SI"]:
            return eleccion
        else:
            print("Regresa cuando estes listo para jugar")
eleccion_usuario = listo_empezar()
print(f"Empecemos")  #inicio del juego
