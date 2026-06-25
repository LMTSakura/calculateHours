"""
脚本名称：calculateHours.py
作者：刘明焘
创建日期：2026-05-30
最后修改：2026-05-31
版本：1.2
描述：统计CSV文件中任务时间总和并计算小时数
"""
import csv
import math
import os
import sys
import time
from datetime import datetime
def initAndCalculateHours():
    path = r'./count.csv'
    # 统计表中数据占有行数
    with open(path,'r',encoding='utf-8',errors='ignore') as fileObject:
        # 获取行数
        row_count = 0
        for row in fileObject:
            row_count += 1
        print(f"csv文件已占数据总行数: {row_count}")
        total_rows = row_count - 1
    # 主功能
    with open(path,'r',encoding='utf-8',errors='ignore') as fileObject:
        readOperateObject = csv.DictReader(fileObject)
        # 任务字典初始化
        top_color_dict = {}
        # 任务数初始化、任务总秒数初始化
        top_color_counts,top_color_sum = 0,0
        now = datetime.now()
        # v1.1追加进度条初始化
        process_barLen = 50
        process_barCurrentVal = 0
        for fileRow in readOperateObject:
            # print(fileRow)
            # 累加任务数、任务总秒数
            top_color_counts += 1
            row_top_color_unit_seconds = float(fileRow['top_color'])
            top_color_sum += row_top_color_unit_seconds
            # 加列表/字典方便迭代
            row_top_color_unit_mission = fileRow["episode名"]
            # print(type(row_top_color_unit_mission))
            top_color_dict[row_top_color_unit_mission] = row_top_color_unit_seconds
            # 获取[1][0]的任务名
            missionName = fileRow["任务名"]
            # v1.1追加进度条功能实现
            process_barCurrentVal += 1
            percent = process_barCurrentVal / total_rows * 100
            filled_len = int(process_barLen * process_barCurrentVal // total_rows)
            bar = "\033[32m#\033[0m" * filled_len + "\033[31m-\033[0m" * (process_barLen - filled_len)
            print(f"\r进度: \033[31m|\033[0m{bar}\033[31m|\033[0m {percent:.1f}%", end="")
            time.sleep(0.2)
        clearScreen() # 保留数据故禁用
        print('\n')
        print('''||-------------------------------------------------------------------------------||''')
        print("   当前\033[1;33m任务名称\033[0m：",'\033[31m',missionName,'\033[0m',sep='')
        # 任务总数统计显示、任务秒总值显示、任务总小时数显示
        print("   当前时间节点\033[1;33m任务总数\033[0m统计：",'\033[1;32m',top_color_counts,'\033[0m',' 个',sep='')
        print("   当前时间节点\033[1;33m任务耗时总秒数\033[0m统计：",'\033[1;32m',top_color_sum,'\033[0m',' 秒',sep='')
        print('   当前时间节点\033[1;33m任务耗时总小时数\033[0m统计：',top_color_sum / 3600,f" (\033[1;32m{(math.floor(top_color_sum / 3600 * 100) / 100):.2f}",'\033[0m',' 小时)',sep='')
        # 展示任务列表
        print("   当前时间节点\033[1;33m任务耗时详情：\033[0m")
        for row_top_color_unit_mission,row_top_color_unit_seconds in top_color_dict.items():
            print(f"            {row_top_color_unit_mission}: {row_top_color_unit_seconds:.2f} 秒 ({row_top_color_unit_seconds/3600:.3f} 小时)")
        print('                     ','\033[31m',now.strftime('%Y-%m-%d %H:%M:%S'),'\033[0m')
        print('''||-------------------------------------------------------------------------------||''')
        print()
        # print("\033[32m绿\033[0m","\033[31m红\033[0m","\033[1;33m黄_加粗\033[0m") # 测
def setupColor():
    # 判win还是Lin
    if sys.platform == "win32":
        os.system('')
        return True
    return True
def clearScreen():
    # 判win还是Lin
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def fileIsExist():
    files = os.listdir()
    print(files)
    flag = 0
    for file in files:
        if file == 'count.csv':
            flag = 1
            continue
    if flag == 0:
        print('请先使用read_recording_info.py插入时长并创建cvs文件')    
        return 0
if __name__ == "__main__":
    # fileIsExist()
    setupColor()
    initAndCalculateHours()
