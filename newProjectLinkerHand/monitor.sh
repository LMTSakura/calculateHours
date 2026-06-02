# !/bin/bash
:<<! 
    功能:
        自动运行calculate.py文件
    运行命令:
        chmod -x monitor.sh
        sudo bash monitor.sh
!
# 切目录
cd /opt/linkerhand/ws_src/collection_data
# 切环境
source /home/linkerhand/.venv/data_collection/bin/activate

echo "已开启自动执行"
# 监控并执行
while inotifywait -e modify ./count.csv; do
    python3 calculateHours.py
    echo "自动执行中..."
done

