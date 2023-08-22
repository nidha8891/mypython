films=[
    {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
    {"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
    {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
    {"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
    {"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
    {"language":"thamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
    {"language":"thamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
    {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
    {"language":"telungu","name":"kgf","rating":5,"year":2018,"genres":["action","romance","thriller"]}

]
#printing all names
films_name= [f.get("name") for f in films]

#print filter movies with gener=mystery
# for f in films:
    # if "mystery" in f.get("genres"):
        # print(f.get("name"))

# mystery_films=[f.get("name") for f in films  if "mystery" in f.get("genres")]
# print(mystery_films)

# malayalam_films=[f.get("language") for f in films ]

# print(max(films,key=lambda f:f.get("rating")))

# films_name=[ f.get("name")for f in films if f.get("year")==2023]
# print(films_name)

films_sort=sorted(films,reverse=True,key=lambda m:m.get("rating"))
print(films_sort)











