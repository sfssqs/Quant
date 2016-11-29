# coding=utf-8
# !/usr/bin/python

print range(0, 11)

print '--------------------------------------------------'
print ''' Filter : filter(fuction, sequence) '''
def f(x):
    return x % 3 == 0 or x % 5 == 0
print filter(f, range(2, 25))

print '--------------------------------------------------'
print ''' Map: map(function, sequence) '''
def cube(x):
    return x*x*x
print map(cube, range(1, 11))

print '--------------------------------------------------'
print ''' Reduce: reduce(function, sequence) '''
def add(x, y):
      return x+y
print reduce(add, range(1, 11))
