''' 
Author Loc VU
Created on 26.9.2015
'''

def bubble_sort(array):
	for i in range(0, len(array) ):
		for j in range(0, len(array)-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
	return array

if __name__ == '__main__':
	list = [1,3,5,3,121,3,5,7,4,23,31]
	print bubble_sort(list)

