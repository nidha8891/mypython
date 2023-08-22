num=10
is_prime=True
for i in range(2,num):
    if(num%2==0):
        is_prime=False
        break
    if(is_prime==True):
        print(num,"is not a prime" )
else:
          print(num,"is a prime number")