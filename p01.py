def p01(*nums):
    minnum=None
    # ↓程式區域↓
    minnum = min(nums)
    minnum = float(minnum)
    # ↑程式區域↑
    return minnum

print(p01(9,1))
print(type(p01(9,1)))