# coding=utf-8
# !/usr/bin/python

''' 
Tuple

Can not modify a tuple, but can connect and combination
Order set
'''

''' initilize empty tuple'''
tup1 = ()

'''initilize only one elements'''
tup1 = (50, )

''' initlize more elements '''
tup1 = ('physics', 'chemistry', 1997, 1998)

''' modify tuple '''
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print tup3

# if you do this, error occured
# tup1[0] = 100

''' Delete tuple, tuple item can not be deleted, but we can delete the whole tuple '''
del tup3

''' Any objects divided by comma can be recgnized like a tuple '''
print 'abc', -4, 13.2


tup = (1, 2, 1, 3, 5, 7, 8)
print 'tup = ' + str(tup)

'''Count x appear times in tuple'''
count = tup.count(1)
print 'tup.count(1) = ' + str(count)

'''Compare the two elements in tuple'''
print 'cmp(0, 1) = ' + str(cmp(0, 1))

'''Count elemets in tuple'''
print 'len(tup) = ' + str(len(tup))

'''Return the max value of tuple'''
print 'max(tuple) = ' + str(max(tup))

'''Return the min value of tuple'''
print 'min(tuple) = ' + str(min(tup))

'''Convert list to tuple'''
seq = [1, 2, 3, 4]
print 'tuple(seq) = ' + str(tuple(seq))
