# Podemos escribir un archivo con el modo"a"

file = open("file_handling/demo.txt", "a")

file.write("Hola inmundo")

file.close()

file = open("file_handling/demo.txt", "w")

file.write("Oooops, se borro el contenido")

file.close()
