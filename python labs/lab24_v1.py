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
       
heavy_rain =[]
for i in range(0,len(date_rain)):
    if date_rain[i]["rain"] > 250:
    
        heavy_rain.append((date_rain[i]["date"].strftime("%b-%Y"),date_rain[i]["rain"]))

print(heavy_rain)