#Lab 21: Count Words

#open the file
def load_text(path):
    with open(path) as text_file:
        text = text_file.read().strip('\n').lower()
    return text

def get_words(text):
    text.replace(","," ")
    text.replace("."," ")
    text.replace("!"," ")
    text.replace("?"," ")
    text.replace("'","")
    words = text.split()
    return words

path = "The War of the Worlds.txt"
text =load_text(path)
word_list = get_words(text)
word_dict = {}

for i in range(0,(len(word_list) -1)):
    if (word_list[i], word_list[i+1]) not in word_dict.keys(): #looks to see if pair in dict 
        word_dict[(word_list[i], word_list[i+1])] = 1
    elif (word_list[i], word_list[i+1]) in word_dict.keys(): # adds occurance if already in dict
        word_dict[(word_list[i], word_list[i+1])] += 1
        
# words = list(word_dict.items()) # .items() returns a list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])
word_find = input(f"Type in a word to find the words which most frequently follow it in {path}: ").lower()
words_found = {k:v for k, v in word_dict.items() if word_find == k[0]} # looks for input word in the first place in tuple keys saves as new dict
found = list(words_found.items())
found.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(found))):  # print the top 10 words, or all of them, whichever is smaller
    print(found[i])