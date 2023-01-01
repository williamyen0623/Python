

def p07(version1='1.0', version2='1.0.0'):
    output=None
    # ↓程式區域↓
    l1 = str(version1).split(".")
    l2 = str(version2).split(".")
    print(l1,'\n',l2)
    print(int(l1[1]))
    print(int(l2[1]))
    a = False
    for i in (range(len(l1)) if len(l1)<len(l2) else range(len(l2))):
        if(int(l1[i])==int(l2[i])):
            pass
        elif(int(l1[i])<int(l2[i])):
            output = -1
            a = True
        else:
            a = True
            output = 1
            
        if(a == False):
            if(len(l1)==len(l2)):
                output = 0
            elif(len(l1) < len(l2)):
                output = 0
            else:
                output = 1
    # ↑程式區域↑
    return output
print(p07())