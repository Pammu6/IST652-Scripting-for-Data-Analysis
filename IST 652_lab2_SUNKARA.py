# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:28:18 2019

@author: KARTHEEK SUNKARA
"""
#Lab 2 assignment

#1). Given a list of non-empty tuples, write a sort expression that will sort in increasing order by the last element in each tuple
# Solution for question 1
a=[(2,3),(1,6),(3,3),(9,0),(6,5)]
a=sorted(a, key=lambda x: x[-1]) 
#x[-1] indicates the element based on which the sorting is to be done

#Define at least two lists with tuples of different lengths and show the same sort expression executing against both lists. 
# Solution for question 2
b=[(2,0,1),(2,4),(6,0),(8,9),(2,0,5)]
c=[(3,0),(9,5),(6,6,0),(2,7,1),(0,1)]

#sorting list/tuple based on the last value of its sublists/tuples
b=sorted(b,key=lambda x: x[-1])
c=sorted(c,key=lambda x: x[-1])

#2). Given the grades of 21 students in a class, write a program which will print to console: 
grades = [['Harry', 89], 
          ['Berry', 82], 
          ['Tina', 78], 
          ['Akriti', 92], 
          ['Harsh', 93], 
          ['Ben', 68], 
          ['Geeta', 70], 
          ['Tao', 75], 
          ['Kelly', 100], 
          ['Miguel', 99], 
          ['Ashley', 80], 
          ['Marta', 92], 
          ['Jackson', 90], 
          ['Freddy', 85], 
          ['Lilly', 70], 
          ['Albert', 75], 
          ['Watson', 100], 
          ['Juan', 99], 
          ['Belle', 92], 
          ['Nikhil', 91], 
          ['Freddy', 100], ]

#The maximum grade and the student(s) who recieved it
maxval=max([sublist[-1] for sublist in grades])
#The minimum grade and the student(s) who recieved it
minval=min([sublist[-1] for sublist in grades])
#initiating empty lists.
maxmem=[]
minmem=[]
#Finding the corresponding entry for maxval and minval
[maxmem.append(i[0]) for i in grades if i[-1]==maxval]
[minmem.append(i[0]) for i in grades if i[-1]==minval]

#average is sum/number
average=sum(h[-1] for h in grades)/len(grades)
#3) Given the same grades as the previous question, write a program which will print to console
#sorting the grades and finding the median
d=sorted(grades,key=lambda x: x[-1])
d[round(len(grades)/2)+1]

#4) Given the following dictionary of people and their ages, print the dictionary items as a sorted list of strings in the following format: 
age_dict = {'Harry': 30, 
            'Berry': 22, 
            'Tina': 25, 
            'Akriti': 32, 
            'Harsh': 61, 
            'Ben': 47, 
            'Geeta': 55, 
            'Tao': 39, 
            'Kelly': 27, 
            'Miguel': 29, 
            'Ashley': 29, 
            'Marta': 33, 
            'Jackson': 19, 
            'Freddy': 18, 
            'Lilly': 44, 
            'Albert': 23, 
            'Watson': 19, 
            'Juan': 41, 
            'Belle': 32, 
            'Nikhil': 22, } 

#copying dict keys and values into an empty list as needed
d=[]
j=[]
for key, value in age_dict.items():
    temp = [key,value]
    d.append(temp)
d=sorted(d,key=lambda x: x[-1])
for x in d:
    j.append(str(x[1])+'-'+str(x[0]))
    
    
#5) Using either a loop or a list comprehension - write a program which generates the first 20 even squares. 
#Even number squares are found
for i in range(21):
    if i>0:
        if i%2==0:
            print(i**2)


zoo_animals = {'giraffe': 3, 
               'elephant': 4, 
               'lion': 9, 
               'hippopotamus': 1, 
               'crocodile': 25, 
               'wild dog': 5, 
               'hyena': 10, 
               'zebra': 9, 
               'anaconda': 25, 
               'python': 5, 
               'kangaroo': 10, 
               'cheetah': 2, 
               'leopard': 1} 

e=[]

#comparing each new key value with the elements of e
#if not equal then appended
for key,value in zoo_animals.items():
    if key not in e:
        e.append(key)

#The number of distinct species
print('The number of distinct species:' +str(len(e)))

#The total number of animals 
print('The total number of animals:'+ str(sum(g for g in zoo_animals.values())))

#the average number of animals for key species is its corresponding value
r=[]
for key,value in zoo_animals.items():
    print('The average number of animals for specie' +' '+str(key)+' '+'is'+' '+str(value))
    r.append([key,value])

#using max function to find the maximum animalcount value in sublists of r
print(str(max(f[1] for f in r)) +' '+'animal count is the highest number in the species')
h=max(f[1] for f in r)
#if the max count h matches the sublist second element in r then the first element i.e the corresponding species is printed
for v in r:
    if v[1]==h:
        print(v[0])

#similar to the method followed above
#finding the least value and storing it in h
#finding the corresponding sublist entries for the value h in list r         
print(str(min(f[1] for f in r)) +' '+'animal count is the least number in the species')
h=min(f[1] for f in r)
for v in r:
    if v[1]==h:
        print(v[0])   




            
            
    
    


 






        
        

        
        
        






    
    
    
