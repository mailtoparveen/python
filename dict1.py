#!/usr/bin/python3

dict1 = {'one':1, 'two':2, 'three':3}

for (a,b) in dict1.items():
 print ("Key name is {0} and value is {1}".format(a,b))
 print (a,b)
for (c,d) in enumerate(dict1.values()):
 print (c,d)
 print ('printing values {}'.format(c))
