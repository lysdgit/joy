a=2
b=5

# while (a>0 and b>0) :
#     print("h",end ='')
#     a=a-1
#         if(a=0 and b>0):
for i in range(a):
    print("h",end ='')
for i in range(b):
    print("i",end ='')

    
#四舍五入
def sishewuru(a):
    m=int(a/10)
    n=a-10*m
    if (n<5):
        a=10*m
    if (n>4):
        a=10*(m+1)
    print(a)

sishewuru(10.8)