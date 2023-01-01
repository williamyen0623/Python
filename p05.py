def p05(l1=[2,1], x=2):
    output_list=None
    # ↓程式區域↓
    l2 = []
    l3 = []
    for i in range(0, len(l1)):
        if(l1[i]<3):
            l2.append(l1[i])
        else:
            l3.append(l1[i])
    l2.sort()
    output_list = l2 + l3
    # ↑程式區域↑
    return output_list

print(p05())