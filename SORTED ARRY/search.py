lst=[1,3,4,8,9]
elemt=4
is_found=False
for i in range(0,len(lst)):
    if elemt==lst[i]:
        is_found=True
        break
    print("found"if is_found==True else "not found" )