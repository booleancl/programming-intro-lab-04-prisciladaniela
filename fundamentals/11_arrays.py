# Los Arreglos (listas) son una ESTRUCTURA DE DATOS FUNDAMENTAL
# que permite agrupar valores, separados por coma

first_array=['Sacar la basura', 'peinarse', 'dormir', 'Secar la ropa']

# En python el primer elemento de un arreglo tiene posición (indice) 0
print(first_array[0])
print(first_array[1])
print(first_array[2])
print(first_array[3])
# No existe el elemnto con indice 4 y python da un error
# print(first_array[4])

# Podemos saber el largo de un arreglo o lista con la función pre definida len()
print(len(first_array))

# Adémas, podemos agregar elementos al arreglo
first_array.append('Comer')
first_array.append('Dormir')

# Podemos indicar la posición del nuevo elemento a agregar con insert
first_array.insert(0,'Levantarse')

# Podemos imprimir la lista completa
print(first_array)