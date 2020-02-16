import csv
from datetime import datetime


data=[]

def printFile(path):
    file=open(path)
    #for line in file:
        #print(line)
    lines=[line for line in open(path)]
    print(lines[0])
    print(lines[1])

    dataset=[line.strip().split(',') for line in open(path)]
    for data in dataset:
        print(data)


def csvParse(path):
    file=open(path,newline='')
    reader=csv.reader(file)
    header=next(reader)

    for row in reader:
        date=datetime.strptime(row[0],'%m/%d/%Y')
        open_price=float(row[1])
        high=float(row[2])
        low=float(row[3])
        close=float(row[4])
        volume=int(row[5])
        adj_close=float(row[6])
        data.append([date,open_price,high,low,close,volume,adj_close])


def computeReturns():
    path="C:\\Users\Daemon\Python_learning\\returns.csv"
    file=open(path,'w',newline='')
    writer=csv.writer(file)
    writer.writerow(["Date", "Returns"])
    for i in range(len(data)-1):
        todays_row=data[i];
        todays_date=todays_row[0]
        todays_price=todays_row[-1]
        yesterdays_row=data[i+1]
        yesterdays_price=yesterdays_row[-1]
        daily_return=(todays_price-yesterdays_price)/yesterdays_price
        formatted_date=todays_date.strftime('%m/%d/%Y')
        writer.writerow([formatted_date,daily_return])



csvParse("C:\\Users\Daemon\Python_learning\Google Stock Market Data - google_stock_data.csv.csv")
computeReturns()

