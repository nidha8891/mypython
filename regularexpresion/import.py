# import packagename

import re
sen="joel is a very good student in may batch"
sen2="joel is a very good student in may batch"

# x=re.search("^joel",sen)
# y=re.search("^joel",sen)
# en=re.search("joel$",sen)
st_en=re.search("^joel.*batch$",sen)
st_en2=re.search("^joel.*batch$",sen2)
print(st_en)
# print(x)
# print(y)
# print(en)