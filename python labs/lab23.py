#load csv file

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
#create contact list   
contacts = []
#use first line to create the keys
keys =lines[0].split(",")
#convert each list into its group of values and create dict for each contact 
for i in range(1,(len(lines))):
    line = lines[i].split(",")
    entry = dict(zip(keys, line))
    contacts.append(entry)

print(contacts)
