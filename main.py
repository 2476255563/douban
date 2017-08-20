import urllib2, re

def parsing(txt):
    content=re.findall(r'<span class="rating_num" property="v:average">.+?</span>', txt, re.S)
    stc = float(re.search(r'>(.+?)</span>', content[0]).group(1))

    k = 0
    score = []
    while k < len(content):
        score.append(float(re.search(r'>(.+?)</span>', content[k]).group(1)))
        k = k + 1
    return score

def output(score):
    k = 0
    while k < len(score):
        f.append(score[k])
        k = k + 1

f = []
i = 0
while i < 10:
    url = 'https://movie.douban.com/top250?start=' + str(i * 25)
    con = urllib2.urlopen(url)
    i = i + 1
    score = parsing(con.read())
    output(score)

f.sort()
f.reverse()

i = 0
d = 0
while i < 165:
    d = d + f[i]
    i = i + 1
print d

