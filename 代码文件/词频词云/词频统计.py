def txt():  #输出词频前N的词语
    txt = open("三国演义.txt","r").read() #打开txt文件,要和python在同一文件夹
    words = jieba.lcut(txt)  #精确模式，返回一个列表
    counts = {}  #创建字典
    excludes = ("将军","二人","却说","荆州","不可","不能","如此","如何",\
                "军士","左右","军马","商议","大喜") #规定要去除的没意义的词语
    for word in words:
        if len(word) == 1:                          #把意义相同的词语归一
            continue
        elif word == "诸葛亮" or word == "孔明曰":
            rword = "孔明"
        elif word == '关公' or word == '云长':
            rword = '关羽'
        elif word == '玄德' or word == '玄德曰':
            rword = '刘备'
        elif word == '孟德' or word == "丞相" or word == '曹躁':
            rword = '曹操'
        else:
            rword = word
        counts[rword] = counts.get(rword,0) + 1     #字典的运用，统计词频P167
    for word in excludes: #删除之前所规定的词语
        del(counts[word])
    items = list(counts.items())   #返回所有键值对P168
    items.sort(key=lambda x:x[1], reverse =True) #降序排序
    N =eval(input("请输入N：代表输出的数字个数"))
    wordlist=list()
    for i in range(N):
        word,count = items[i]
        print("{0:<10}{1:<5}".format(word,count)) #输出前N个词频的词语