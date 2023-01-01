def p08(n=13):
    output=None
    # ↓程式區域↓
    a = False
    b = False
    while n % 4 == 0:  # 用4
        n //= 4
    if n % 8 == 7:  #7 = 4 + 1 + 1 + 1 
        output = 4
        a = True
    if(a == False):
        for i in range(n + 1):
            temp = i * i
            if temp <= n:
                if int((n - temp) ** 0.5) ** 2 + temp == n:
                    output = 1 + (0 if temp == 0 else 1)
                    b = True
                    break
            else:
                break
        if(b == False):
            output = 3
    # ↑程式區域↑
    return output
print(p08())