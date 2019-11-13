import csv

def get_data_from_csv(fileName):
    return (list(csv.reader(open(fileName))))

def receive_new_record():
    event = input("Event > ")
    gender = input("Sex > ")
    performance = input("Performance > ")

    data = get_data_from_csv ("wr.csv")
    for record in data:
        if record[0] == event and record[1] == gender and float(record[2]) > int(performance):
            record[2] = performance
            print("New record! Saving...")
            data_out(record, data.index(record), "wr.csv")
            print("Saved.")

def data_out(data, index, fileName):
    override = { index : data }
    
    dataList = []
    with open(fileName, "r") as f:
        readCSV = csv.reader(f)
        dataList.extend(readCSV)
    
    with open(fileName, "w") as f:
        writer = csv.writer(f)
        for line, row in enumerate(dataList):
            newRow = override.get(line,row)
            writer.writerow(newRow)

while True:
    if input("\n1. Enter new performance\n2. View world records\n\n> ") == '1':
        receive_new_record()
    else:
        for record in get_data_from_csv ("wr.csv"):
            print(record)
