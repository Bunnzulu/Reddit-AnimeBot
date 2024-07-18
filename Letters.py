from collections import Counter

Letters = "q,w,e,r,t,y,u,i,o,p,l,k,j,h,g,f,d,s,a,x,c,v,b,n,m"

def CountLetters(text:str):
    n = 1
    Result = Counter(text)
    Most_used_letter = Result.most_common(n)
    while Most_used_letter[n-1][0] not in Letters.split(","):
        n += 1
        Most_used_letter = Result.most_common(n)
    Most_used_letters = f"Most used letter is {Most_used_letter[n-1][0]}.\n It appears {Most_used_letter[n-1][1]} times"
    All_Letters = f"Letters used are {list(filter(lambda x:x in Letters.split(","),set(Result.elements())))}."
    return Most_used_letters,All_Letters



