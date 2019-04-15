import requests
url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9077'
r=requests.get(url)
#将文本信息以@进行切片
tlist=r.text.split('@')[1:]
tlist[-1]=tlist[-1][:-2]
all=[]
with open("data/city.txt","w",encoding="utf-8") as w:
 for i in tlist:
    i=i.split('|')
    print(i)
    w.writelines(i[1]+"\n")
    #all += [i]     #将以'|'分隔开的信息以列表的形式添加到all里面
