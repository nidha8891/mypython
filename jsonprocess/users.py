from json import load

with open("C:\\Users\\nidha\\OneDrive\\Desktop\\mypythonprogram\\jsonprocess\\data.json","r") as f:
    data=load(f)


    print(data)

    for u in data:
        print(u.get("name"))

# print(max(data,key=lambda s:s.get("total")))

# print(sorted(data,reverse=True,key=lambda s:s.get("total")))

print(u.get("name") for u in data if u.get("course")=="bca" )