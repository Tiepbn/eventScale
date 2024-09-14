import csv

# lấy file từ process 7
list_des = []
with open(r"D:\7.reseach\process7_Length_ratio\process7_Length_ratio.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        list_des.append(i)
list_des.pop(0)

name = ['group_id',
         'event_id',
         'similar_e_group',
         'len_text',
         'ratio_length',
         'deviation_text',
         'description']
    
        
#tính trung bình độ tương tự theo nhóm
ssum = 0
count = 1
mean=0
list_mean = []
for i in range(len(list_des)):
    if(i==len(list_des)-1):
        ssum = ssum + float(list_des[i][2])
        mean = float(ssum)/(count+1)
        for i in range(count):
            list_mean.append(round(mean,5))
        break   
    elif(list_des[i][0] == list_des[i+1][0]):
        count = count+1
        ssum = ssum + float(list_des[i][2])
    else:
        ssum = ssum + float(list_des[i][2])
        mean = float(ssum) / count
        for i in range(count):
            list_mean.append(round(mean,5))
        count =1
        ssum =0
        
#chèn độ lệch của độ tương tự vào vị trí thứ 3    
for i in range(len(list_des)):
    list_des[i].insert(3,float(list_des[i][2]) - list_mean[i])
        
  

name = ['group_id',
         'event_id',
         'similar_e_group',
         'devi_similar_e_g',
         'len_text',
         'ratio_length',
         'deviation_text',
         'description']    
  
list_text = []
for i in range(len(list_des)):
    list_text.append(list_des[i][7].split())
    

#tính độ tương tự
    
#khai báo thư viện
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity

#đếm lần lượt số sự kiện của mỗi nhóm
list_count = []
ki=0
for i in range(len(list_des)):
    if(i==len(list_des)-1):
        list_count.append(ki+1)
        break    
    if(list_des[i][0]==list_des[i+1][0]):
        ki+=1
    else:
        list_count.append(ki+1)
        ki=0



#hàm tính độ tương tự giữa text thứ a và b trong listdes[][7]

def Sim(a,b):
    if(len(list_text[a])!=0):
        a_vals = Counter(list_text[a])
        b_vals = Counter(list_text[b])
        
        # convert to word-vectors
        words  = list(a_vals.keys() | b_vals.keys())
        a_vect = [a_vals.get(word, 0) for word in words]       
        b_vect = [b_vals.get(word, 0) for word in words]        
        
        c = round(cosine_similarity([a_vect], [b_vect])[0][0],5)
    else:
        c=1
    return c

#hàm tính ma trận độ tương tự của từng nhóm
def Matrix_sim(k,n):
    M=[]
    m=[]
    for i in range(n):
        for j in range(n):
            if i==j:
                m.append(1)
            elif i>j:
                m.append(M[j][i])
            else:
                m.append(Sim(k+i,k+j))
        M.append(m)
        m=[]
    return M

#tính max, min , average độ tương tự so với từng sự kiện trong nhóm
k=0
list_Mmv = []
for i in list_count:
    print(k,round(k*100/len(list_mean),2),"%")
    Matrix = Matrix_sim(k, i)
    for j in range(i):
        v = sum(Matrix[j])/len(Matrix[j])
        Matrix[j].pop(j)
        M = max(Matrix[j])
        m = min(Matrix[j])
        list_Mmv.append([M,m,v])
    k+=i

#chèn max và min độ tương tự vào list_des
    
for i in range(len(list_des)):
    list_des[i].insert(4,list_Mmv[i][0])
    list_des[i].insert(5,list_Mmv[i][1])
    list_des[i].insert(6,list_Mmv[i][2])
    
        
name = ['group_id',
         'event_id',
         'similar_e_group',#2
         'devi_similar_e_g',#3
         'max_similar',#4
         'min_similar',
         'ave_similar',
         'len_text',
         'ratio_length',
         'deviation_text',
         'description']   
    
#xuất file

list_des.insert(0,name)
  
with open(r"D:\7.reseach\process8_maxMinMean_similar_des\process8_maxMinMean_similar_des.csv", "w",  newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_des)




        
        
        
        
        