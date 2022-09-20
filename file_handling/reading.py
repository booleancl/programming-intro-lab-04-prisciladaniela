# Hay tres modos para leer un archivo con la función open()

#"r" para leer 
#"a" para agregar al final (oppend)
#"w" para sobre escribir el contenido

file = open('file_handling/sample.txt', "r", encoding="UTF-8")
# La función open entre un "objeto". Entenderemos un objeto
# como algo que tiene "datos" y "metodos". Los métodos son para
# manipular sus datos

print(file)


# Para leer el contenido del objeto file, tenemos el método del objeto
# read

print(file.read())

# Podemos leer el archivo utilizando for
file = open('file_handling/sample.txt', "r", encoding="UTF-8")
for line in file: 
    print(line)

# Luego de utilizar el archivo debemos cerrarlos
file.close()