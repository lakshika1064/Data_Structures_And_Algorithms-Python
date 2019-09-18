def ordered_linear_search(arr,value):
	for i in range(len(arr)):
		if arr[i]==value:
			return i
		elif arr[i]>value:
			return -1
	return -1
A=[34,48,52,57,60,68,77,102]
print(ordered_linear_search(A,60))
