#!/usr/bin/env python

import fileinput
import os
import sys
list1 = list()
#adjaceny = list()
predecesor = list()
distance = list()
read_lines = 0
INF = float("inf")
#def floydwarshall(graph):
#reading in from example.input and splitting the first part
for line in fileinput.input():
                    read_lines = read_lines + 1
                    splt = line.split()
                    list1.append(splt)

for p in range(1, read_lines+1):
        distance.append([INF] * read_lines)
        predecesor.append([0]*read_lines)

#storing all the distanc ebetween vertexes by separating them at comma with split         
for i in list1:
    vertex = int(i[0])
    for r in i[1:]:
        s = r.split(',')
        distance[vertex][int(s[0])] = int(s[1])
        distance[int(s[0])][vertex] = int(s[1])

#for i in range(1,read_lines +1):
 #   distance[i-1][i-1] = 0
  #  predecesor[i-1][i-1] = '-'

#finding the shortest path between nodes 
for i in range(1, read_lines+1):
	for j in range(1,read_lines+1):
		predecesor[i-1][j-1] = i-1
		for k in range(1,read_lines+1):
			if distance[i-1][k-1] + distance[k-1][j-1] < distance[i-1][j-1]:
				distance[i-1][j-1] = distance[i-1][k-1] + distance[k-1][j-1]
				predecesor[i-1][j-1] = k-1
#showing that i*i=0, because it will be a loop
for i in range(1,read_lines +1):
    distance[i-1][i-1] = 0
    predecesor[i-1][i-1] = '-'

a = 0
print "Distance Matrix:"
print 'n', '   ',
for x in range(1, read_lines + 1):
        print x-1, '   ',
print '    '

for i in distance:
    print a, '   ',
    for j in i:
        print j,
	print '   ',
    print '   '
    a = a + 1

print "Predecessor Matrix:"
print '\nn', '   ',
for x in range(1, read_lines + 1):
        print x-1, '   ',

print '   '

a=0
for j in predecesor:
  print a, '   ',
  for k in j:
	print k,
	print '   ',
  print ''
  a = a + 1
