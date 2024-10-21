"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""
def num_vocales(cadena):
    vocales = {
        'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0
    }
    
    for letra in cadena.lower():
        if letra in 'aáàâä':
            vocales['a'] += 1
        elif letra in 'eéèêë':
            vocales['e'] += 1
        elif letra in 'iíìîï':
            vocales['i'] += 1
        elif letra in 'oóòôö':
            vocales['o'] += 1
        elif letra in 'uúùûü':
            vocales['u'] += 1
    
    return vocales


if __name__ == "__main__":
    palabra = input("Escriba una pababra: ")
    vocales = num_vocales(palabra)
    print(f"Tiene: {vocales["a"]} a, {vocales["e"]} e, {vocales["i"]} i, {vocales["o"]} o, {vocales["u"]} u")
