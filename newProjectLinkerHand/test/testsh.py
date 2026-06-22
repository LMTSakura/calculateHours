import time

print("步骤1: 读取参数...")
param = input("输入参数: ")
print(f"收到: {param}")

print("步骤2: 模拟数据处理和上传...")
time.sleep(3)
print(" 数据处理完成！")
print(" 数据上传完成！")

print("步骤3: 等待用户输入...")
user_input = input("是否继续? (x退出): ")  # 这里会卡住
print(f"用户输入: {user_input}")
print("程序结束")