from pathlib import Path

def tokeninze(paragraphs):
    #loop through the paragraph put unique words in a dictionary
    unique_words = set()   
    words = paragraphs.split()
    for word in words:
        #for word in paragraph:
        unique_words.add(word)

    return unique_words
    

def remove_special_characters(paragraphs):
    #remove '.', ',','?', '"','"', '(',')', '<br', '/>', '''
    special_characters = ['.', ',','?', '"','"', '(',')', '<br', '/>', ","]
    removed_characters = []
    
    return removed_characters
    

def remove_numbers(paragraphs):
    #regex to remove digits
    pass

def to_lower(paragraphs):
    #call tolower funcition
    pass

def remove_stop_words(paragraphs,stopwords):
    #load stopwords into a list
    #loop through list and use python remove function
    #return file with no stop words
    pass

def stemmer(paragraphs):
    pass

def frequency(paragraphs):
    #count the frequency of every word
    #return dictionary
    pass

def write(freqs):
    #write the frequency matrix to a file
    pass

def read_file(filename):
    file_data = ""
    file_data= Path(filename).read_text()
    #with open(filename, 'r') as f:
    #    file_data = f.read()

    return file_data

def main():
    fd = read_file('Project4_paragraphs.txt')
    print(type(fd))
    token = tokeninze(fd)
    print(token)

if __name__ == '__main__':
    main()