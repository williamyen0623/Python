

def p03(x=-123):
    reverse=None
    # ↓程式區域↓
    reverse = ''
    x = str(x)
    for i in x:
        if(i=='-'):
            pass
        else:
            reverse = i + reverse
    if('-' in x):
        reverse = '-' +reverse
    reverse = int(reverse)
    # ↑程式區域↑
    return reverse

print(p03())
print(type(p03()))