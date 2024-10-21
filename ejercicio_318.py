def es_palindromo(palabra: str):
    if palabra == palabra[::-1]:
        print('La palabra', palabra, 'es un palíndromo')
        return True
    else:
        print('La palabra', palabra, 'no es un palíndromo')
        return False
    

if __name__ == "__main__":
    palabra_usu = input('Dame una palabra y te diré si es un palíndromo o no: ')
    es_palindromo(palabra_usu)