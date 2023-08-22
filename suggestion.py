users=["sachin","kohli","sehwag","rahul","raina","nidha"]
sachin_followers=["kohli","sehwag","rahul"]
suggst=[]
for followers in users:
 if followers !="sachin" and not in sachin_followers:
  suggst.append(followers)
print(suggst) 