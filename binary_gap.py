def bin_gap(n):
    bi = format(n,"0b")
    cont = 1
    maxi = 2
    for s in range(bi.find("1"),bi.rfind("1")): #len(bi)):
        if bi[s]=="1":
            cont = 0
        if bi[s] == "0":
            cont += 1
            if maxi < cont:
                maxi = cont
    return(maxi)

print(bin_gap(14352323423450))
#  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


# nueva linea de miguel
