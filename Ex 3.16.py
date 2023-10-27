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
second_largest = -1
largest = -1
for a in range (len(num_list)):
	if largest < num_list[a]:
		largest = num_list[a]
	
#Second loop statement that runs through the same list and looks for the second largest value in the list
#Uses an extra conditional statement that makes sure num_list[a] is greater than second_largest and doesn't equal the largest value
for a in range (len(num_list)):
	if second_largest < num_list[a]:
		if num_list[a] != largest:
			second_largest = num_list[a]
			
#Print the final statement that displays the two largest values in the list
print('The largest value is: ', largest, 'The second largest value is: ', second_largest)
	