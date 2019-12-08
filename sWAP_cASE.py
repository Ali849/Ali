def swap_case(s):
    swaplist=[]

    for i in range(0,(len(s))):
     y=s[i]
     i+=1
     if y.isupper():
       swaplist.append(y.lower())
     elif y.islower():
        swaplist.append(y.upper())
     else:
       swaplist.append(y)
    
    return("".join(swaplist))
