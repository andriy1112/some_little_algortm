nums = [4,1,2,1,2]


def ger(arr):
	if arr == 0:
		return 0
	i = 0
	for j in range(1, len(arr)):
		if arr[j] != arr[i]:
			i += 1
			arr[i] = arr[j]

	return i+1


print(ger(nums))
