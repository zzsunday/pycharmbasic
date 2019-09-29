import csv
f1=open(r"D:\Downloads\CCDS.current.txt",'r')
file=csv.reader(f1,delimiter="\t")
#print(list(file))
sum=0
next(file)
exon_dict={}
print(type(exon_dict))
print(exon_dict.keys())
for record in file:
    print(exon_dict)
    if record[9] != "-":
        print(record[9])
        chr=record[0]
        exon_list=record[9].lstrip("[").rstrip("]").split(", ")
        print('====================================================')
        print(exon_list)
        print('-----------------------------------------------------')
        print(exon_dict)
        print('++++++++++++++++++++++++++++++++++++++++++++++++++')
        #print(exon_list)
        for range in exon_list:
            exon=chr+":"+range
            #print(exon)
            if exon not in exon_dict:
                exon_dict[exon]=""
                #print(range)
                exon_start=int(range.split("-")[0])
                exon_end=int(range.split("-")[1])
                # print(exon_start)
                sum+=exon_end-exon_start
print(sum)