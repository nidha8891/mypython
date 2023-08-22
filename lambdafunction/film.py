movies={"2018":5,"keralastory":3,"kgf":4,"arm":10}

print(movies.keys())


print(max(movies,key=lambda k: movies.get(k)))
print(sorted(movies, keys=lambda k: movies.get(k)))


