# Tenemos expresiones que se pueden evaluar en términos booleanos
# ó dicótomicos 
# Ejemplo

print(10 > 9)

# Esto nos permite hacer ejecuciones condicionales, por ejemplo

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

gaby_age = 4
Paola_age = 30

# Estas siguientes instrucciones las podriamos leer como:
# "Si (if)el resultado de is_adult ejecutada con la variable gaby_age o paola_age
# es verdadero, enronces el programa imprime'¿Quieres una cerveza?'
# De otro MODO (else), imprime 'Cantemos Chuchuwa'"

if is_adult(Paola_age):
    print("Quieres una cerveza")
else:
    print("Cantemos Chuchuwa") 

# elif es una abreviacion de "else if", nos permite segui evaluando expresiones

if (Paola_age > gaby_age):
    print("Paola es mayor que Gaby")
elif Paola_age < gaby_age:
    print("Paola es menor que gaby")
else:
    print("Tienen la misma la edad Gaby y Paola")
     