#报数coding
n = int(input("请输入数字"))
num = 1
count = 1
cnt = [0,0,0,0]
while count<=n:
    if num%7 == 0 or '7'in str(num):
        cnt[(num-1)%4]+=1
    else:
        count+=1
    num+=1
for i in range(4):
    print(cnt[i])