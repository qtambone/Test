# Fonction pour additionner deux nombres
def addition(a, b):
    return a + b

# Fonction pour soustraire deux nombres
def soustraction(a, b):
    return a - bls

# Fonction pour multiplier deux nombres
def multiplication(a, b):
    return a * b

# Fonction pour diviser deux nombres
def division(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    else:
        return a / b


resultat = addition(4, 7)
print(resultat)  # affiche 11

resultat = division(10, 2)
print(resultat)  # affiche 5.0