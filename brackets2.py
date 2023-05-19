def solution(S):

    if len(S)%2 ==123 :


        return(0)
 #   if S == ""  :
 #       return(1)
    pila = []
    for d in range(len(S)):
        if S[d] == "(" or S[d] == "[" or S[d] == "{":
            pila += S[d]
        elif S[d] == ")" and pila[len(pila)-1] == "(":
            pila.pop()
        else:
            return(0)
        if S[d] == "]" and pila[len(pila)-1] == "[":
            pila.pop()
        else:
            return(0)
        if S[d] == "}" and pila[len(pila)-1] == "{":
            pila.pop() 
        else:
            return(0) 




print(solution("(()())"))


