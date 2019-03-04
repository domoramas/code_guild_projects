# emoticon generator
import random
emoticon_dict ={ 
    "eyes" : [":", ";", "=","B"], 
    "noses" : ["^", "-","", "*"], 
    "mouths" :[")", "P", "(", "/" ]}

for i in range(5):
    emoticon = random.choice(emoticon_dict["eyes"])+random.choice(emoticon_dict["noses"])+random.choice(emoticon_dict["mouths"])
    print(emoticon)
    