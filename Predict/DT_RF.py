import csv

import pandas as pd
import numpy as np
import sklearn

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


X = data[features]
Y = data['class']


X_train = X.iloc[:int(0.8 * len(data))]
X_test = X.iloc[int(0.8 * len(data)):]
Y_train = Y.iloc[:int(0.8 * len(data))]
Y_test = Y.iloc[int(0.8 * len(data)):]


# Tạo mô hình Decision Tree
decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, Y_train)
y_pred_tree = decision_tree.predict(X_test)
accuracy_tree = accuracy_score(Y_test, y_pred_tree)


#random forest
random_forest = RandomForestClassifier(random_state=42)
random_forest.fit(X_train, Y_train)
y_pred_forest = random_forest.predict(X_test)
accuracy_forest = accuracy_score(Y_test, y_pred_forest)

#navie bayes
naive_bayes = GaussianNB()
naive_bayes.fit(X_train, Y_train)
y_pred_nb = naive_bayes.predict(X_test)
accuracy_nb = accuracy_score(Y_test, y_pred_nb)


#logistic Regression
logistic_regression = LogisticRegression(random_state=42)
logistic_regression.fit(X_train,Y_train)
y_pred_lr = logistic_regression.predict(X_test)
accuracy_lr = accuracy_score(Y_test,y_pred_lr)


X_train = X_train.to_numpy()
Y_train = Y_train.astype(int).to_numpy()
X_test = X_test.to_numpy()
Y_test = Y_test.astype(int).to_numpy()

# KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)
y_pred_knn = knn.predict(X_test)
accuracy_knn = accuracy_score(Y_test, y_pred_knn)



print(f"Decision Tree Accuracy: {accuracy_tree}")
print(f"Random Forest Accuracy: {accuracy_forest}")
print(f"Naive Bayes Accuracy: {accuracy_nb}")
print("Logistic Regression Accuracy: ", accuracy_lr)
print("KNN Accuracy (k=5): ", accuracy_knn)

label_ = ['Small','Medium', 'Large']


#tạo cmap color
colors=[(1,1,1),(0.4,0.4,0.4)]
cmap = mcolors.LinearSegmentedColormap.from_list('mycmap',colors,N=250)

# Confusion matrix và heatmap cho Decision Tree
cm_tree = confusion_matrix(Y_test, y_pred_tree)
# Tính phần trăm dữ liệu trong từng ô của confusion matrix
percentages_tree = np.round( (cm_tree.T / np.sum(cm_tree,axis = 1)).T * 100, 1)
# Tạo heatmap với số lượng và phần trăm dữ liệu
plt.figure(figsize=(6, 4))
for i in range(cm_tree.shape[0]):
    for j in range(cm_tree.shape[1]):
        if i == 0 and j == 0:  # Nếu vị trí là (0, 0)
            text_color = 'white'  # Màu trắng cho chữ
        else:
            text_color = 'black'  # Màu đen cho chữ
        plt.text(j + 0.5, i + 0.5, f'{cm_tree[i, j]} ({percentages_tree[i, j]}%)', horizontalalignment='center',
                  verticalalignment='center', color= text_color)
sns.heatmap(cm_tree, annot=False, cmap=cmap, fmt='', xticklabels=label_, yticklabels=label_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Decision Tree')
plt.show()


# Confusion matrix và heatmap cho Random Forest
cm_forest = confusion_matrix(Y_test, y_pred_forest)
# Tính phần trăm dữ liệu trong từng ô của confusion matrix
percentages_ran = np.round ( ( cm_forest.T/np.sum(cm_forest,axis=1)).T *100, 1)
# Tạo heatmap với số lượng và phần trăm dữ liệu
plt.figure(figsize=(6, 4))
for i in range(cm_forest.shape[0]):
    for j in range(cm_forest.shape[1]):
        if i == 0 and j == 0:  # Nếu vị trí là (0, 0)
            text_color = 'white'  # Màu trắng cho chữ
        else:
            text_color = 'black'  # Màu đen cho chữ
        plt.text(j + 0.5, i + 0.5, f'{cm_forest[i, j]} ({percentages_ran[i, j]}%)', horizontalalignment='center', verticalalignment='center', color= text_color)
sns.heatmap(cm_forest, annot=False, cmap=cmap, fmt='d', xticklabels=label_, yticklabels=label_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Random Forest')
plt.show()

# Confusion matrix và heatmap cho Naive Bayes
cm_nb = confusion_matrix(Y_test, y_pred_nb)
plt.figure(figsize=(6, 4))
# Tính phần trăm dữ liệu trong từng ô của confusion matrix
percentages_nb = np.round( (cm_nb.T/ np.sum(cm_nb, axis=1)).T*100, 1)
# Tạo heatmap với số lượng và phần trăm dữ liệu
plt.figure(figsize=(6, 4))
for i in range(cm_nb.shape[0]):
    for j in range(cm_nb.shape[1]):
        if i == 0 and j == 0:  # Nếu vị trí là (0, 0)
            text_color = 'white'  # Màu trắng cho chữ
        else:
            text_color = 'black'  # Màu đen cho chữ
        plt.text(j + 0.5, i + 0.5, f'{cm_nb[i, j]} ({percentages_nb[i, j]}%)', horizontalalignment='center', verticalalignment='center', color= text_color)
sns.heatmap(cm_nb, annot=False, cmap=cmap, fmt='d', xticklabels=label_, yticklabels=label_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Naive Bayes')
plt.show()


# Confusion matrix và heatmap cho Logistic Regression
cm_lr = confusion_matrix(Y_test, y_pred_lr)
# Tính phần trăm dữ liệu trong từng ô của confusion matrix
percentages_lr = np.round( (cm_lr.T/ np.sum(cm_lr, axis=1)).T*100, 1)
# Tạo heatmap với số lượng và phần trăm dữ liệu
plt.figure(figsize=(6, 4))
for i in range(cm_lr.shape[0]):
    for j in range(cm_lr.shape[1]):
        if i == 0 and j == 0:  # Nếu vị trí là (0, 0)
            text_color = 'white'  # Màu trắng cho chữ
        else:
            text_color = 'black'  # Màu đen cho chữ
        plt.text(j + 0.5, i + 0.5, f'{cm_lr[i, j]} ({percentages_lr[i, j]}%)', horizontalalignment='center', verticalalignment='center', color= text_color)
sns.heatmap(cm_lr, annot=False, cmap=cmap, fmt='d', xticklabels=label_, yticklabels=label_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Logistic Regression')
plt.show()

# Confusion matrix và heatmap cho KNN
cm_knn = confusion_matrix(Y_test, y_pred_knn)
# Tính phần trăm dữ liệu trong từng ô của confusion matrix
percentages_knn = np.round((cm_knn.T / np.sum(cm_knn, axis=1)).T * 100, 1)
# Tạo heatmap với số lượng và phần trăm dữ liệu
plt.figure(figsize=(6, 4))
for i in range(cm_knn.shape[0]):
    for j in range(cm_knn.shape[1]):
        if i == 0 and j == 0:  # Nếu vị trí là (0, 0)
            text_color = 'white'  # Màu trắng cho chữ
        else:
            text_color = 'black'  # Màu đen cho chữ
        plt.text(j + 0.5, i + 0.5, f'{cm_knn[i, j]} ({percentages_knn[i, j]}%)', horizontalalignment='center', verticalalignment='center', color= text_color)
sns.heatmap(cm_knn, annot=False, cmap=cmap, fmt='d', xticklabels=label_, yticklabels=label_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - KNN')
plt.show()


# Gini importance của Random Forest
importances = random_forest.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(10, 6))
plt.bar(range(X.shape[1]), importances[indices], color="skyblue", align="center")
plt.xticks(range(X.shape[1]), [features[i] for i in indices], rotation=20, fontsize = 14, fontweight = 'bold')
plt.yticks(fontsize = 12, fontweight = 'bold')
plt.xlim([-1, X.shape[1]])
plt.show()






with open(r"D:\7.reseach\predict_range_member_attendees\zzzDT_RF\resultFullData.csv","w", newline = '')as file:
    csv_writer= csv.writer(file)
    csv_writer.writerow(['Decision tree','','','percent DT','accuracy decisiontree',  accuracy_tree])
    csv_writer.writerows(np.hstack((cm_tree,percentages_tree)))
    csv_writer.writerow(['Random Forest','','','percent RF','accuracy random forest',accuracy_forest])
    csv_writer.writerows(np.hstack((cm_forest,percentages_ran)))
    csv_writer.writerow(['Naive Bayes','','','percent NB','accuracy Naive Bayes ',accuracy_nb])
    csv_writer.writerows(np.hstack((cm_nb,percentages_nb)))
    csv_writer.writerow(['Logistic Regression','','','percent LR','accuracy Logistic Regression',accuracy_lr ])
    csv_writer.writerows(np.hstack((cm_lr,percentages_lr)))
    csv_writer.writerow(['K Nearest Neighbor ','','','percent KNN','accuracy KNN', accuracy_knn])
    csv_writer.writerows(np.hstack((cm_knn,percentages_knn)))




#trực quan Group box
boxTree =np.array([]) 
boxRan =np.array([]) 
boxNb =np.array([]) 
boxLr =np.array([]) 
boxKnn =np.array([]) 


boxTree= np.append(boxTree, 100*accuracy_tree)
boxTree = np.concatenate((boxTree,np.diag(percentages_tree)), axis = 0)

boxRan= np.append(boxRan, 100*accuracy_forest)
boxRan = np.concatenate((boxRan,np.diag(percentages_ran)), axis = 0)

boxNb= np.append(boxNb, 100*accuracy_nb)
boxNb = np.concatenate((boxNb,np.diag(percentages_nb)), axis = 0)

boxLr= np.append(boxLr, 100*accuracy_lr)
boxLr = np.concatenate((boxLr,np.diag(percentages_lr)), axis = 0)

boxKnn= np.append(boxKnn, 100*accuracy_knn)
boxKnn = np.concatenate((boxKnn,np.diag(percentages_knn)), axis = 0)

data = np.array([boxTree, boxRan, boxNb, boxLr, boxKnn])

key_=['All','Small','Medium','Large']

# Tạo DataFrame từ các mảng
testdata = df = pd.DataFrame(data,
                             index= ['Decision Tree', 'Random Forest', 'Naive Bayes', 'Logistic Regression', 'KNN'],
                             columns=key_)




# Tạo pattern
pattern = ['', 'o', '.', '\\']

ax = testdata.plot.bar(width=0.7)

# Thiết lập pattern cho từng cột
for i, col in enumerate(testdata.columns):
    for j, patch in enumerate(ax.patches[i * 5: ]):
        patch.set_hatch(pattern[i])
        
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
plt.show()













