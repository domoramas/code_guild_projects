#rain data 
# need to load the file
import datetime
def load_text(path):
    with open(path) as text_file:
        data_table = text_file.read().strip('\n')
    return data_table

data_table = load_text("skyline_school.rain.txt")
data_lines  = data_table.split("\n")
data_lines = list(data_lines)
date_rain = []
for i in range(0,len(data_lines)):
    date = data_lines[i][0:11]
    try:
        date = datetime.datetime.strptime(date, '%d-%b-%Y')
    except:
        date
    rain_total = ((data_lines[i][11:17]).strip())
    try:
        rain_total = int(rain_total)
        date_rain.append({"date":date, "rain" :rain_total})  
    except:
        pass
       
# #mean
total = []
for i in range (len(date_rain)):
    total.append(date_rain[i]['rain'])
mean = round(sum(total)/len(total),2)
print(f'the mean is {mean}')

# #variance
v_total = [(((date_rain[x]["rain"]) - mean) **2) for x in range(len(date_rain))] #comprehension for variance
variance = round(sum(v_total)/len(v_total),2)
print(f'the variance is {variance}')

# #most rain:
date_rain.sort(key= lambda dictionary: dictionary["rain"], reverse=True)
print(f'Highest daily rain total: {(date_rain[0]["date"]).strftime("%d-%b-%Y")} with {(date_rain[0]["rain"])}')

#rain_years:
years= {}
for i in range (len(date_rain)):
        if ((date_rain[i]["date"]).year) not in years: #creates key with year and starts list of rain totals for values
            years[(date_rain[i]["date"]).year] = [(date_rain[i]["rain"])]
        elif ((date_rain[i]["date"]).year) in years:
           years[(date_rain[i]["date"]).year].append(date_rain[i]["rain"]) #adds rain totals to matching year
yearly_totals ={k:(round(sum(years[k])/len(years[k]),2)) for k in years.keys()}  # iterates through keys to get the average of each list of values  

yearly_total = list(yearly_totals.items()) # .items() returns a list of tuples
yearly_total.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
most_rain = yearly_total[0] # saves highest rain total
print(f'The year with the highest rain fall ave: {most_rain}')