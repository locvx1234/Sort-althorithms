''' 
Author Loc VU
Created on 26.9.2015
'''

def insert_sort(array):
	 merge_sort(seq):
	if len(seq) <= 1:
		return seq
	mid = int(len(seq)/2)
	left = merge_sort(seq[:mid])
	right = merge_sort(seq[mid:])
	return merge(left,right)

def merge(array_1, array_2):
	index_1 = 0
	index_2 = 0
	array = []
	len_array_1 = len(array_1)
	len_array_2 = len(array_2)
	
	while index_1 < len_array_1 and index_2 < len_array_2:
		if array_2[index_2] <= array_1[index_1]:
			array.append(array_2[index_2])
			index_2+=1
		else:
			array.append(array_1[index_1])
			index_1+=1
	while index_1 < len_array_1:
		array.append(array_1[index_1])
		index_1+=1
	while index_2 < len_array_2:
		array.append(array_2[index_2])
		index_2+=1
	return array

if __name__ == '__main__':
	list = [2,3,2,43,12,211]
	print merge_sort(list)


