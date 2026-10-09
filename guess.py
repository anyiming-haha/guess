import random

secret_num = random.randint(1, 100)
count = 0

print("=====猜数字小游戏=====")
print("我已经想好一个1~100之间的数字，你来猜！")

while True:
    guess_str = input("请输入你猜测的数字：")
    try:
        guess = int(guess_str)
    except ValueError:
        print("输入无效，请输入整数！")
        continue

    count += 1

    if guess > secret_num:
        print("大了！再试试更小的数")
    elif guess < secret_num:
        print("小了！再试试更大的数")
    else:
        print(f"🎉恭喜猜对！答案是：{secret_num}")
        print(f"你一共猜了 {count} 次")
        break
