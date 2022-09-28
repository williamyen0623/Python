#利用身份運算子id()檢查變數所存在的記憶體位址是否相同,講述所有變數皆屬於物件相同值的變數存在相同記憶體位址
x=5
print(id(x))
y=5
print(id(y))
print(x==y)
print(x is y)
print(id(x)==id(y))
y=20
print(id(y))
print(x==y)
print(x is y)
print(id(x)==id(y))