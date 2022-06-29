text="hai hello hai hello my dear"
word_count={}
words=text.split()#[hai,hello,hai,hello,my,dear]
for w in words:
    if w in word_count:#hai in word_count
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)