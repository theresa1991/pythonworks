num=[10,20,30,40,50,-8,-5]
psum=0
nsum=0
for n in num:
    if(n>0):
        psum=psum+n
    elif(n<0):
        nsum=nsum+n
print(psum)
print(nsum)