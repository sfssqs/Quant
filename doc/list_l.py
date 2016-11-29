# coding=utf-8
# !/usr/bin/python

'''  
List 
can be used as stack
'''

''' initilize list '''
L = [1, 'JoinQuant', 1.4]

print 'L = ' + str(L)

''' Lenght '''
print 'len(L) = ' + str(len(L))

''' Head &  Tail element'''
print 'L[0] = ' + str(L[0])
print 'L[-1] = ' + str(L[-1])
print 'L[1:-1] = ' + str(L[1:-1])

'''  List add '''
print 'L + [2, 3, 4] = ' + str(L+[2, 3, 4])


a = [1, 2, 3, 3, 1234.5]
print '-------------------------------------------'
print 'a = ' + str(a)
print 'a.count(1) = ' + str(a.count(1))
print 'a.count(3) = ' + str(a.count(3))
print 'a.count(x) = ' + str(a.count('x'))

print '-------------------------------------------'
a.append(555)
print 'a.append(555) ' 
print 'a = ' + str(a)

print '-------------------------------------------'
a.extend([7, 8, 9])
print 'a.extend([7, 8, 9]) '
print 'a = ' + str(a)

print '-------------------------------------------'
a.insert(2, -1)
print 'a.insert(2, -1)'
print 'a = ' + str(a)

print '-------------------------------------------'
a.remove(2)
print 'a.remove(2)'
print 'a = ' + str(a)

print '-------------------------------------------'
a.reverse()
print 'a.reverse(2)'
print 'a = ' + str(a)

print '-------------------------------------------'
a.sort()
print 'a.sort()'
print 'a = ' + str(a)

print '-------------------------------------------'
print 'a.sort(cmp=None, key=None, reverse=True)'
a.sort(cmp=None, key=None, reverse=True)
print 'a = ' + str(a)

print '-------------------------------------------'
a.remove(3)
print 'a.remove(3)'
print 'a = ' + str(a)

print '-------------------------------------------'
del a[0]
print 'del a[0]'
print 'a = ' + str(a)

print '-------------------------------------------'
del a[2:4]
print 'del a[2:4]'
print 'a = ' + str(a)

print '-------------------------------------------'
a.pop()
print 'a.pop()'
print 'a = ' + str(a)

print '-------------------------------------------'
del a
print 'del a'
print 'a = ' + str(a)