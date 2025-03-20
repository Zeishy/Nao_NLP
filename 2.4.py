import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')

def generate_synonyms(sentence):
    
    words = sentence.split()
    new_sentence = []

    for word in words:
        synonyms = wordnet.synsets(word)
        if synonyms:
            new_word = synonyms[0].lemmas()[0].name()
            new_sentence.append(new_word)
        else:
            new_sentence.append(word)

    return ' '.join(new_sentence)
