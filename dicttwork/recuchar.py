pattern="ABBDC"
char_count={}
for c in pattern:
    if c in char_count:
        print(f"first recursive is {c}")

        break
    else:
        char_count[c]=1



