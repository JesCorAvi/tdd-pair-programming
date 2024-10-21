from ejercicio_318 import es_palindromo  

def test_es_palindromo():
    assert es_palindromo("Radar") == True
    assert es_palindromo("reconocer") == True
    assert es_palindromo("ana") == True  
    
    assert es_palindromo("palabra") == False
    assert es_palindromo("python") == False
    assert es_palindromo("programa") == False