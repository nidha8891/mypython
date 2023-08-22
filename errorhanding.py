# # num2= (int (input("enter a value for number2")))

# try:

#     res=num1/num2
#     print("result,res")
# except Exception as e:
#     print ("Exception occured")

# print("db commit1")
# print("db commit")


# lst=[20,30,30,10,50]
# location=int(input("enter location to fetch value from list"))

# try:                      # error
#     print(lst[location])
# except Exception as e:
#     print(e.args)    # error
# finally:
#    print("dbcommit")
#    print("filw read")


# age=int(input("enter age"))

# if age<18:
#     raise Exception("invalid age")
# else:
#     print("valid")


num= input("enter number")

if type(num)==int:
    print(num**3)
else:
    raise Exception("operand must be inetger")




