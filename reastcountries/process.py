from json import load
with open("C:\\Users\\nidha\\OneDrive\\Desktop\\mypythonprogram\\reastcountries\\rest.json",encoding="UTF-8") as f:
    data=load(f)

print(len(data))

# for m in data:
    # print(m.get("name"))

    # all_countery=[ m.get("name") for m in data]

# for m in data:
    # print(m.get("region"))

# all_regions={m.get("region") for m in data}
# print(all_regions)


# all_asian= [ m.get("name")  for m in data if m.get("region")=="asia"]
# print(all_asian)

    # if m.get("name")=="afganisthan":
    #   ( m.get("population"))

# print[for m in data if]



# borders=[ m.get("borders") for m in data if m.get("name")=="India"][0]
# print(borders)

# country_border_name=[ m.get("name") for m in data if m.get("alpha3Code") in borders][0]
# print(country_border_name)


for m in data:
    if m.get("")


