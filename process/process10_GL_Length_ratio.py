import csv

#read file info in filter4
list_des = []
with open(r"D:\7.reseach\process6_devi_des\process6_devi_des.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        a=[]
        a.append(i[1])#event id
        a.append(i[2])#len text
        list_des.append(a)
list_des.pop(0)

#đọc file lấy các event id
list_GL_id = []
with open("D:/7.reseach/process3_venue_range/venue_process3.csv", "r" , encoding="iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        list_GL_id.append(i)
        
        
#tính xem event_id tương ứng với index bao nhiêu để tính toán
index_dict = {value[0]: index for index, value in enumerate(list_des)}        


#tính len text / mean text        
list_ratio = []

count = 0
for i in list_GL_id:
    count +=1
    print(count)
    event_id = i[0]
    index_des = index_dict[event_id]
    len_text_0 = float(list_des[index_des][1])
    s = 0 
    for j in i:
        event_idj = j
        index_des = index_dict[event_idj]
        len_text_event = float(list_des[index_des][1])
        s += len_text_event
        
    a = []
    a.append(event_id)
    #kiểm tra xem s có bị bằng 0 không
    if s!=0 :
        a.append(len_text_0/s)
    # nếu sự kiện xung quanh có tổng số text là 0 thì append 0 vào tỉ lệ
    else:
        a.append(1)
    list_ratio.append(a)
    
name = ['event_id','ratio_length']


list_ratio.insert(0,name)

#test    251413466,    244925843,    245347065    ,245875249    ,256363206


  
with open(r"D:\7.reseach\process10_GL_Length_ratio\process10_GL_Length_ratio.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_des)

        
        
        
        
