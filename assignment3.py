# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 09:53:57 2022

@author: Kassaundra
"""
# VARIABLE OP EXERCISES
sub_code = "sub"
subnr_int = 2
subnr_str = "2"


print(sub_code+subnr_str)
#print(sub_code+subnr_int)
# python doesn't know how to add an integer and a string, so it gives an error that they can't be added

print(sub_code+" "+subnr_str)
print(sub_code+" "+(subnr_str*3))
print((sub_code+subnr_str)*3)
print((sub_code*3)+(subnr_str*3))

# LIST OP EXERCISES
import numpy
numlist = [1,2,3]
numarr = numpy.array([1,2,3])
print(numlist*2)
print(numarr*2)
# multiply list = prints list multiple times
# multiply array = multiply the values stored in the array

strlist = ['do','re','mi','fa']
print([(strlist[0]*2),(strlist[1]*2),(strlist[2]*2),(strlist[3]*2)])
print(strlist*2)
print([strlist[0],strlist[0],strlist[1],strlist[1],strlist[2],strlist[2],strlist[3],strlist[3]])
print([strlist[0],strlist[0]],[strlist[1],strlist[1]],[strlist[2],strlist[2]],[strlist[3],strlist[3]])

# ZIPPING EXERCISES
import itertools

faces = ['face1.png','face2.png','face3.png','face4.png','face5.png' ]
houses = ['house1.png','house2.png','house3.png','house4.png','house5.png']
cues = ['cue1','cue2']
Trials = list(itertools.product(faces,houses,cues))+list(itertools.product(houses,faces,cues))
numpy.random.shuffle(Trials)
print(Trials)


# INDEXING
colors = ['red','orange','yellow','green','blue','purple']
print(colors[-2])
print(colors[-2][2:])
del colors[5]
colors.append('indigo')
colors.append('violet')
print(colors)

# SLICING
list100 = []
for i in range(101) : 
    list100.append(i)
print(list100[:10])
print(list100[-2::-2])
print(list100[:-5:-1])
print(list100[40:44] == [39,40,41,42,43])