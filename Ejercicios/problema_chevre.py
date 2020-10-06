a = input()

sub = input()

num = len(sub)

n = len(a)

c = 0
for i in range(0 , n - num + 1):
    print(a[i : i + num ])
    if(a[i : i + num ] == sub):
        c += 1

print(c)