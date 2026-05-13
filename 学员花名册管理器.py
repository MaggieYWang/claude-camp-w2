#这是一个学院花名册管理器，可以添加、删除、查询用户。
student_info_list = []
def add_student():
    name = input("请输入需要添加的学员姓名：")
    email = input("请输入学员邮箱：")
    date_joined = input("请输入学员加入日期yyyy-mm-dd：")
    student_info = {"name": name, "email": email, "date_joined": date_joined} 
    student_info_list.append(student_info)
    print(student_info_list)

def remove_student():
    global student_info_list
    name = input("请输入需要移除的学员姓名：")
    student_info_list = [s for s in student_info_list if s["name"] != name]
    print(student_info_list)

def find_student():
    name = input("请输入需要查找的学员姓名: ")
    result = [s for s in student_info_list if s["name"] == name]  # 存到临时变量
    
    if result:
        for s in result:
            print(f"姓名: {s['name']}")
            print(f"邮箱: {s['email']}")
            print(f"加入日期: {s['date_joined']}")
    else:
        print("未找到该学员")  # 没找到，友好提示

def main():
    while True:
        print("===== 学员花名册管理器 =====")
        print("1. 添加学员")
        print("2. 删除学员")
        print("3. 查找学员")
        print("0. 退出")
        choice = input("请输入选项：")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            find_student()
        elif choice == "0":
            print("再见！")
            break  #这里才应该 break
        else:
            print("您的输入有误，请重新输入")

main()