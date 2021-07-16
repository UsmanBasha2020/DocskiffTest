from datetime import date, timedelta
from calendar import SATURDAY

def return_interval_dates(startDate,endDate):
   
    startYear = int(startDate[0:4])
    startMonth = int(startDate[4:6])
    startDay = int(startDate[6:])

    endYear = int(endDate[0:4])
    endMonth = int(endDate[4:6])
    endDay = int(endDate[6:])

    if startYear >= 1900 and endYear <= 2100:
        sdate = date(startYear, startMonth, startDay)   # start date
        edate = date(endYear, endMonth, endDay)   # end date

        delta = edate - sdate       # as timedelta
       
        list_of_dates = []
        temp_year = ''
        temp_month = ''
        for i in range(delta.days + 1):
            cur_day = sdate + timedelta(days=i)

            if cur_day.weekday() == SATURDAY:
                day = cur_day.day
                if (day in range(22, 28 + 1)):
                    if day%5 != 0:
                        if(cur_day.month < 10):
                            month = '0'+str(cur_day.month)
                        else: 
                            month = str(cur_day.month)

                        if cur_day.day < 10:
                            day = '0'+str(cur_day.day)
                        else:
                            day = str(cur_day.day)
                        print(str(cur_day.year)+month+day)

                elif(day % 5 == 0):
                    if(cur_day.month < 10):
                        month = '0'+str(cur_day.month)
                    else: 
                        month = str(cur_day.month)

                    if cur_day.day < 10:
                        day = '0'+str(cur_day.day)
                    else:
                        day = str(cur_day.day)
                    print(str(cur_day.year)+month+day)


return_interval_dates('20180728','20180927')
