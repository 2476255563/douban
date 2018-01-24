import requests, re

def parsing(text) :
    # 提取一个页面的分数
    content = re.findall(r'<span class="rating_num" property="v:average">.*?</span>', html, re.S)

    score = []
    for i in range(len(content) ) :
        score.append(float(re.search(r'>(.+?)</span>', content[i]).group(1)))
    
    return score

fractions = []
for i in range(1, 11) :
    res = requests.get(r'https://movie.douban.com/top250?start=' + str(i) )
    html = res.text
    arr = parsing(html)
    fractions = fractions + arr

# 对数组进行排序
fractions.sort()
fractions.reverse()

# 对答案相加
sum = 0
for i in range(166) :
    sum = sum + fractions[i]

# 打印答案
print(str(sum) )