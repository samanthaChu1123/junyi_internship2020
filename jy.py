# 1.A
a = "junyiacademy"
b = "flipped class room is important"

def reverse(string):
    new = ""
    i = -1
    while 1:
        new += string[i]
        i -= 1
        if string[i] == string[0]:
            new += string[i]
            break
    return new

print('f("%s") == "%s" '%(a,reverse(a)))

# 1.B
def reverse2(string):
    s = string.split()
    ans = ""
    for i in s :
        ans += "%s " % reverse(i)
    return ans[:-1]

print('f("%s") == "%s"'%(b,reverse2(b)))

# 2
def tt(num):
    lis = []
    for i in range(1,num+1):
        lis.append(i)
        if(i % 5 == 0):
            if i % 3 != 0:
                lis.remove(i)
        elif(i % 3 == 0):
            if i % 5 != 0:
                lis.remove(i)
    print(len(lis))

tt(15)
