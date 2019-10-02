import datetime as dt
currentDT = dt.datetime.now()
print("current date n time:", currentDT)   #shows date n time

currentDT = dt.datetime.today()  #shows only date n time
print("current date n time:", currentDT)

currentDT = dt.date.today()
print("current date:", currentDT)      #shows todays date

currentYear=dt.date.today()
print("current year:",currentYear.year)       #shows year

currentMonth=dt.date.today()
print("current month:",currentMonth.month)    #shows month

currentWeek=dt.date.today()
print("current week:",currentYear.weekday())     #first week is 0

compDate=dt.date(1996,1,17)
thisYear=dt.date(2019,1,17)
difference=thisYear-compDate    #compares date
print(difference)    #or print(difference/365)

changeYear=compDate.replace(year=2020)           #chng yr
print(changeYear)
changeMonth=compDate.replace(month=9)        #chng month
print(changeMonth)
changeDay=compDate.replace(day=27)    #chng day
print(changeDay)
changeDT=compDate.replace(year=2021,month=3,day=30)   #chng all
print(changeDT)

compDate=dt.date(1996,1,17)
thisYear=dt.date(2019,1,17)
if thisYear > compDate:
    print(thisYear)
else:
    print(compDate)

timeVar=dt.time(23,50,12)     #shows time
print(timeVar)


