num1=10
num2=40
num3=50
first=0
second=0
thrid=0

if(num1>num2)and(num1>num3):
    first=num1
    if(num2>num3):
     second=num2
     thrid=num3
    else:
     second=num3
     thrid=num2
elif(num2>num1)and(num2>num3):
    first=num2 
    if(num1>num3):
        second=num1
        thrid=num3
    else:
         second=num3
         third=num1
elif(num3>num1)and(num3>num2):
    first=num3
    if(num1>num2):
         second=num1
         third=num2
    else:
          second=num2
          third=num1
          print(second)




