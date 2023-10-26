#Exercise 3.16
"""  Use a loop to find the two largest values of 10 numbers entered"""

#create list for values to slot into
num_list = [] 

#while loop that reads inputs
for i in range (10):
	item = int (input('Please enter a number: '))
	num_list.append(item)

#Nested loops that compare the current index to the remainder of the list
#If a number in the list is bigger than the current index, the max value is replaced
for number in num_list:
	max = num_list[0]
	max2 = num_list[0]
	for a in range (len(num_list)):
		if max < num_list[a]:
			max = num_list[a]
		else:
			continue
			#Second loop statement that runs through the same list and looks for the second largest value in the list
			#If a number in the list is bigger than the current index and does not match the value of max, the max2 value is replaced
			if max2 != max and max2 < num_list[0]:
				max2 = num_list[a]
			else:
					continue
#Print the final statement that displays the two largest values in the list
print('The max value is: ', max, 'The second largest value is: ', max2)
	