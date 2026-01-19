from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as file:
        contents = file.read()
        words = contents.splitlines()
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    total = 0
    for letter in word:
        if letter.upper() in LETTER_SCORES.keys():
            total += LETTER_SCORES[letter.upper()]
    return total

def max_word_value(words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    maxValue = -1
    maxValueWord = ""
    
    for word in words:
        score = calc_word_value(word)
        if score > maxValue:
            maxValue = score
            maxValueWord = word
    
    return maxValueWord
    

if __name__ == "__main__":
    # run test from test_wordvalue.py
    pass