import json
import csv
 
filename = 'adm1'
# Opening JSON file and loading the data
# into the variable data
with open('output/{}.json'.format(filename)) as json_file:
    data = json.load(json_file)

count = 0
count_split=1
splitter = 10
new_file = True
data_file = open("output/csv/{}/{}.csv".format(filename,count_split), 'w')
csv_writer = csv.writer(data_file)
for item in data:
    # Writing data of CSV file
    if count <= (splitter*count_split) :
        if new_file:
            header = item.keys()
            csv_writer.writerow(header)
            new_file = False
        csv_writer.writerow(item.values())
        count += 1
    else:
        count_split +=1
        data_file.close()
        data_file = open("output/csv/{}/{}.csv".format(filename,count_split), 'w')
        csv_writer = csv.writer(data_file)
        header = item.keys()
        csv_writer.writerow(header)
        csv_writer.writerow(item.values())
        count += 1
data_file.close()