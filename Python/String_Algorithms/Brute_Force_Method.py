def brute_force_method(stri,pattern):
	if not pattern : return 1
	for i in range(	len(stri)-len(pattern)+1):
		stri1=i; patterni=0
		while stri1<len(stri) and patterni<len(pattern) and stri[stri1]==pattern[patterni]:
			stri1+=1
			patterni+=1
		if patterni==len(pattern) : return i
	return -1

print (brute_force_method("xxxyabcbcaaaabcabc","abc"))

