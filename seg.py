#Calcular  perimetro y area de un rectangulo dada su base y altura



#retangulo= (perimetro, y, area)
#rectangulo= character(input("ingresa la formúla de perimetro y area"))
#rectangulo= ("perimetro"(2*(L+A),y ,"area" (A= L*A)))
#print(p(2*(L*A)) y (A= L*A))

largo =float(input("Introduce el  largo del rectangulo"))
ancho =float(input("Introduce  el ancho del rectangulo"))

area =largo * ancho
perimetro= 2 * (ancho +largo)
print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es:{perimetro}")

