import csv

#đọc file lấy số text trong 1 description
list_des = []
with open(r"D:\7.reseach\process6_devi_des\process6_devi_des.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        a=[]
        a.append(i[1])
        a.append(i[2])
        list_des.append(a)
list_des.pop(0)

list_GL_id = []
with open("D:/7.reseach/process3_venue_range/venue_process3.csv", "r" , encoding="iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        list_GL_id.append(i)
        
#tính xem event_id tương ứng với index bao nhiêu để tính toán
index_dict = {value[0]: index for index, value in enumerate(list_des)}        



def mean_list(a):
    s = 0
    for i in a:
        s+= float(i)
    return s/len(a)

#tính trung bình của từng nhóm theo GL id
list_mean = []
test = []
a=0
for i in list_GL_id:
    a+=1
    print(a)
    #những sự kiện tổ chức ở địa điểm riêng biệt(không có sự kiện nào từng tổ chức xung quanh)
    if len(i) == 1 :
        index = index_dict[i[0]]
        event = list_des[index]
                
        list_mean.append(event[1])
        continue
    else:
        test = []
        for j in range(len(i)):
            #lấy index tương ứng trong list_des
            index = index_dict[i[j]]
            event = list_des[index]
            leng = event[1]
            test.append(leng)
            
        list_mean.append(mean_list(test))

devi = []

for i in range(len(list_GL_id)):
    a=[]
    a.append(list_GL_id[i][0])
    event_Id = list_GL_id[i][0]
    index = index_dict[event_Id ]
    number = list_des[index][1]
    a.append( float(number   ) - float(list_mean[i]))
    devi.append(a)
        
name = ['event_id', 'deviation']
devi.insert(0,name)
  
with open(r"D:\7.reseach\process9_GL_devi_des\process9_GL_devi_des.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    #writer.writerows(name)
    writer.writerows(devi)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        