word=input("enter a string")
out=input("enter another word")

str_word=sorted(word)
str_out=sorted(out)
print("anagram" if str_word==str_out else "not anagram")