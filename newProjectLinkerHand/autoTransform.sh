# !/bin/bash
cd /home/linkerhand/data_convert_upload_c9
source /home/linkerhand/.venv/data_collection/bin/activate
{
 echo "/opt/linkerhand/ws_src/collection_data"
 echo "/home/linkerhand/DataResult_20260622_lmt_zyx"
 echo "c5fdf2f2-a7ea-4626-9f17-6387c204c6ea"
 echo "zyx_lmt"
 echo "y"
 echo "x"
} | python convert_upload.py

