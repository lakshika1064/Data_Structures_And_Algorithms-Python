

def binary_search(arr,value):		#function of iterative binary search
	low=0
	high=len(arr)-1
	while low<=high:
		mid=(low+high)//2
		if arr[mid]> value:
			high=mid-1
		elif arr[mid]<value:
			low=mid+1
		else:
			return mid
	return -1



A=[12,13,14,67,78,90,124]
print("Value searched is at position",end=" ")
print(binary_search(A,90))


