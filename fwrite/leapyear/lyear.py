years=[2000,1900,2002,2001]

f=open("C:\Users\nidha\OneDrive\Desktop\mypythonprogram\fwrite\leapyear\data.txt","w")

for y in years:
    if (y %100==0 and y %400==0):
        f.write(str(y))
    elif (y %100 !=0 and y %4==0):
        f.write(str(y))      