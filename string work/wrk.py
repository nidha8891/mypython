tex="one 100 and fifty 5"
 
word=tex.split(" ")
for w in word:
    if w.isdigit():
        print(w)

        num=[w  for w in tex.split(" ") if w.isdigit()]
        print(num)


text="england promised to continue its aggressive approch to test cricket"
vowel= {"a","e","i","o","u"}
words= text.split()
wor=[w for w in text.split(" ") if w[0].casefold()in vowel]
print(wor)



# longest words text="hello" 

# text="hello i am in kakkanad"
# word=text.split(" ")
# max(len(word,key=lambda w:len(w)))
# print(word)



