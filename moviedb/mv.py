from json import load
with open("C:\\Users\\nidha\\OneDrive\\Desktop\\mypythonprogram\\moviedb","r",encoding="UTF-8") as f:
    data=load (f)


gener_filter={m.get("title") for m in data for g in m.get ("geners") if g in ["comdey","fantasy"]}
print(gener_filter)


yc={}
for m in data:
    year=m.get("year")
    if year in yc:
        yc[year]+=1
    else:
        yc[year]=1
print(yc)

print(max(yc, key=lambda k: yc.get(k)))
print(min(yc, key=lambda k: yc.get(k)))


