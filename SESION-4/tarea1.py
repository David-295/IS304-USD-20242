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
    patron = r'^(-?\d+(\.\d+)?)(\s*[\+\-\*/%]\s*(-?\d+(\.\d+)?))*$'
    return bool(re.match(patron, expresion))
