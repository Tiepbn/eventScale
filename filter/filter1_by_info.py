import csv
import pandas as pd
import numpy as np

list_info_eID = []

with open("D:/7.reseach/filter1/info_file.csv",'r', encoding = 'iso-8859-1')as file:
  csv_reader = csv.reader(file)
  for row in csv_reader:
    list_info_eID.append(row[3])


list_info_eID = list_info_eID[1:]
set_info = set(list_info_eID)

list_des = []
with open ("D:/7.reseach/NewYork_event_description2012_2020.txt", 'r', encoding = 'iso-8859-1')as file:
    for line in file:
            process_line = line.strip()
            process1 = process_line.split('\t')
            if(process1[2] in set_info): 
                list_des.append(process1)
           
#with open("D:/reseach/venue_filter.csv", 'w', encoding = 'iso-8859-1', newline = '')as file:
#    writer = csv.writer(file)
#    writer.writerows(list_des)
    
    
#xu ly description của filter 2:
    
print(list_des[0])

for i in range(20):
    print(list_des[i][2])
    
print(list_attendees_idE[0])

list_des_filter2 = []
for i in list_des:
    if(i[2] in set_att_idE):
        list_des_filter2.append(i)
        
        
with open("D:/7.reseach/filter2/description_filter2.csv","w",encoding="iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_des_filter2)
