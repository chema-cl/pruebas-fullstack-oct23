import calculadora
import pytest

def test_sumar():
	a = 2
	b = 2
	c = calculadora.sumar(a, b)
	assert c == 4

def test_restar():
	a = 2
	b = 2
	c = calculadora.restar(a, b)
	assert c == 0

def test_multiplicar():
	a = 2
	b = 3
	c = calculadora.multiplicar(a, b)
	assert c == 6