lst=[[1,2],
     [4,50],
     [50,45],
     ]

for ls in lst:
    for num in ls:
        print(num)

allnumbers=[ num for ls in lst for num in ls if num > 5]
print(allnumbers)