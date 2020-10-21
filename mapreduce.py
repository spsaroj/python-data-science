import sys
import string

def mapper():
    for line in sys.stdin:
        data = line.strip().split(" ")
        for i in data:
            cleaned_data = i.translate(string.maketrans(","), string.punctuation).lower()
            #emit a key-value pair
            print("{0}\t{1}".format(cleaned_data, 1))

def reducer():
    word_count = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if( len(data) != 2):
            continue
        
        this_key, count = data
        if( old_key and old_key != this_key ):
            print("{0}\t{1}".format(old_key, word_count))
            word_count = 0
        
        old_key = this_key
        word_count += float(count)
    
    if(old_key != None):
        print("{0}\t{1}".format(old_key, word_count))