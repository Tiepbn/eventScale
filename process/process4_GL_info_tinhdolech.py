import csv
import numpy as np

#read file info in filter4
list_info = []
with open("D:/7.reseach/filter4_drop-under_5_event_in_group/infomation_filter4.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_info.append(row)
        
        
list_GL_id = []
with open("D:/7.reseach/process3_venue_range/venue_process3.csv", "r" , encoding="iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_GL_id.append(row)
        
index_dict = {value[3]: index for index, value in enumerate(list_info)}



#tính độ lệch giờ
list_hour_deviation = []

for i in range(len(list_GL_id)):    
    GL_id = list_GL_id[i]
    sum=0
    for j in GL_id:
        sum = sum +  int(list_info[index_dict[j]][10])
    mean = sum/len(GL_id)
    hour_deviation = int(list_info[index_dict[GL_id[0]]][10]) - mean
    list_hour_deviation.append(hour_deviation)


#calculate deviation weekdays


day_to_number = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}



list_wd_deviation = []

for i in range(len(list_GL_id)):    
    GL_id = list_GL_id[i]
    sum=0
    for j in GL_id:
        sum = sum + day_to_number[list_info[index_dict[j]][11]]
    mean = sum/len(GL_id)
    wd_deviation = day_to_number[list_info[index_dict[GL_id[0]]][11]] - mean
    list_wd_deviation.append(wd_deviation)


deviation = []


for i in range(len(list_hour_deviation)):
    a=[]
    a.append(list_GL_id[i][0])
    a.append(list_hour_deviation[i])
    a.append(list_wd_deviation[i])
    deviation.append(a)
    

name = ['event_id', 'hour_devi_GL', 'wd_devi_GL']

deviation.insert(0,name)

with open("D:/7.reseach/process4_GL_info_tinhdolech/process_4_GL_info_deviation.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(deviation)






