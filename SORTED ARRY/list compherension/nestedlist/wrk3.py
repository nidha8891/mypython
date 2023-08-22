items=[
    [1,"potatto",45,"veg",10],
    [1,"tomatto",40,"veg",20],
    [1,"onion",35,"veg",0],
    [1,"brinjal",50,"veg",0],
    [1,"fish",145,"nonveg",10],
    [1,"chicken",145,"nonveg",10],
    [1,"egg",6,"nonveg",100]

]
# print(len(items))

# in_stock=[ite[1]  for ite in items if ite[4] > 0 ]
# print(in_stock) 
# out_stock=[ite[1] for ite in items if ite[4]==0]
# print(out_stock)
# veg=[ite[1] for ite[2] in items  if ite[3]=="veg"]
# print(veg)
# products=[ite[1]  for ite in items if ite[2] in range(50,100)]
# print(products)

veg_product=[ite[1]  for ite in items if ite[2] in range(40,80) and ite[3]=="veg"]
print(veg_product)