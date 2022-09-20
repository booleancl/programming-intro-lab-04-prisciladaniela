# Una función es un grupo de sentencias con un nombre, que realiaza una computación.
# Primero uno define una función y luego se "llama" o "ejecuta" esa función.

# Python viene con muchas funciones listas para usar. 
# Solo hay que llamrla o ejecutarlas
print ("Hola Priscila")

# La mayoría de las funciones entregan un valor, es decir, nos devuelven el resultado. Ejemplo:

str_num = "32" # Esto es un string que parece número
real_num = int(str_num) # Esta función transforma a entero 
print(type(real_num))

float_num = 3.9999
int_num = int(float_num) # No aproxima, corta el decimal
print(int_num)

# La siguiente línea es un error
# int("Hola inmundo")

print(float('32')) # Esta función entrega un float
print(str(3.1415)) # Esta función entrega un str

# Composición de funciones: Andar funciones

print(str(3.1415))
