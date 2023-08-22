fread=("C:\Users\nidha\OneDrive\Desktop\mypythonprogram\lambdafunction\numbers\data.txt","r")
fwrite=("C:\Users\nidha\OneDrive\Desktop\mypythonprogram\lambdafunction\numbers\leapdata.txt","w")

for line in fread:
    years=int(line.rstrip("\n"))
    if(years %100==0 and years%400==0 ):
        fwrite.write(str(years)+"\n")
    elif(years %100 !=0 and years%4==0):
        fwrite.write(str(years)+"\n")

