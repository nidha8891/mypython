f=open("C:\\Users\\nidha\\OneDrive\\Desktop\\mypythonprogram\\decisionmakeingstatement.py\\users\\data.txt","r")
users=[]

for line in f:
    text=line.rstrip("\n")
    name,followers,following=text.split(",")
    print(name,followers,following)
