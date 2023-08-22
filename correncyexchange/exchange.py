from json import load

with open("C:\Users\nidha\OneDrive\Desktop\mypythonprogram\correncyexchange\db.json") as f:
    data=load(f)

rates=data.get("conversion_rate")  
amount=int(input("enter a amount you want tp exchange  :>"))
fromcurrencycode=input("enter source currency code  :>")
tocurrencycode=input("enter destination currency code  :>")

from_code_rate=rates.get(fromcurrencycode)
to_currecy_code_rate=rates.get(tocurrencycode)

result=(amount/from_code_rate)*to_currecy_code_rate
print(result)
  