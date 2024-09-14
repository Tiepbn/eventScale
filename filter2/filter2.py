import csv

list_attendees = []

#read file attendees in filter 1
with open("D:/7.reseach/filter1/attendees_filter.csv","r",encoding = "iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if(len(row)>9):
            list_attendees.append(row)

list_person_id = []
list_count= []

#đếm số người có tham gia trong sự kiện(yes thì đếm)
for i in range(len(list_attendees)):
    count = 0
    for j in range(len(list_attendees[i])-5):
        list_attendees[i][j+5] = list_attendees[i][j+5].split("_")
        if( list_attendees[i][j+5][2][0] == "y"):
            count=count+1
            list_person_id.append(list_attendees[i][j+5][0])
    list_count.append(count)

#chèn thêm một cột số người thực tế tham gia
for i in range(len(list_attendees)):
    list_attendees[i].insert(5, list_count[i])
    
#chỉ giữ lại những sự kiện có từ 5 người trở lên
list_attendees1 = []
for i in list_attendees:
    if(i[5]>4):
        list_attendees1.append(i)
            
#ghi lại file attenndees mới        
with open("atendees2_filter.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_attendees1)

#vẽ biểu đồ histogram về số người tham dự các sự kiện
data = []
for i in list_attendees1:
    data.append(i[5])
    
import matplotlib.pyplot as plt
plt.hist(data, bins=100, edgecolor='black')
plt.title('Biểu đồ Histogram')
plt.xlabel('Giá trị')
plt.ylabel('Tần số')
plt.xlim(0,100)
plt.show()


#set id của attendees
list_attendees_idE = []
for i in list_attendees1:
    list_attendees_idE.append(i[3])
set_att_idE = set(list_attendees_idE)


print(list_attendees_idE[0])


"""
xuất file csv sau khi lọc
"""


#list_info_filter2 = []
list_venue = []
list_des = []
a=0
with open("D:/7.reseach/filter1/venue_filter.csv","r",encoding = "iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        a=a+1   
        if(row[2] in set_att_idE):
            list_venue.append(row)
            
for i in range(5):
    print(list_venue[i])

list_id_ve = []
for i in range(len(list_venue)):
    list_id_ve.append(list_venue[i][2])
set1 = set(list_id_ve)

with open("D:/7.reseach/filter2/venue_filter2.csv","w",encoding="iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_venue)
    
    
    
    
    
    
    
    