def binary_search(array,value,low=0,high=-1):		#function of Recursive binary search
	if not array:return -1			#condition for value not in the list	
	if(high==-1):
		len(array)-1				
	if low==high:
		if array[low] == value: return low
		else : return -1
	mid=(low+high)//2
	if array[mid]> value:
		return binary_search(array,value,low,mid-1)
	elif arr[mid]<value:
		return binary_search(array,value,mid+1,high)
	else:
		return mid



A=[12,13,14,67,78,90,124]
print("Value searched is at position",end=' ')
print(binary_search(A,90))
