weather=[
    {"tvm":25},
    {"apy":23},
    {"kty":27},
    {"idk":18},
    {"ekm":29},
    {"tsr":28},
    {"tvm":26},
    {"apy":22},
    {"kty":28},
    {"idk":19},
    {"ekm":30},
]


temp={}
for t in weather:
    for k,v in t.items():
        d_name=k
        c_temp=v
    if d_name in temp:
          old_temp=temp[d_name]
          if c_temp>old_temp:
           temp[d_name]=c_temp
    else:
           temp[d_name]=c_temp

print(temp)
        



