''' 
Author Loc VU
Created on 26.9.2015
'''

def insert_sort(array):
	for i in range(1, len(array)):
		key = array[i]
		j = i-1
		while j >= 0 and key < array[j]:
			array[j+1] = array[j]
			j -= 1
		array[j+1] = key
	return array

if __name__ == '__main__':
	list = [23,434,23,23,22,33,34,5,65]
	print insert_sort(list)
