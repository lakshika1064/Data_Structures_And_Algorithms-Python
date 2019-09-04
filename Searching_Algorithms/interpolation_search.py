#In real life if we need to find a word starting from d then we know it will be somewhere in the starting of the dictionary so we will start searching it from starting not from mid or from the last. Same theory is applied on interpolation search

def interpolation_search(array,value)
	low=0
	high = len(array)-1
	while array[low]<= value and array[high]>=value			#to check if the value is on the list
		mid=(low+ ( (value - array[low])) * (high-low)
		    /(array[high]-array[low]))				#------(1)
		if array[mid]<value:
			low=mid+1
		elif array[mid]>value:
			high=mid -1
		else:
			return mid
	if array[low]==value:
		return low
	return None


#(1)-----in equation we are using slope formula in which (x1,y1) are (array[low],low) and (x2,y2) are (array[high],high)
