import csv
list_des = []

#read file des in filter 3
with open("D:/7.reseach/filter3_drop-greater_100_attendees/description_filter3.csv","r",encoding = "iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_des.append(row)  
    
#get list group in list_des
list_group = [row[1] for row in list_des]

#kiem tra xem có bao nhiêu nhóm
set_gr = set(list_group)

#create a dictionary to store count element
element_count = {}

for i in list_group:
    if i in element_count:
        element_count[i] += 1
    else:
        element_count[i] = 1
    
set_gr_done = set([i for i in list_group if element_count[i] >= 5])

list_des_done = []
for row in list_des:
    if row[1] in set_gr_done:
        list_des_done.append(row)        
        
with open("D:/7.reseach/filter4_drop-under_5_event_in_group/description_filter4.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_des_done)
    
    
    
    
set_eid_des_done = set([row[2] for row in list_des_done])


list_venue = []
with open("D:/7.reseach/filter3_drop-greater_100_attendees/venue_filter3.csv","r",encoding = "iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[2] in set_eid_des_done :
            list_venue.append(row)
with open("D:/7.reseach/filter4_drop-under_5_event_in_group/venue_filter4.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_venue)
    
    
list_att = []
with open(r"D:/7.reseach/filter3_drop-greater_100_attendees/attendees_filter4.csv","r",encoding = "iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[3] in set_eid_des_done :
            list_att.append(row)
with open(r"D:/7.reseach/filter4_drop-under_5_event_in_group/attendees_filter4.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_att)
    
    
list_info = []
with open(r"D:\7.reseach\filter3_drop-greater_100_attendees\infomation_filter3.csv","r",encoding = "iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[3] in set_eid_des_done :
            list_info.append(row)

with open(r"D:/7.reseach/filter4_drop-under_5_event_in_group/infomation_filter4.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_info)
            
    
