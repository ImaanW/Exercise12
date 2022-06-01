import random
lottery_numbers = [] #here is the empty lists where the variables will be
for i in range(0,6):
#range function Use range(stop) to create a range of 0 to stop where stop is the number of lines desired.
    number = random.randint(1,50)
#number = variable for generated number = andomly generated number between the given range of 1,50
    while number in lottery_numbers:
#while the number previously generated is true(is the same) in the lottery_numbers = keep generating a new number untill false(previosuly picked)
        number = random.randint(1,50)
    lottery_numbers.append(number)
#gather all 1 randomly generated and add them to the list called lottery_numbers each time going roung the loop
print(lottery_numbers)

