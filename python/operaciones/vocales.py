texto = input("Introduce un texto: ")
cont = 0
for i in range(len(texto)):
    if texto[i].lower() == "a" or \
       texto[i].lower() == "e" or \
       texto[i].lower() == "i" or \
       texto[i].lower() == "o" or \
       texto[i].lower() == "u":
       cont += 1

print(f"El texto contiene {cont} vocales.")