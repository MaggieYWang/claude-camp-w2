import json
from pathlib import Path
FILENAME = Path(__file__).parent / "todos.json"  # 统一管理文件名
task_to_complete = []    

def add_task():
    while True:
        task = input("请输入待办事项（输入0退出）：\n")  
        if task == "0":   
            break
        elif task != "":  # 非空则添加至列表
            task_to_complete.append(task)
            print(f"已添加：{task}")

def remove_task():
    while True:
        task_done = input("请输入已完成事项（输入0退出）：\n")  
        if task_done == "0":   
            break
        elif task_done != "":  # 非空则更新列表
            if task_done in task_to_complete:   # 先检查再删除
                task_to_complete.remove(task_done)
                print(f"已移除：{task_done}")
            else:
                print(f"❌ 未找到：{task_done}")

def save_tasks():
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(task_to_complete, file, ensure_ascii=False, indent=2)
    print("已保存到本地")

def load_tasks():
    global task_to_complete
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            task_to_complete = json.load(file)
        print(f"✅ 已加载 {len(task_to_complete)} 条待办事项")
    except (FileNotFoundError, json.JSONDecodeError):
        task_to_complete = []

load_tasks()
while True:
    print("-" * 25 + "\n1.添加  2.删除  3.查看  0.退出")
    choice = input("请输入选项：")
    if choice == "1":
        add_task()； save_tasks()
    elif choice == "2":
        remove_task()； save_tasks()
    elif choice == "3":
        print("你的待办清单：", task_to_complete)
    elif choice == "0":
        print("再见！"); break 
    else:
        print("您的输入有误，请重新输入")   
    

