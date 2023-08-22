rates= {
    "USD": 1,
    "AED": 3.6725,
    "AFN": 86.0330,
    "ALL": 97.5499,
    "AMD": 386.9256,
    "ANG": 1.7900,
    "AOA": 824.0658,
    "ARS": 254.7465,
    "AUD": 1.5099,
    "AWG": 1.7900,
    "AZN": 1.6979,
  "BAM":1.7974
  }
  


amount=int(input("enter a amount you want tp exchange  :>"))
fromcurrencycode=input("enter source currency code  :>")
tocurrencycode=input("enter destination currency code  :>")

from_code_rate=rates.get(fromcurrencycode)
to_currecy_code_rate=rates.get(tocurrencycode)

result=(amount/from_code_rate)*to_currecy_code_rate
print(result)





