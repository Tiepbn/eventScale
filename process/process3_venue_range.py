import csv
from math import sin, cos, sqrt, atan2, radians

list_venue_evid = []

with open("D:/7.reseach/filter4_drop-under_5_event_in_group/venue_filter4.csv", 'r', encoding='iso-8859-1') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list_venue_evid.append(row)

# Bán kính của trái đất (km)
R = 6373.0

# Danh sách mới để lưu các danh sách event ID thỏa mãn điều kiện
list_evid_venue_500m = []

for i in range(len(list_venue_evid)):
    lat1 = radians(float(list_venue_evid[i][7]))
    lon1 = radians(float(list_venue_evid[i][8]))
    print(i)
    # Danh sách event ID thỏa mãn điều kiện cho dòng hiện tại
    events_within_500m = []
    events_within_500m.append(list_venue_evid[i][2])

    for j in range(len(list_venue_evid)):        
        if i != j:  # Để tránh tính khoảng cách từ một dòng đến chính nó
            lat2 = radians(float(list_venue_evid[j][7]))
            lon2 = radians(float(list_venue_evid[j][8]))

            dlon = lon2 - lon1
            if abs(dlon) > radians(0.0108):
                continue
            
            dlat = lat2 - lat1
            
            if abs(dlat) > radians(0.0083):
                continue            

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = R * c

            if distance < 0.5:
                events_within_500m.append(list_venue_evid[j][2])  # Thêm event ID vào danh sách
    list_evid_venue_500m.append(events_within_500m)
 
with open("D:/7.reseach/process3_venue_range/venue_process3.csv", "w", encoding = "iso-8859-1", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(list_evid_venue_500m)  