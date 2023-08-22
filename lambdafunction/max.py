# word={"hello","hai"}
# print(max(word,key=lambda w:len(w)))
# print(min(word,key=lambda w:len(w)))


# lst=[20,30,10,5]
# print(sorted(lst))
# print(sorted(lst,reverse=False)




text="aabbbccbnm"
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1



print(min(wc,key=lambda k:wc.get(k)))