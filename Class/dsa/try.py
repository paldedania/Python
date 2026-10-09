
# var used
s = input("enter:")
t = input("enter: ")
ls = len(s)
lt = len(t)
sdic = {}
tdic = {}
if ls != lt:
    print("false") 

for i in s:
    if i in sdic:
        sdic[i] +=1
    else:
        sdic[i] = 1     
print(sdic)

for y in t:
    if y in tdic:
        tdic[y] +=1
    else:
        tdic[y] = 1     
print(tdic)

if sdic == tdic:
    print("ya")
    