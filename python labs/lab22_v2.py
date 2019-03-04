import math
import sys

#open text file:
def load_text(path):
    with open(path) as text_file:
        test_text = text_file.read().strip('\n')
    return test_text
  #gets list of sentences:    
def get_sentences(test_text):
    test_text.replace("?",".")
    test_text.replace("!", ".")
    sentences= test_text.split(".")
    return sentences

#gets list of words
def get_words(sentences):
    words = "".join(sentences).split()
    return words
#gets list of all letters
def get_char(words):
    char = "".join(words)
    return char
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

try:
    test_text = load_text(sys.argv[1])
    sentences = get_sentences(test_text)
    print(len(sentences))
    words = get_words(sentences)
    print(len(words))
    char = get_char(words)
    print(len(char))
    ari =math.ceil(4.71*(len(char)/len(words)) + .5*(len(words)/len(sentences)) - 21.43)

    print(f' The ARI for {sys.argv[1]} is {ari} \n This corresponds to a {(ari_scale[ari]["grade_level"])} level of difficulty \n that is suitable for an average person {(ari_scale[ari]["ages"])} years old.')
except:
    print("invalid input")