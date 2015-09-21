#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora


import sys

def main():
    print("hola")

def suma(sumando1, sumando2):
    return sumando1 + sumando2

if __name__ == "__main__":
#    print(sys.argv)
    try:
        operando1 = int(sys.argv[2])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("¡Tienen que ser enteros!")
    print(suma(operando1, operando2))

def resta(restando1, restando2):
    return restando1 - restando2

if __name__ == "__main__":
#    print(sys.argv)
    try:
        operando1 = int(sys.argv[2])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("¡Tienen que ser enteros!")
    print(resta(operando1, operando2))
