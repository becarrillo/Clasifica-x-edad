def clasificarRangoEdad(edad):
    if edad > 0 and edad <= 125:
        if edad < 18:
            print("Menor de edad")
        else:
            if edad >= 18 and edad < 60:
                print("Mayor de edad")
            else:
                print("De la tercera edad")
    else:
        print("Edad Inválida")
        
edad = 9
clasificarRangoEdad(edad)
edad = -6
clasificarRangoEdad(edad)
edad = 89
clasificarRangoEdad(edad)
edad = 16
clasificarRangoEdad(edad)
edad = 29
clasificarRangoEdad(edad)