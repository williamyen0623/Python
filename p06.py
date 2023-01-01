import random as r
def p06(nums = [3,3], target = 6):
    output_list=None
    # ↓程式區域↓
    output_list = []
    while(True):
        a = r.randint(0, len(nums)-1)
        while(True):
            b = r.randint(0, len(nums)-1)
            if(b!=a):
                break
        if(nums[a]+nums[b]==target):
            output_list.append(a)
            output_list.append(b)
            break
    output_list.sort()
    # ↑程式區域↑
    return output_list

print(p06())