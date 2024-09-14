
import csv

#read file process 2 to take description
list_des = []
with open(r"D:\7.reseach\process2_des_NLTK\des_process2.csv", "r" , encoding="iso-8859-1")as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        list_des.append(i)
list_des.pop(0)

#đọc file lấy các event id
list_GL_id = []
with open(r"D:/7.reseach/process3_venue_range/venue_process3.csv", "r" , encoding="iso-8859-1") as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        list_GL_id.append(i)
        
        
#tính xem event_id tương ứng với index bao nhiêu để tính toán
index_dict = {value[1]: index for index, value in enumerate(list_des)}        
    
name = ['group_id', 'event_id', 'similar', 'description']

list_devi_similar = []

for i in list_GL_id:
    event_id_center = i[0]
    index_des_center = index_dict[event_id_center]
    #lấy độ tương tự của sự kiện ở trung tâm
    similar_center = float(list_des[index_des_center][2])
    
    s=0
    for j in i:
        event_id_xq = j
        index_des_xq = index_dict[event_id_xq]
        #lấy độ tương tự của sự kiện xung quanh
        similar_xq = float(list_des[index_des_xq][2])
        s += similar_xq

    list_devi_similar.append(round(similar_center - s,5))


#tính độ tương tự
    
#khai báo thư viện
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity




#hàm tính độ tương tự giữa text thứ a và b trong listdes[][7]

def Sim(a,b):
    if len(list_des[a][3])!=0 and len(list_des[b][3])!=0  :
        a_vals = Counter(list_des[a][3])
        b_vals = Counter(list_des[b][3])
        
        # convert to word-vectors
        words  = list(a_vals.keys() | b_vals.keys())
        a_vect = [a_vals.get(word, 0) for word in words]       
        b_vect = [b_vals.get(word, 0) for word in words]        
        
        c = round(cosine_similarity([a_vect], [b_vect])[0][0],5)
    else:
        #nếu một trong hai des rỗng thì độ tương tự bằng 0
        c=0
    return c


count = 0
length = len(list_GL_id)
#tạo list chứa max mà min của độ tương tự
list_Mmv = []

similar = 0
for i in list_GL_id:
    count = count +1
    print(count, round(count*100/length,3), '%')
    M=0
    m=1
    event_id_center = i[0]
    index_des_center = index_dict[event_id_center]
    
    a=[]
    if(len(i)!=1):
        list_s = []
        for j in i[1:] :
            event_id_xq = j
            index_des_xq = index_dict[event_id_xq]

            #tính similar
            similar = Sim(index_des_center,index_des_xq)
            
            #append các giá trị tính được vào một list sau đó dùng hàm để tính ave, max, min
            list_s.append(similar)
        a.append(max(list_s))
        a.append(min(list_s))
        a.append(sum(list_s)/len(list_s))
        list_Mmv.append(a)
            
    else:
        #thêm 1 cho max và 1 cho min nếu chỉ có 1 sự kiện
        a.append(1)
        a.append(1)
        a.append(1)
        list_Mmv.append(a)
        #max = 1
        #min = 1
        #ave = 1

for i in range(len(list_Mmv)):
    list_Mmv[i].insert(0,list_GL_id[i][0])
name = ['event_id', 'ave_similar', 'Max_similar', 'min_similar','ave_similar']
list_Mmv.insert(0,name)
        
with open(r"D:\7.reseach\process11_GL_maxMinDevi_similar_des\process11_GL_maxMinDevi_similar_des.csv","w",encoding = "iso-8859-1",newline ="") as file:
    writer = csv.writer(file)
    writer.writerows(list_Mmv)

