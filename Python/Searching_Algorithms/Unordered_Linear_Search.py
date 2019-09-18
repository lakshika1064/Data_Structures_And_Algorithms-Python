def un_ordered_linear_search(arr,value):
	for i in range(len(arr)):
		if arr[i]==value:
			return i
	return -1

A=[534,246,933,127,277,321,454,798,277]
print(un_ordered_linear_search(A,277))
