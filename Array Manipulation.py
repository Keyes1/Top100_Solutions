def arrayManipulation(n, queries):
    ar=[0]*(n + 1)
    for i in queries:
        a,b,k= i
        ar[a - 1]+=k
        if b<=len(ar): 
            ar[b] -=k
            
    highest=temp=0
    for i in ar:
        temp +=i
        if highest<temp:
            highest=temp
    return highest
