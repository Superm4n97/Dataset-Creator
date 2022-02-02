from dataclasses import replace


def load_classes():
    txtFile = open(r'Scripts\classes.txt',"r+")
    lst = txtFile.readlines()
    lst.sort()
    nwList = ["Choose Class"]
    for st in lst:
        s = ""
        for i in range(0,len(st)-1):
            s = s+st[i]
        nwList.append(s)
    #print(tuple(nwList))
    txtFile.close()
    return nwList

#load_classes()