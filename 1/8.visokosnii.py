y = int(input())
if y % 4 == 0 and y % 100 != 0:
    print("високосний")
elif y % 400 == 0:
    print("високосний")
else:
    print("неа")
