def queens(index):
	if promising(i):
		if i == n:
			print col
		else:
			for j in range(1, n+1):
				col[i+1] = j
				queens(i + 1)

def promising(index):
	k = 1
	switch = True
	while k < i and switch:
		if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
			switch = False
		k +=1
	return switch

col = 
