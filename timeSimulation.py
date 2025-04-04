import csv
import datetime
def loader():
    global dater
    itemObj=open('items.csv','r',newline="")
    csvreader=csv.reader(itemObj)
    head=next(csvreader)
    dater={} #k,v pairs of item id, [expiry date, uses, waste status]
    for row in csvreader:
        try:
            dater[int(row[0])]=[datetime.date.fromisoformat(row[7]), int(row[8].split()[0]), "Not Waste"]
        except:
            dater[int(row[0])]=["no expiry", int(row[8].split()[0]), "Not Waste"]
    itemObj.close()
def currStatus():
    global currDate
    global dater
    global disposalList
    opDict={}
    for itemID in dater:
        if dater[itemID][0]=="no expiry":
            daysLeft="N/A"
        else:
            daysLeft=(dater[itemID][0]-currDate).days
            if daysLeft<=0:
                dater[itemID][2]="Expired"
        if dater[itemID][1]<1:
            dater[itemID][2]="Used"
        uses=dater[itemID][1]
        stat=dater[itemID][2]
        opDict[itemID]=(daysLeft,uses,stat)
        if (itemID not in disposalList) and (dater[itemID][2]!="Not Waste"):
            disposalList.append(itemID)
    return opDict
def shiftCurrentDate(dailyUseList,n=1):
    global currDate
    global dater
    global disposalList
    currDateOriginal=currDate
    currDate=currDate+datetime.timedelta(days=n)
    for itemID in dater:
        if dater[itemID][0]=="no expiry":
            if itemID in dailyUseList:
                usesLeft=dater[itemID][1]
                if usesLeft>=n:
                    useItem(itemID,n)
                    print(itemID,"used for ",n," days.")
                elif usesLeft==0:
                    pass
                else:
                    useItem(itemID,usesLeft)
                    print(itemID,"completely used up in ",usesLeft," days.")
            continue
        else:
            if dater[itemID][2]!="Not Waste":
                continue
            daysLeft=(dater[itemID][0]-currDate).days
            daysToExpiry=(dater[itemID][0]-currDateOriginal).days
            if daysLeft<0:
                dater[itemID][2]="Expired"
                if itemID not in disposalList:
                    disposalList.append(itemID)
            if itemID in dailyUseList:
                usesLeft=dater[itemID][1]
                if usesLeft>=n and (daysToExpiry)>=n:
                    useItem(itemID,n)
                    print(itemID,"used for",n," days")
                elif usesLeft>=n and (daysToExpiry)<n:
                    useItem(itemID,daysToExpiry)
                    print(itemID,"expired in ",daysToExpiry," days")
                elif usesLeft<n and (daysToExpiry)>=n:
                    useItem(itemID,usesLeft)
                    print(itemID,"completely used up in ",usesLeft," days.")
                elif usesLeft<n and daysToExpiry<n:
                    limiter=min([usesLeft,daysToExpiry])
                    useItem(itemID,limiter)
                    if usesLeft<daysToExpiry:
                        print(itemID,"completely used up in ",usesLeft," days.")
                    else:
                        print(itemID,"expired in ",daysToExpiry," days")                
def useItem(itemID,n):
    global dater
    global disposalList
    found=False
    for objID in dater:
        if objID==itemID:
            found=True
            dater[itemID][1]=dater[itemID][1]-n
            if dater[itemID][1]==0:
                dater[itemID][2]="Used"
                if itemID not in disposalList:
                    disposalList.append(itemID)
            break
    else:
        if not found:
            print("Item not found")

disposalList=[]
dater={}
curd=input("Enter start date")
currDate=datetime.date.fromisoformat(curd)
loader()
while True:
    print("Enter choice")
    print("1) Current status")
    print("2) Simulate n days")
    n=int(input())  
    if n==1:
        opDict=currStatus()
        print("item id, days to expiry, uses left, waste status")
        for itemID in opDict:
            print(itemID,": ",opDict[itemID][0]," days; ",opDict[itemID][1]," uses;",opDict[itemID][2])
        print("Disposal list: ",disposalList)
    elif n==2:
        dailyUseList=[]
        x=int(input("Enter delta: "))
        f=open('dailyUse.csv','r',newline='')#csv containing itemIDs of daily use items
        csvreader=csv.reader(f)
        head=next(csvreader)
        for row in csvreader:
            dailyUseList.append(int(row[0]))
        f.close()
        shiftCurrentDate(dailyUseList,x)

    
