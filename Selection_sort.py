''' 
Author Loc VU
Created on 26.9.2015
'''

def selection_sort(array):
	len_array = len(array)
	for i in range(0, len_array):
		for j in range(i, len_array):
			if array[i] > array[j]:
				array[i], array[j] = array[j], array[i]
	return array

if __name__ == '__main__':
	list = [2,3,41,3,4,5,3,33,232,2,12,3]
	print selection_sort(list)