word="nidhanasreen"
vowels={"a","e","i","o","u"}
v_count=0
c_count=0
for ch in word:
    if ch in vowels:
        c_count+=1
    else:
        v_count+=1
print(f"vowels count={v_count},consent count={c_count}")