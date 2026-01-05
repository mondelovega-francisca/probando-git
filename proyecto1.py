print("1)Square")
print("2)Rectangle")
print("3)Triangle")
print("4)Circle")
eleccion=int(input("Choose the type of area you want to calculate: "))
while eleccion!=1 and eleccion!=2 and eleccion !=3 and eleccion !=4:
    print("Wrong input")
    eleccion=int(input("Choose the type of area you want to calculate: "))
if eleccion==1: #area cuadrado
    lado=float(input("Enter the side of the square in cm"))
    area=lado*lado
    print(f"El área es {area} cm^2")
elif eleccion==2:#area rectangulo
    lado1=float(input("Enter the width of the rectangle: "))
    lado2=float(input("Enter the height of the rectangle: "))
    area2=lado1*lado2
    print(f"El área es {area2} cm^2")
elif eleccion==3:#area triangulo
    base=float(input("introduce the base of the triangle: "))
    altura=float(input("enter the height of the triangle: "))
    area3=base*altura/2
    print(f"El área es {area3} cm^2")
else: #area circulo
    radio=float(input("enter the radius of the circle: "))
    area4=3.14159*radio*radio
    print(f"El área es {area4} cm^2")