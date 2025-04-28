edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad: ")
if edad >= 18 and ciudad == "bogotá":
    print("Puede votar en bogota")
elif edad >= 18 and ciudad != "bogota":
    print("No puede votar en bogota")
else:
    print("No puede votar por no ser mayor de edad")