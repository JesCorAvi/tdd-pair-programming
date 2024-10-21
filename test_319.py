from ejercicio_319 import *

def test_num_vocales():
    assert num_vocales('plátano') == {'a': 2, 'e': 0, 'i':0, 'o': 1, 'u': 0}
    assert num_vocales('fdjkdhf') == {'a': 0, 'e': 0, 'i':0, 'o': 0, 'u': 0}
    assert num_vocales('pingüino') == {'a': 0, 'e': 0, 'i':2, 'o': 1, 'u': 1}