# Podemos crear o definir nuestras propias funciones
# Lo hacemos con la palabra especial "def" y el cuerpo
# La función debe ir correctamente indentado

def chuchuwa(inst):
    print("Chuchuwa chuchuwa chuchuwa wa wa!")
    print("Chuchuwa chuchuwa chuchuwa wa wa!")
    print("Atención!, Compañia")
    print(inst)

print(chuchuwa)
print(type(chuchuwa))

# El llamado de la función
chuchuwa("Mano hacia el frente")
chuchuwa("Hombro hacia atrás")

# Las funciones deben llamarse o ejecutarse con los mimos parametros que se definió
result = chuchuwa("lengua afuera") 

# Si la función no tiene un valor de retorno, nos entregará "None", que es para representar: "Nada"
print(result)
