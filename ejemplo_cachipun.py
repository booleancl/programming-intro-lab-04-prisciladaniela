import random
print("Bienvenido al juego del cachipun")
print("Selecciona tu opción")
print("1 para la piedra")
print("2 para la tijera")
print("3 para la piedra")
user_input = int(input("jugador1\n"))
options = ["piedra","tijera","papel"]
user_option = options[user_input -1]

computer_option = random.choice(options)

print("Mi mano: ", user_option)
print("Mano del computador:", computer_option)

if(user_option == computer_option):
    print("Empatan jugadores")
elif (user_option == "piedra" and computer_option == "tijera") or (user_option == "tijera" and computer_option == "papel") or (user_option == "papel" and computer_option == "piedra"):
    print("Felicitaciones, ganaste la partida")
else:
    print("lo siento el computador a ganado")    

