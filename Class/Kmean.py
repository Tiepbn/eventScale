#from kneed import KneeLocator
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import numpy as np
import csv
    
list_class = []
list_index = []
with open("D:/7.reseach/filter4_drop-under_5_event_in_group/attendees_filter4.csv", "r", encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_class.append(row[5])  
        list_index.append(row[3])      

#chuyển dữ liệu về dạng số và reshape
list_class_reshaped = [[int(x)] for x in list_class]


# Áp dụng thuật toán KMeans để phân cụm dữ liệu
kmeans = KMeans(
    n_clusters=3,
    init="random",
    n_init=10,
    max_iter=300,
    random_state=42
)

np_class_reshaped = np.array(list_class_reshaped)
K =kmeans.fit(np_class_reshaped)



#xem cacsc classs thuộc các nhóm sau khi dùng KMeans
list_class = []
for i in range(len(list_class_reshaped)):
    list_class.append(K.labels_[i])

list_0 = []
list_1 = []
list_2 = []

for i in range(len(list_class)):
    if(list_class[i]==0):
        list_0.append(list_class_reshaped[i][0])
    if(list_class[i]==1):
        list_1.append(list_class_reshaped[i][0])
    if(list_class[i]==2):
        list_2.append(list_class_reshaped[i][0])

print("range List 1,2,3")
min(list_1)
min(list_2)


        
        
#ghép event_id, attendess_user, class và sắp xếp lại theo event id
sorted_data = []
for i in range(len(list_class)):
    a=[]
    a.append(list_index[i])
    a.append(list_class_reshaped[i][0])
    a.append(list_class[i])
    sorted_data.append(a)
sorted_data = sorted(sorted_data,key=lambda x:x[0])

#đọc file Merge
list_Merge = []
with open("D:/7.reseach/zMerge/Merge_feature.csv", "r", encoding = "iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_Merge.append(row)
        
list_Merge.pop(0)     
   
list_Merge = sorted(list_Merge,key=lambda x:x[0])        
data = []       
 
names=['event_id',
         'X1',
         'X2',
         'X3',
         'X4',
         'X5',
         'X6',
         'X7',
         'X8',
         'X9',
         'X10',
         'X11',
         'X12',
         'X13',
         'X14',
         'X15',
         'X16',
         'X17',
         'X18',
         'time',
         'group_id',
         'attdees',
         'class'] 

#thêm class vào cuối của data
for i in range(len(list_Merge)):
    list_Merge[i].append(sorted_data[i][2])
    

data = sorted(list_Merge,key=lambda x:x[19]) 
data.insert(0,names)

with open("D:/7.reseach/zzKmean/data.csv", "w", encoding="iso-8859-1", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    
    
    

    
    
    
    
    
    
    
    