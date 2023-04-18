def bin_gap(n):
    bi = format(n,"0b")
    cont = 0
    maxi = 0
    for s in range(bi.find("1"),bi.rfind("1")): #len(bi)):
        if bi[s]=="1":
            cont = 0
        if bi[s] == "0":
            cont += 1
            if maxi < cont:
                maxi = cont
    return(maxi)

print(bin_gap(14352323423450))
