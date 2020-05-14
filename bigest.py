def max22(L,left,right):
    if len(L)==1:
        return L[0]
    mid = (left+right+1)//2
    left_L = [L[i] for i in range(left, mid)]
    right_L = [L[i] for i in range(mid, right+1)]
    a = max22(left_L,  0 , len(left_L)-1)
    b = max22(right_L, 0 , len(right_L)-1)
    return max(a,b)

def max_list22(L):
    return max22(L,0,len(L)-1)

print(max_list22([4,8,15,16,23,42]))