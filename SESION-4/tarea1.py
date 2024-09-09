'''
/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 '''
import re

def es_expresion_correcta(expresion):
    patron = r'^(-?\d+(\.\d+)?)(\s*[-+*/]\s*(-?\d+(\.\d+)?))*$'
    
    if re.match(patron, expresion):
        if '--' in expresion:
            return False
        return True
    else:
        return False

expresion_usuario = input("Por favor, ingresa una expresión matemática: ")

if es_expresion_correcta(expresion_usuario):
    print("La expresión es correcta.")
else:
    print("La expresión es incorrecta.")
