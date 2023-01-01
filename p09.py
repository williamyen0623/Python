

def p09(citations=[1,4,2,8,5,7]):
    h=None
    # ↓程式區域↓
    h = 0
    N = len(citations)
    for i, c in enumerate(citations):
        h = max(h, min(N - i, c))
    # ↑程式區域↑
    return h

print(p09())