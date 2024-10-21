from ejercicio_319 import *

palabra = 'plátano'

def test_num_a():
    assert num_a(palabra) == 2

def test_num_e():
    assert num_e(palabra) == 0

def test_num_i():
    assert num_i(palabra) == 0

def test_num_o():
    assert num_o(palabra) == 1

def test_num_u():
    assert num_u(palabra) == 0