##对于NLP（自然语言处理）来说，分词是一步重要的工作,这里使用jieba分词
##对你输入的文章进行分词然后统计等等操作
import jieba
##导入用于用于制作词云图的wordcloud
from wordcloud import WordCloud,ImageColorGenerator
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd
import docx
#规定要去除的没意义的词语
excludes = ("有关","从本","以及","一定","凡因","之前","一项","之日起","总则","一支",
"一般","及其","GB","11","20","T18894","T11822","1987","2020","第二十二条","30","10","日起",
"几个","之一","为了","以下")
#定义用户词典
file_userdict = 'userdict.txt'
jieba.load_userdict(file_userdict)
document = docx.Document("001.docx")
content = " ".join([para.text for para in document.paragraphs])
seg_list = jieba.cut(content, cut_all=False)
# 过滤标点符号、无意义的单个字
seg_list = [
    word
    for word in seg_list
    if len(word) > 1]
#去除不想要的词
seg_list = seg_list
for i in excludes:
    while i in seg_list:
        seg_list.remove(i)
ciyundata = " ".join(seg_list)
# 统计词频
from collections import Counter
counter = Counter(seg_list)
# 构造pandas并且排序
df = pd.DataFrame(list(counter.items()), columns=["word", "count"])
df.sort_values(by="count", ascending=False, inplace=True)
# 输出到Excel文件
df.to_excel("科学技术研究档案管理规定-词频数据.xlsx", index=False)
#添加形状配置文件
# image1 = Image.open("test.png")
# MASK = np.array(image1)
#绘制词云图
wc = WordCloud(font_path="E:\\PythonLearn\\词频\\simsun.ttf",background_color="white",max_words=1000,max_font_size=100,width=1000,height=1000,repeat=False,collocations=False,mode='RGBA').generate(ciyundata)
plt.imshow(wc)
plt.axis("off")
wc.to_file('科学技术研究档案管理规定-词云分析.png')