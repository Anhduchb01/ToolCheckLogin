
import os
import time
# Get the current folder
current_folder = os.getcwd()
with open(current_folder + '/credit.txt', 'r') as f:
	list_creadit = []
	for line in f:
		number, month, year = line.strip().split('|')
		list_creadit.append([number, month, year])
print(list_creadit)
print(len(list_creadit))
for i in range(len(list_creadit)-1,-1,-1):
	# Process the element
	print(i)
	element = list_creadit[i]
	print(element)
	# Delete the element from the list
	list_creadit.pop(-1)
	

	# Write the updated list back to the file
	with open(current_folder + '/credit.txt', 'w') as f:
		for item in list_creadit:
			f.write('|'.join(item) + '\n')
	time.sleep(5)




