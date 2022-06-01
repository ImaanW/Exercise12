#QUESTION1
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['Oke']
print(cheese)
#Orginally this printed the oke and o k e as it was not in brackets
#no print statement
#To add two items  you... there are two ways to do it
#cheese += ['Cheshire','BlueCheese']
cheese.extend(['Cheshire','BlueCheese'])
print(cheese)

#QUESTION2
tup = 'Hello'
print(len(tup))
#here it is printing the lenghth of the string tup which is 5

tup = 'Hello',
print(len(tup))
#counting the number of values in the tuple a commar',' is what makes it a tuple