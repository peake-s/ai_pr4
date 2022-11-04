from . import PorterStemmer

def tokenize(paragraphs):
    words = paragraphs.split()

    return words
    

def remove_special_characters(paragraphs):
    special_characters = ['.', ',','?', '"','"', "(",")", "<br", "/>", ",","'","'",'!']
   
    removed_characters = paragraphs
    for i in special_characters:
        removed_characters = removed_characters.replace(i, '')
    
    return removed_characters
    

def remove_numbers(paragraphs):
    special_characters = ['0','1','2','3','4','5','6','7','8','9']
   
    removed_digits= paragraphs
    for i in special_characters:
        removed_digits = removed_digits.replace(i, '')
    
    return removed_digits

def to_lower(paragraph):
    data = [word.lower() for word in paragraph]
    return data

def remove_stop_words(words,stopwords):
    removed = []
    removed = [word for word in words if word not in stopwords]

    return removed

def stemmer(paragraph):
    port = PorterStemmer()
    pass

def frequency(words):
    unique_words = {}   
    
    for word in words:
        if word in unique_words:
            unique_words[word] += 1
        else:
            unique_words[word] = 1


def write(freqs):
    #write the frequency matrix to a file
    pass

def read_file(filename):
    file_data = []
    with open(filename, 'r') as f:
        #file_data = (f.readlines())
        file_data = f.read()

    #paragraphs
    splat = file_data.split('\n')

    return splat

def main():
    paragraph_list = read_file('Project4_paragraphs.txt','\n')
    stop_words = read_file('Project4_stop_words.txt','\n')
    ported_stemmed_pars = []

    for paragraph in paragraph_list:
        paragraph = remove_special_characters(paragraph)
        paragraph = remove_numbers(paragraph)
        tokenized_par = tokenize(paragraph)
        lower_toke = to_lower(tokenized_par)
        stop_words_removed = remove_stop_words(lower_toke,stop_words)


if __name__ == '__main__':
    main()