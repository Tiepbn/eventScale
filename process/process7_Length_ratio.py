# lấy file từ process 6
import csv

list_des = []
with open(r"D:\7.reseach\process6_devi_des\process6_devi_des.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        list_des.append(i)
list_des.pop(0)


#tính trung bình text theo nhóm
sum = 0
count=1
mean=0
list_mean = []
for i in range(len(list_des)):
    if(i==len(list_des)-1):
        sum = sum + int(list_des[i][3])
        mean = float(sum)/(count+1)
        for i in range(count):
            list_mean.append(mean)
        break   
    elif(list_des[i][0] == list_des[i+1][0]):
        count = count+1
        sum = sum + int(list_des[i][3])
    else:
        sum = sum + int(list_des[i][3])
        mean = float(sum) / count
        for i in range(count):
            list_mean.append(mean)
        count =1
        sum =0
        
        
#tính tỉ lệ độ dài / độ dài trung bình
list_ratio = []        
for i in range(len(list_des)):
    if(list_mean[i]!=0):
        list_ratio.append(int(list_des[i][3])/list_mean[i])
    else:
        list_ratio.append(1)


#insert tỉ lệ vào cột 4
for i in range(len(list_des)):
    list_des[i].insert(4,list_ratio[i])


#tên lần lượt của các cột trong list_des
name = ['group_id', 'event_id', 'similar_e_group', 'len_text','ratio_length', 'deviation_text','description']



list_des.insert(0,name)
  
with open(r"D:\7.reseach\process7_Length_ratio\process7_Length_ratio.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_des)











