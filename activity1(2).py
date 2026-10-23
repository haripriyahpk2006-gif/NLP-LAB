text="i like nlp i like pytho i like to study"
words=text.split()
print("words frequency")
for i in words:
    print(i,":",words.count(i))
    while i in words:
        words.remove(i)
    words=text.split()
    print("\nBingram Frequency")
    done=[]
    for i in range(len(words)-1):
        pair=words[i]+" "+words[]
