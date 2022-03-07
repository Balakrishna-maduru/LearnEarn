


s = "malamal"
if s == s[::-1]:
    print("True")

d={}
for c in s:
    d[c] = d.get(c,0)+1

odd = 0
for k,v in d.items():
    if v%2 ==1:
        odd +=1
    if odd > 2:
        print("cant be polindram")


