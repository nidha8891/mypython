numbers=[2,7,8,9,12,13]
odd=[]
even=[]
for num in numbers:
     even.append(num) if num%2==0 else odd.append(num)   
    # if num%2==0:
    #  even.append(num)
    # else:
    #    odd.append(num)
print(odd)
print(even)
