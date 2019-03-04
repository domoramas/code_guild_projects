# emoticon generator
import random
eye_list = [":", ";", "=","B"]
nose_list = ["^", "-","", "*"]
mouth_list =[")", "P", "(", "/" ]

for i in range(5):
    emoticon = random.choice(eye_list) + random.choice(nose_list) + random.choice(mouth_list)
    print(emoticon)