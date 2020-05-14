n, k = input().split()
n, k = int(n), int(k)
if n == k or n > k:
	print(-1)

else:
	listAllPrice = []
	for i in range(1, n+1):
		listAllPrice.append(i)
	k_pryce= []
	for j in range(1, k+1):
		k_pryce.append(j)
	bigest_pryce = list(set(listAllPrice) - set(k_pryce))
	rez = ''
	for q in range(len(bigest_pryce)):
		if q < len(k_pryce):
			rez += str(bigest_pryce[q])
			rez += str(k_pryce[q])
		else:
			rez += str(bigest_pryce[q])
	print(rez)