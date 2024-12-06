import json
import requests
from tqdm.auto import tqdm

# 读取JSON文件
with open('source_pdf.json', 'r') as f:
    data = json.load(f)

# 遍历JSON数据并下载PDF文件
for filename, url in tqdm(data.items()):
    response = requests.get(url)
    if response.status_code == 200:
        # 保存PDF文件到当前路径
        with open(filename, 'wb') as pdf_file:
            pdf_file.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}")