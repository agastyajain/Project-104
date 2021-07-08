import csv
from collections import Counter
with open('Height.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)
data = Counter(new_data)
mode_data_range = { 
    '20-50' : 0 ,
    '50-70' : 0 , 
    '70-100' : 0,
}
for Height,occurence in data.items():
    if 20<float(Height) < 50 :
        mode_data_range['20-50'] += occurence
    elif 50<float(Height) < 70 :
        mode_data_range['50-70'] += occurence
    elif 70<float(Height) < 100 :
        mode_data_range['70-100'] += occurence
mode_range , mode_occurence = 0,0 
for range,occurence in mode_data_range.items():
    if occurence > mode_occurence:
        mode_range,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode = float((mode_range[0]+mode_range[1])/2)
print(f"Mode is : {mode:2f}")
