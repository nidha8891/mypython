class users:

    data=[
        {"id":1,"username":"jhon","email":"jhon@gmail.com","password":"password@123"},
        {"id":2,"username":"hari","email":"hari@gmail.com","password":"password@123"},
        {"id":3,"username":"ravi","email":"ravi@gmail.com","password":"password@123"},
        {"id":4,"username":"vijay","email":"vijay@gmail.com","password":"password@123"},
        {"id":5,"username":"vinu","email":"vinu@gmail.com","password":"password@123"},
        {"id":6,"username":"tom","email":"tom@gmail.com","password":"password@123"},
]
    
    def get(self):          #get=> listing element
         return self.data
    
    def retrieve(self,id):     #one detail return
         return [ u for u in self.data if u.grt("id")==id]
    
    def post(self,obj):        # one resource creating
         self.data.append(obj)
         
         def destroy(self,id):    # deleting ressource
          obj=[u for u in self.data if u.get("id")==id]
          self.data.remove(obj)

          def put(self,id,value):
            obj=[u for u in self.data if u.get("id")==id]
            pos=self.data.index(obj)
            self.data[pos]=value




     
    


obj=users()
# data={"id ":5,"username":"vinus","emails":"vinus1232gmail.com","password":"pass123"}
# obj.put(5,data)

print(obj.retrieve(5))










