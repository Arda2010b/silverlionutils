import math

class mathf:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / y

    @staticmethod
    def sqrt(x): 
        return math.sqrt(x)

    @staticmethod
    def powerof(x, y):
        return x ** y

    @staticmethod
    def modulo(x, y):
        return x % y

    @staticmethod
    def average(x, y):
        return (x + y) / 2

    @staticmethod
    def sin(x):
        return math.sin(x)

    @staticmethod
    def cosine(x):
        return math.cos(x)

    @staticmethod
    def tangent(x):
        return math.tan(x)

    @staticmethod
    def log(x):
        return math.log(x)

    @staticmethod
    def pythagorus(x, y):
        return math.sqrt(x**2 + y**2)

# usage 
mathf.add(2,3)
