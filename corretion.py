word="eagle"
input="egg"
wc={}

for c in word:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1

for ch in input:
    if ch in wc and wc[ch]> 0:
        wc[ch]-=1
    else:
        wc[ch]=1
        break
    break
print()
