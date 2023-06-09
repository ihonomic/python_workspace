""" Space & time complexity is reduced to 0(n) """
from timeit import timeit


def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-2) + fibo(n-1)


def fibo(n):
    """ Bottom - up """
    fibTable = [0, 1]
    for i in range(2, n+1):
        fibTable.append(fibTable[i-2] + fibTable[i-1])
    return fibTable[n]


fibTable = {1: 1, 2: 1}


def fibo(n):
    """ Top - down"""
    if n <= 2:
        return 1
    if n in fibTable:
        return fibTable[n]
    else:
        fibTable[n] = fibo(n-1) + fibo(n-2)
        return fibTable[n]


print(fibo(10))

# ==================================


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


hashTable = {}


def factorial(n):
    if n in hashTable:
        return hashTable[n]

    if n == 0:
        hashTable[n] = 1
        return 1
    else:
        hashTable[n] = n * factorial(n-1)
        return hashTable[n]


print(factorial(10))
