''' 
Author Loc VU
Created on 26.9.2015
'''

def shell_sort(array):
	dist = len(array)/2
	while dist > 0:
		for i in range(dist, len(array)):
			j = i
			temp = array[j]
			while array[j] < array[j-dist]  and j >= dist:
				array[j] = array[j-dist]
				j -= dist
			array[j] = temp
		dist /= 2
	return array

if __name__ == '__main__':
	list = [2,3,1,6,5,545,233,33,1,23,4]
	print shell_sort(list)

