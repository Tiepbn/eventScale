import csv
#thu vienn tinh do tuong quan
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity

#read file info in filter4
list_des = []
with open("D:/7.reseach/filter4_drop-under_5_event_in_group/description_filter4.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_des.append(row)
        
#đọc file đã tìm group location
list_GL_id = []
with open("D:/7.reseach/process3_venue_range/venue_process3.csv", "r" , encoding="iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_GL_id.append(row)

#tính xem event_id tương ứng với index bao nhiêu để trỏ vào des của event đó rồi tính toán
index_dict = {value[2]: index for index, value in enumerate(list_des)}

import nltk
#nltk.download('punkt')
from nltk.tokenize import word_tokenize
import re
#nltk.download('stopwords')  
from nltk.corpus import stopwords   
#nltk.download('words')
from nltk.corpus import words


stop_words =set(stopwords.words('english'))        
english_words = set(words.words())

for i in range(len(list_des)):
    list_des[i][3] = re.sub(r'[^\x00-\x7F]+', ' ', list_des[i][3])     

for i in range(len(list_des)):
    list_des[i][3] =set(word_tokenize(list_des[i][3]))
    
for i in range(len(list_des)):
    list_des[i][3] = [word.lower() for word in list_des[i][3]]

for i in range(len(list_des)):   
    list_des[i][3] = [word for word in list_des[i][3] if word not in stop_words]

for i in range(len(list_des)):
    list_des[i][3] = [word for word in list_des[i][3] if word in english_words]
 
   
list_doc = []
for i in range(len(list_GL_id)):
    print(i)
    doc = []
    GL_id = list_GL_id[i]
    skip_first = True
    for j in GL_id:
        if skip_first == True:
            skip_first = False
            continue
        des_event = list_des[index_dict[j]][3]
        for k in des_event:
            doc.append(k)
    set_doc = set(doc)
    doc = list(set_doc)
    list_doc.append(doc)
    
list_similarity = []
for i in range(len(list_GL_id)):
    print(i)
    GL_id = list_GL_id[i]
    if(len(GL_id) ==1):
        list_similarity.append(0)
    else:
        # Đếm số lần xuất hiện của từng từ trong danh sách A và B
        A_counts = Counter(list_des[index_dict[GL_id[0]]][3])
        B_counts = Counter(list_doc[i])

        # Tạo vector từ danh sách A và B
        words = list(A_counts.keys() | B_counts.keys())
        A_vector = [A_counts.get(word, 0) for word in words]
        B_vector = [B_counts.get(word, 0) for word in words]

        # Tính cosine similarity round:làm tròn 
        similarity = round(cosine_similarity([A_vector], [B_vector])[0][0],3)
        list_similarity.append(similarity)
    
list_similarity_nested = [[item] for item in list_similarity]

    
with open("D:/7.reseach/process5_GL_des_NLTK/process5_GL_des_NLTK.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_similarity_nested)
                
    
    
    
    
    