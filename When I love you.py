import random as r
import sys
import time as t

# 用户输入字母 User input letter
a = input("请输入字母")
# 创建两个空列表 Create two empty lists
b = []
c = []
# 定义变量d，初始值为1 Define variable d, initial value is 1
d = 1

# 将用户输入的字母添加到列表b和c中 Add user input letter to list b and c
for i in a:
    b.append(i)
    c.append(i)
# 打乱列表b的顺序 Shuffle the order of list b
r.shuffle(b)
print("已将您输入的内容格式化为{}".format(c))
# 程序暂停1秒 Program pause for 1 second
t.sleep(1)
print("正在为您匹配...")
# 程序暂停1秒 Program pause for 1 second
t.sleep(1)

# 记录开始时间 Record start time
start_time = t.time()
# 当列表b和c不相等时，循环执行 When list b and c are not equal, loop execution
while b != c:
    if b != c:
        # 定义变量d，每次循环加1 Define variable d, add 1 for each loop
        d += 1
        # 打乱列表b的顺序 Shuffle the order of list b
        r.shuffle(b)
        # 打印出匹配的结果 Print out matching results
        print("匹配的第{}次，结果为{}".format(d, b))

# 记录结束时间 Record end time
end_time = t.time()

# 计算程序运行时间，并保留小数点后两位 Calculate program running time and keep two decimal places
time = round(end_time - start_time)
# 程序暂停1秒 Program pause for 1 second
t.sleep(1)
# 打印出程序运行结果 Print out program running results
print(
    "恭喜您，在经历了{}次匹配，共计{}秒后，寻找到了那个和您相同的的“{}”\n世界广阔，而你我渺如尘埃\n可只要用心寻觅，耐心等待\n总能找到那个爱你的TA".format(
        d, time, a))
# 程序暂停5秒 Program pause for 5 seconds
t.sleep(5)
# 打印出10个换行符 Print out 10 newline characters
print('\n' * 10)
# 打印出I LOVE YOU Print out I LOVE YOU
print('I LOVE YOU')

# 退出程序，并返回520 Exit the program and return to 520
sys.exit(520)
