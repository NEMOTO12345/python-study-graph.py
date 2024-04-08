# 日本の西暦と人口のグラフを作成


import matplotlib.pyplot as plt
import japanize_matplotlib

x = []
y = []

with open('c01.csv','r',encoding="shift-jis") as f:
    for line in f:
        temp = line.strip().split(',')
        if temp[0] == '0':
            x.append(temp[4])
            y.append(temp[6])
plt.xlabel('人口')
plt.ylabel('西暦')
plt.title('人口分布')
plt.bar(y,x)
plt.show()

