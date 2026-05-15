print("=== 简易计算器 ===")
print("支持 + - * /，输入 q 随时退出\n")

quit_flag = False  # 记录用户是否主动退出

# 第一个循环：专门收集合法输入
while True:
    num1 = input("请输入第一个数字（输入 q 退出）：")
    if num1 == "q":
        quit_flag = True
        break
    op = input("请输入运算符（+ - * /）：")
    if op == "q":
        quit_flag = True
        break
    num2 = input("请输入第二个数字（输入 q 退出）：")
    if num2 == "q":
        quit_flag = True
        break

    try:
        num1 = float(num1)  # 把字符串转成数字
        num2 = float(num2)
        break               # 输入合法，跳出循环
    except ValueError:
        print("请输入有效数字，重新开始\n")
        continue            # 回到循环开头重新输入

# 第二步：循环外执行计算
if quit_flag:
    print("再见！")
else:
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("⚠ 除数不能为 0")
            result = None
    else:
        print(f"⚠ 不支持的运算符：{op}")
        result = None
    if result is not None:
       print(f"\n{num1:g} {op} {num2:g} = {result:g}")