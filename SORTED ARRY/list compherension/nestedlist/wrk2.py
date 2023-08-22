mobiles=[
    [100,"redminote12",23000,"5g"],
    [101,"oneplusnord",32000,"5g"],
    [102,"iphnoe14",123000,"5g"],
    [103,"s23ultra",133000,"5g"],
    [104,"pexel12",43000,"5g"],
    [105,"nothing",13000,"4g"],
    [106,"galaxya52",23000,"5g"]
]
print(len(mobiles))

# mobiles_names=[mob[1] for mob in mobiles]
# print(mobiles_names)


# mobiles_names=[mob[1] for mob in mobiles if mob[3]=="4g"]
# print(mobiles_names)


# mobiles_names=[mob[1]for mob in mobiles if mob[2]<30000]
# print(mobiles_names)

# mobiles_names=[mob[1] for mob in mobiles if mob[2] in range(30000,50000)]
# print(mobiles_names)


mobiles_names=[mob[1] for mob in mobiles  if mob[2]<25000 and mob[3]== "5g"]
print(mobiles_names)

