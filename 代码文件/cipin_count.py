# 1. 安装依赖的包
# # 读取docx
# !pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-docx
# # 中英文分词
# !pip install -i https://pypi.tuna.tsinghua.edu.cn/simple jieba
# # 输出到excel
# !pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas

# 2. 读取docx文件到一个大字符串
import docx
document = docx.Document("Python（计算机程序设计语言）.docx")
content = " ".join([para.text for para in document.paragraphs])
# print(len(content))
# print(content[:10])

# 3. 中文分词
import jieba
seg_list = jieba.cut(content, cut_all=False)
print(type(seg_list))
# 过滤标点符号、无意义的单个字
seg_list = [
    word
    for word in seg_list
    if len(word) > 1
]
# print(seg_list[:30])

# 4. 统计词频
from collections import Counter
counter = Counter(seg_list)
for key,count in list(counter.items())[:10]:
    print(key,count)

# 5. 构造pandas并且排序
import pandas as pd
df = pd.DataFrame(list(counter.items()), columns=["word", "count"])
# print(df.head())
df.sort_values(by="count", ascending=False, inplace=True)
# print(df.head())

# 6. 输出到Excel文件
df.to_excel("分析结果-词频数据.xlsx", index=False)
