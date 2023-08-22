class Employee:
     id=int
     name=str
     desig=str
     salary=int
#java,c++ => class name


     def __init__(self,id,name,salary,desig):       
        
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary

     def get_emp(self):
        print(self.name,self.id,self.salary,self.desig)





obj=Employee("nihala",345,77000,"dm")
obj.add_employee()

obj.add_employee("nidha",234.88000,"hm")
obj.get_employee()
