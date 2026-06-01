# 切目录
cd /opt/linkerhand/ws_src/collection_data
# 切环境
source /home/linkerhand/.venv/data_collection/bin/activate

# 监控并执行
while inotifywait -e modify ./count.csv; do
    python3 calculateHours.py
done
