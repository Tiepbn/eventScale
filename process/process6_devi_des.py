

# đọc file description từ event process2
import csv

list_des = []
with open(r"D:\7.reseach\process2_des_NLTK\des_process2.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_des.append(row)
        
list_des.pop(0)
#sắp xếp theo event id
sorted_data = sorted(list_des, key=lambda x: x[0])
      

#insert độ dài của mô tả vào sorted data
for i in range(len(sorted_data)):
    word = sorted_data[i][3].split()
    count = len(word)
    sorted_data[i].insert(3,count)
    

#tính trung bình text theo nhóm
sum = 0
count=1
mean=0
list_mean = []
for i in range(len(sorted_data)):
    if(i==len(sorted_data)-1):
        sum = sum + int(sorted_data[i][3])
        mean = float(sum)/(count+1)
        for i in range(count):
            list_mean.append(mean)
        break   
    elif(sorted_data[i][0] == sorted_data[i+1][0]):
        count = count+1
        sum = sum + int(sorted_data[i][3])
    else:
        sum = sum + int(sorted_data[i][3])
        mean = float(sum) / count
        for i in range(count):
            list_mean.append(mean)
        count =1
        sum =0

#tính độ lệch của text mô tả, lưu vào list_devi
list_devi = []
for i in range(len(sorted_data)):
    t = float(sorted_data[i][3])-list_mean[i]
    list_devi.append(t)
    
#insert độ lệch vào cột 4
for i in range(len(sorted_data)):
    sorted_data[i].insert(4,sorted_data[i][3]-list_mean[i])



#tên lần lượt của các cột trong sorted_data
name = ['group_id','event_id','similar_e_group','len_text','deviation_text','description']

sorted_data.insert(0,name)
  
with open(r"D:\7.reseach\process6_devi_des\process6_devi_des.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    #writer.writerows(name)
    writer.writerows(sorted_data)
                







