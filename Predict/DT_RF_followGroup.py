import pandas as pd
import numpy as np
import sklearn

import csv

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import matplotlib.colors as mcolors

from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score,confusion_matrix



data =pd.read_csv(r"D:\7.reseach\predict_range_member_attendees\zzKmean\data.csv", encoding="iso-8859-1")
data['X2'] = data['X2'].astype('category')

#sắp xếp theo group
groups = data.groupby('group_id')

features =['X1',
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
         'X18'] 


#lwu ket qua du doan
list_acc_dec = []
list_acc_ran = []
list_acc_nb  = []
list_acc_lr  = []
list_acc_knn = []

def cm_hanle(test_data,test_predictions):
        #tesst
    dic_cofusion = {
        '0_0': 0, '0_1': 0, '0_2': 0,
        '1_0': 0, '1_1': 0, '1_2': 0,
        '2_0': 0, '2_1': 0, '2_2': 0
    }
    

    for true_class, predicted_class in zip(test_data['class'], test_predictions):
        
        if true_class == 0 and predicted_class == 0:
            dic_cofusion['0_0'] +=1
        elif true_class == 1 and predicted_class == 1:
            dic_cofusion['1_1'] +=1
        elif true_class == 2 and predicted_class == 2:
            dic_cofusion['2_2'] +=1
            
        elif true_class == 1 and predicted_class == 0:
            dic_cofusion['1_0'] +=1
        elif true_class == 0 and predicted_class == 1:
            dic_cofusion['0_1'] +=1
                         
        elif true_class == 2 and predicted_class == 0:
            dic_cofusion['2_0'] +=1
        elif true_class == 0 and predicted_class == 2:
            dic_cofusion['0_2'] +=1
                         
        elif true_class == 1 and predicted_class == 2:
            dic_cofusion['1_2'] +=1
        elif true_class == 2 and predicted_class == 1:
            dic_cofusion['2_1'] +=1
    cm =np.array([ 
            [dic_cofusion['0_0'],dic_cofusion['0_1'], dic_cofusion['0_2']],
            [dic_cofusion['1_0'],dic_cofusion['1_1'], dic_cofusion['1_2']],
            [dic_cofusion['2_0'],dic_cofusion['2_1'], dic_cofusion['2_2']] 
         ])

    
    return cm
            
cm_tree =np.array([[0,0,0],
                    [0,0,0],
                    [0,0,0]])         
cm_ran = cm_tree.copy()
cm_nb  = cm_tree.copy()
cm_lr  = cm_tree.copy()
cm_knn = np.zeros((3, 3), dtype=int)

count_event_test =0
#dùng vòng for áp dụng các mô hình học máy, lưu độ chính xác và vẽ confusion matrix
i=0
for group_id, data_group in groups:
    progress = i / 2418
    percent = "{:.2f}%".format(progress*100)
    bar_length = 110
    filled_length = int(progress * bar_length)
    bar = '[' + '*' * filled_length + '-' * (bar_length - filled_length) + ']'
    print(percent, "|", bar)
    i=i+1
    
    #chia data
    train_size = int(0.8 * len(data_group))
    train_data = data_group.iloc[:train_size]
    test_data = data_group.iloc[train_size:]
    

    
    #use model decision tree
    model = DecisionTreeClassifier(random_state=42)
    model.fit(train_data[features], train_data['class']) 
    test_predictions = model.predict(test_data[features])
    # caculator accuracy
    acc = accuracy_score(test_data['class'],test_predictions)
    list_acc_dec.append(acc)
    #cofusion matrix
    cm_tree =cm_tree + cm_hanle(test_data, test_predictions)    
    
        
    #use model random forest
    model = RandomForestClassifier(random_state=42)
    model.fit(train_data[features], train_data['class']) 
    test_predictions = model.predict(test_data[features])
    # caculator accuracy
    acc = accuracy_score(test_data['class'],test_predictions)
    list_acc_ran.append(acc)
    cm_ran =cm_ran + cm_hanle(test_data, test_predictions)


    #use model Naive Bayes
    model = GaussianNB()
    model.fit(train_data[features], train_data['class']) 
    test_predictions = model.predict(test_data[features])
    # caculator accuracy
    acc = accuracy_score(test_data['class'], test_predictions)
    list_acc_nb.append(acc)
    #cm
    cm_nb =cm_nb + cm_hanle(test_data, test_predictions)

    
    
    
    # Sử dụng model KNN với k=5
    X_train = train_data[features].to_numpy()
    y_train = train_data['class'].astype(int).to_numpy()
    X_test = test_data[features].to_numpy()
    y_test = test_data['class'].astype(int).to_numpy()
    
    model = KNeighborsClassifier(n_neighbors=4)
    model.fit(X_train, y_train)
    test_predictions = model.predict(X_test)
    
    
    # Tính độ chính xác và cập nhật confusion matrix
    acc = accuracy_score(test_data['class'], test_predictions)
    list_acc_knn.append(acc)
    cm_knn = cm_knn + cm_hanle(test_data, test_predictions)
    
    
    
    if len(train_data['class'].unique()) < 2 :
        continue
    #use model Logistic Regression
    model = LogisticRegression(random_state=42)
    model.fit(train_data[features], train_data['class']) 
    test_predictions = model.predict(test_data[features])
    # caculator accuracy
    acc = accuracy_score(test_data['class'], test_predictions)
    list_acc_lr.append(acc)
    #cm
    count_event_test+=len(test_data)
    cm_lr =cm_lr + cm_hanle(test_data, test_predictions)

print('accuracy decisiontree = ',np.trace(cm_tree)/np.sum(cm_tree))
print('accuracy random forest = ',np.trace(cm_ran)/np.sum(cm_ran))
print('accuracy Naive Bayes = ', np.trace(cm_nb)/np.sum(cm_nb))
print('accuracy Logistic Regression = ',np.trace(cm_lr)/np.sum(cm_lr))
print('accuracy KNN = ', np.trace(cm_knn)/np.sum(cm_knn))

label_ = ['Small','Medium', 'Large']

#tạo cmap color
colors=[(1,1,1),(0.4,0.4,0.4)]
cmap = mcolors.LinearSegmentedColormap.from_list('mycmap',colors,N=250)


#decision tree
percentages_tree = np.round( (cm_tree.T / np.sum(cm_tree,axis = 1)).T * 100, 1)
plt.figure(figsize=(6, 4))
for i in range(cm_tree.shape[0]):
    for j in range(cm_tree.shape[1]):
        if i == 0 and j == 0:  # Nếu vị trí là (0, 0)
            text_color = 'white'  # Màu trắng cho chữ
        else:
            text_color = 'black'  # Màu đen cho chữ
        plt.text(j + 0.5, i + 0.5, f'{cm_tree[i, j]} ({percentages_tree[i, j]}%)', 
                 horizontalalignment='center', verticalalignment='center', color = text_color)
sns.heatmap(cm_tree, annot=False, cmap=cmap, fmt='', xticklabels=label_ , yticklabels=label_ )
plt.xlabel('Predicted',fontsize=12)
plt.ylabel('Actual',fontsize=12)
plt.title('Confusion Matrix - Decision Tree')
plt.show()


#random forest
percentages_ran = np.round ( ( cm_ran.T/np.sum(cm_ran,axis=1)).T *100, 1)
plt.figure(figsize=(6,4))
for i in range(3):
    for j in range(3):
        if i == 0 and j == 0:  # Nếu vị trí là (0, 0)
            text_color = 'white'  # Màu trắng cho chữ
        else:
            text_color = 'black'  # Màu đen cho chữ
        plt.text(j + 0.5, i+0.5, f'{cm_ran[i,j]} ({percentages_ran[i,j]}%)', color = text_color , horizontalalignment = 'center', verticalalignment='center')
sns.heatmap(cm_ran, annot = False, cmap = cmap, fmt='', xticklabels=label_, yticklabels=label_)
plt.xlabel('Predicted', fontsize = 12)
plt.ylabel('Actual', fontsize = 12)
plt.title('Confusion Matrix - Random Forest')
plt.show

#Naive Bayes
percentages_nb = np.round( (cm_nb.T/ np.sum(cm_nb, axis=1)).T*100, 1)
plt.figure(figsize=(6,4))
for i in range(3): 
    for j in range(3):
        if i == 0 and j == 0:  # Nếu vị trí là (0, 0)
            text_color = 'white'  # Màu trắng cho chữ
        else:
            text_color = 'black'  # Màu đen cho chữ
        plt.text(j + 0.5, i+0.5, f'{cm_nb[i,j]} ({percentages_nb[i,j]}%)', color = text_color , horizontalalignment = 'center', verticalalignment='center')
sns.heatmap(cm_nb, annot = False, cmap = cmap, fmt='', xticklabels=label_, yticklabels=label_)
plt.xlabel('Predicted', fontsize = 12)
plt.ylabel('Actual', fontsize = 12)
plt.title('Confusion Matrix - Naive Bayes')
plt.show


#Logistic Regression
percentages_lr = np.round( (cm_lr.T/ np.sum(cm_lr, axis=1)).T*100, 1)
plt.figure(figsize=(6,4))
for i in range(3):
    for j in range(3):
        if i == 0 and j == 0:  # Nếu vị trí là (0, 0)
            text_color = 'white'  # Màu trắng cho chữ
        else:
            text_color = 'black'  # Màu đen cho chữ
        plt.text(j + 0.5, i+0.5, f'{cm_lr[i,j]} ({percentages_lr[i,j]}%)', color = text_color , horizontalalignment = 'center', verticalalignment='center')
sns.heatmap(cm_lr, annot = False, cmap = cmap, fmt='', xticklabels=label_, yticklabels=label_)
plt.xlabel('Predicted', fontsize = 12)
plt.ylabel('Actual', fontsize = 12)
plt.title('Confusion Matrix - Logistic Regression')
plt.show


# KNN
percentages_knn = np.round((cm_knn.T / np.sum(cm_knn, axis=1)).T * 100, 1)
# Vẽ heatmap cho confusion matrix của KNN
plt.figure(figsize=(6, 4))
for i in range(cm_knn.shape[0]):
    for j in range(cm_knn.shape[1]):
        if i == 0 and j == 0:  # Nếu vị trí là (0, 0)
            text_color = 'white'  # Màu trắng cho chữ
        else:
            text_color = 'black'  # Màu đen cho chữ
        plt.text(j + 0.5, i + 0.5, f'{cm_knn[i, j]} ({percentages_knn[i, j]}%)', horizontalalignment='center',
                 verticalalignment='center', color = text_color)
sns.heatmap(cm_knn, annot=False, cmap=cmap, fmt='', xticklabels=label_, yticklabels=label_)
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.title('Confusion Matrix - KNN')
plt.show()


print('accuracy decisiontree = ',np.trace(cm_tree)/np.sum(cm_tree))
print('accuracy random forest = ',np.trace(cm_ran)/np.sum(cm_ran))
print('accuracy Naive Bayes = ', np.trace(cm_nb)/np.sum(cm_nb))
print('accuracy Logistic Regression = ',np.trace(cm_lr)/np.sum(cm_lr))
print('accuracy KNN = ', np.trace(cm_knn)/np.sum(cm_knn))
                  


with open(r"D:\7.reseach\predict_range_member_attendees\zzzDT_RF\resultFollowGroup.csv","w", newline = '')as file:
    csv_writer= csv.writer(file)
    csv_writer.writerow(['Decision tree','','','percent DT','accuracy decisiontree',  np.trace(cm_tree)/np.sum(cm_tree)])
    csv_writer.writerows(np.hstack((cm_tree,percentages_tree)))
    csv_writer.writerow(['Random Forest','','','percent RF','accuracy random forest',np.trace(cm_ran)/np.sum(cm_ran)])
    csv_writer.writerows(np.hstack((cm_ran,percentages_ran)))
    csv_writer.writerow(['Naive Bayes','','','percent NB','accuracy Naive Bayes ',np.trace(cm_nb)/np.sum(cm_nb)])
    csv_writer.writerows(np.hstack((cm_nb,percentages_nb)))
    csv_writer.writerow(['Logistic Regression','','','percent LR','accuracy Logistic Regression',np.trace(cm_lr)/np.sum(cm_lr) ])
    csv_writer.writerows(np.hstack((cm_lr,percentages_lr)))
    csv_writer.writerow(['K Nearest Neighbor ','','','percent KNN','accuracy KNN', np.trace(cm_knn)/np.sum(cm_knn)])
    csv_writer.writerows(np.hstack((cm_knn,percentages_knn)))


#trực quan Group box
boxTree =np.array([]) 
boxRan =np.array([]) 
boxNb =np.array([]) 
boxLr =np.array([]) 
boxKnn =np.array([]) 


boxTree= np.append(boxTree, 100*np.trace(cm_tree)/np.sum(cm_tree))
boxTree = np.concatenate((boxTree,np.diag(percentages_tree)), axis = 0)

boxRan= np.append(boxRan, 100*np.trace(cm_ran)/np.sum(cm_ran))
boxRan = np.concatenate((boxRan,np.diag(percentages_ran)), axis = 0)

boxNb= np.append(boxNb, 100*np.trace(cm_nb)/np.sum(cm_nb))
boxNb = np.concatenate((boxNb,np.diag(percentages_nb)), axis = 0)

boxLr= np.append(boxLr, 100*np.trace(cm_lr)/np.sum(cm_lr))
boxLr = np.concatenate((boxLr,np.diag(percentages_lr)), axis = 0)

boxKnn= np.append(boxKnn, 100*np.trace(cm_knn)/np.sum(cm_knn))
boxKnn = np.concatenate((boxKnn,np.diag(percentages_knn)), axis = 0)


data = np.array([boxTree, boxRan, boxNb, boxLr, boxKnn])

key_=['All','Small','Medium','Large']

# Tạo DataFrame từ các mảng
testdata = pd.DataFrame(data,
                        index= ['Decision Tree', 'Random Forest', 'Naive Bayes', 'Logistic Regression', 'KNN'],
                        columns=key_)

# Tạo pattern
pattern = ['', 'o', '.', '\\']

ax = testdata.plot.bar(width=0.7)

# Thiết lập pattern cho từng cột
for i, col in enumerate(testdata.columns):
    for j, patch in enumerate(ax.patches[i * 5: ]):
        patch.set_hatch(pattern[i])
        patch.set_linewidth(2) 
        
# Các chỉ mục và nhãn trục x
plt.xticks(rotation=10)
plt.ylabel("Percentage", fontsize=15, fontweight='bold')

# Hiển thị legend riêng lẻ cho các pattern
legend_elements = []
for i, col in enumerate(testdata.columns):
    # Tạo patch cho mẫu
    patch = Patch(facecolor='white', edgecolor='black', hatch=pattern[i], label=col)
    legend_elements.append(patch)
    # Tạo patch cho màu
    color_patch = Patch(facecolor=plt.cm.tab10(i), edgecolor='black', label="")  # Màu tự động từ cmap tab10
    legend_elements.append(color_patch)

plt.legend(bbox_to_anchor=(0.88, 1.14), ncol = 5)
# Hiển thị biểu đồ
plt.show()

