# coding=utf-8
# !/usr/bin/python
''' 
Deque
Use as queue
 '''

from collections import deque
queue = deque(["Eric", "John", "Michael"])
print queue

queue.append("Terry")
queue.append("Graham")
print queue

print queue.popleft()
print queue.popleft()
print queue



