pattern="ASSCVA"
char_count={}
rec_char=[]
for c in pattern:
    if c in char_count:
        rec_char.append(c)
    else:
        char_count[c]=1
print(rec_char[1])
