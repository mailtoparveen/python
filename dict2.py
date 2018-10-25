#!/usr/bin/python3

pets = {'bird':3.5,'cat':5.0,'dog':7.25,'gerbil':1.5}
user_input = input("enter pet name for whic you need to know price: ")

# print ("Pet price is",pets(user_input))

for (a,b) in pets.items():
#  print ("User input is {}. Now checking for pet {}".format(user_input,a))
 try:
  if a == user_input :
   print ("Pet value of {} is {}".format(user_input,b))
#  print (a,b)
 except:
  print ("Please check something went wrong")
  raise
