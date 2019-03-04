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

word_dict = {}
text =load_text("The War of the Worlds.txt")
words = get_words(text)

for word in words:
    if word not in word_dict.keys():
        word_dict[word] = 1
    elif word in word_dict.keys():
        word_dict[word] += 1
        
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])