import csv



#dict to change weekday from sting to number
day_to_number = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

list_p1 = []
with open("D:/7.reseach/process1_info_tinhdolech/infomation_process1.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_p1.append(row)
#sắp xếp theo event id
sorted_data_1 = sorted(list_p1, key=lambda x: x[3])
#lấy event_id, hour, weekday, hour devi,  week devi, time
merge = [[row[3], row[10], day_to_number[row[12]], row[11], row[13]] for row in sorted_data_1]
#tên cột của list merge
name = [ 'event_id', 'X1', 'X2', 'X3',  'X4']



list_p8 = []
with open(r"D:\7.reseach\process8_maxMinMean_similar_des\process8_maxMinMean_similar_des.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_p8.append(row)
list_p8.pop(0)
#sắp xếp theo event id
sorted_data_8 = sorted(list_p8, key=lambda x: x[1])
#append thêm cột 'max_similar', 'min_similar', 'ave_similar',
for i in range(len(merge)):
    merge[i].append(sorted_data_8[i][4])
    merge[i].append(sorted_data_8[i][5])
    merge[i].append(sorted_data_8[i][6])
    merge[i].append(sorted_data_8[i][8])
    merge[i].append(sorted_data_8[i][9])
    merge[i].append(sorted_data_8[i][2])
#tên cột của list merge
name = [ 'event_id', 'X1', 'X2', 'X3',  'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10']



list_p4 = []
with open("D:/7.reseach/process4_GL_info_tinhdolech/process_4_GL_info_deviation.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_p4.append(row)
list_p4.pop(0)
#sắp xếp theo event id
sorted_data_4 = sorted(list_p4, key=lambda x: x[0])        
#append thêm cột 'hour_devi_GL', 'wd_devi_GL'
for i in range(len(merge)):
    merge[i].append(sorted_data_4[i][1])
    merge[i].append(sorted_data_4[i][2])
#tên cột của list merge
name = [ 'event_id', 'X1', 'X2', 'X3',  'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12']        
        




list_p11 = []
with open(r"D:\7.reseach\process11_GL_maxMinDevi_similar_des\process11_GL_maxMinDevi_similar_des.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_p11.append(row)
list_p11.pop(0)
#sắp xếp theo event id
sorted_data_11 = sorted(list_p11, key=lambda x: x[0])        
#append thêm cột Max_similar','min_similar','ave_similar'
for i in range(len(merge)):
    merge[i].append(sorted_data_11[i][2])
    merge[i].append(sorted_data_11[i][3])
    merge[i].append(sorted_data_11[i][4])
#tên cột của list merge
name = [ 'event_id', 'X1', 'X2', 'X3',  'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'X15']        
        



list_p9 = []
with open(r"D:\7.reseach\process9_GL_devi_des\process9_GL_devi_des.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_p9.append(row)
list_p9.pop(0)
#sắp xếp theo event id
sorted_data_9 = sorted(list_p9, key=lambda x: x[0])        
#append thêm cột 
for i in range(len(merge)):
    merge[i].append(sorted_data_9[i][1])
#tên cột của list merge
name = [ 'event_id', 'X1', 'X2', 'X3',  'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'X15', 'X16']        
        


list_p10 = []
with open(r"D:\7.reseach\process10_GL_Length_ratio\process10_GL_Length_ratio.csv")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_p10.append(row)
#sắp xếp theo event id
sorted_data_10 = sorted(list_p10, key=lambda x: x[0])        
#append thêm cột
for i in range(len(merge)):
    merge[i].append(sorted_data_10[i][1])
#tên cột của list merge
name = [ 'event_id', 'X1', 'X2', 'X3',  'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17']        
        

 
list_p5 = []
with open(r"D:\7.reseach\process5_GL_des_NLTK\process5_GL_des_NLTK.csv")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_p5.append(row)
        
for i in range(len(list_p11)):
    list_p5[i].append(list_p11[i][0])
#sắp xếp theo event id
sorted_data_5 = sorted(list_p5, key=lambda x: x[1])        
#append thêm cột 
for i in range(len(merge)):
    merge[i].append(sorted_data_5[i][0])
#tên cột của list merge
name = [ 'event_id', 'X1', 'X2', 'X3',  'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18']        
        


#lấy cột thời gian và group_id từ cặp eventid-time từ filter1(file info)
event_time = {}
event_group = {}
with open(r"D:\7.reseach\filter1\info_file.csv")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        a = row[3]
        b= row[12]
        c= row[1]
        event_time[a] = b
        event_group[a] = c
#thêm cột thời gian vào sau cột X18
for i in range(len(merge)):
    merge[i].append(event_time[ merge[i][0] ])
    merge[i].append(event_group[ merge[i][0] ])
#tên cột của list merge    
name = [ 'event_id', 'X1', 'X2', 'X3',  'X4',  'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11',
        'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'time','group_id']



list_pclass = []
with open(r"D:\7.reseach\filter4_drop-under_5_event_in_group\attendees_filter4.csv")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        a= []
        a.append(row[3])
        a.append(row[5])    
        list_pclass.append(a)
sorted_data_pclass = sorted(list_pclass, key = lambda x: x[0])
        


for i in range(len(list_pclass)):
    merge[i].append(sorted_data_pclass[i][1])
#tên cột của list merge
name = [ 'event_id', 'X1', 'X2', 'X3',  'X4',  'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11',
        'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'time', 'group_id','attdees'] 

merge.insert(0,name)


with open("D:/7.reseach/zMerge/Merge_feature.csv", "w", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(merge)




