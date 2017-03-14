""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THE PROJECT GUTENBERG EBOOK') == -1:
    	curr_line += 1
    lines = lines[curr_line+1:]

    words = []

    for i in lines:
    	singular_word = ''
    	j = 0
    	i = i.lower()
    	while j < len(i):
    		if i[j] in string.punctuation:
    			i = i.replace(i[j]," ")

    		if i[j] not in string.whitespace:
    			singular_word += i[j]

    		if (j+1 < len(i)) and i[j+1] in string.whitespace:
    			if singular_word != '':
    				words.append(singular_word)
    			j +=2
    			singular_word = ''
    		else:
    			j += 1
    return(words)


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    word_dict = {}
    for word in word_list:
    	if word in word_dict:
    		word_dict[word] += 1
    	else:
    		word_dict[word] = 1

    word_dict = sorted(word_dict, key = word_dict.get, reverse = True)
    return(word_dict[:n])


if __name__ == "__main__":
    print(get_top_n_words(get_word_list('WutheringHeights.txt'), 100))
