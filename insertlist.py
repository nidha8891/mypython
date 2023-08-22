# insert to add to a particular position in alist
# lst=[2,3,5,6]
# lst.insert(0,1)    #listname.insert(position of list,value to be add)
# print(lst)



# create a empty list
# emplst=[]
# print(emplst)

# get the size of

emplst=[]
print(emplst)
length=int(input("enter size of list:"))
for i in range(length):
    num=int(input(f" enter {i}th position ele :"))
    emplst.append(num)
print(emplst)
max_emplst=max(emplst)
print(max_emplst)
maxim=max_emplst+int(10)
emplst.insert(2,maxim)
print(emplst)
