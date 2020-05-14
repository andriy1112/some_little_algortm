s = input()
t = input()
s = list(s)
t = list(t)
tt = t.copy()
ss = s.copy()
point2 = 0
ii = 0
jj = 0

point = 0
point_item = 0
abc = []
days = 0

for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            point += 1

#while ii <= len(s):
 #   while jj <= len(t):
  #      if s[ii-1] == t[jj-1]:
   #         del s[ii-1]
    #        del t[jj-1]
     #       point2 += 1
      #  jj += 1
    #jj = 0
    #ii += 1

while ii <= len(s):
    while jj <= len(t):
        if s[ii-1] == t[jj-1]:
            del s[ii-1]
            del t[jj-1]
            point2 += 1
        jj += 1
    jj = 0
    ii += 1


for g in range(len(ss)):
    if ss[g] in abc:
        point_item += 1
        if point_item >= 2:
            days += 1
            abc.clear()
    else:
        abc.append(ss[g])

print(days)
