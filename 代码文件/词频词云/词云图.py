def create_word_cloud(filename):
    wl = txt() #调用函数获取str
    cloud_mask = np.array(Image.open("love.jpg"))#词云的背景图，需要颜色区分度高 需要把背景图片名字改成love.jpg
    wc = WordCloud(
        background_color = "black", #背景颜色
        mask = cloud_mask,          #背景图cloud_mask
        max_words=100,              #最大词语数目
        font_path = 'simsun.ttf',   #调用font里的simsun.tff字体，需要提前安装
        height=1200,                #设置高度
        width=1600,                 #设置宽度
        max_font_size=1000,         #最大字体号
        random_state=1000,          #设置随机生成状态，即有多少种配色方案
        )
    myword = wc.generate(wl)  # 用 wl的词语 生成词云
    # 展示词云图
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    wc.to_file('1.jpg')  # 把词云保存下当前目录（与此py文件目录相同）