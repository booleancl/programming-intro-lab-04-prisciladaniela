# Las funciones pueden hacer cosas y también pueden retornar valores

def circle_area(radius):
    area = 3.1415*radius**2
    return area

# En este caso la función me entrega o devuelve el valor   

result = circle_area(4)
print(result)

def circle_volume(radius,height):
    volume = 3.1415*radius**2*height
    return volume

result_two = circle_volume(4,10)
print(result_two)
print(area)