import csv
import re
f=open(r"D:\Downloads\CCDS.current.txt",'r')
sum=0
list=[]
for line in f:
    if line.startswith('#'):
        continue

    exons = re.findall('[0-9]+-[0-9]+', line)  # 匹配像00000-00000这种格式的数据，检查了一下可以将所有的外显子匹配到
    for exon in exons:
        list.append(exon)  # 将每一个外显子存入list中
st = set(list)  # 将列表set去重
for i in st:
    exon_one = i.split('-')  # 还可以用find函数找到-的位置然后用切片操作找到起始点和终止点
    exon_start = exon_one[0]
    exon_end = exon_one[1]
    sum += int(exon_end) - int(exon_start)
print(sum)





