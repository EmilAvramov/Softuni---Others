from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from collections import Counter


def get_part_of_speech(word):
    probable_part_of_speech = wordnet.synsets(word)

    pos_counts = Counter()

    pos_counts["n"] = len([item for item in probable_part_of_speech
                           if item.pos() == "n"])
    pos_counts["v"] = len([item for item in probable_part_of_speech
                           if item.pos() == "v"])
    pos_counts["a"] = len([item for item in probable_part_of_speech
                           if item.pos() == "a"])
    pos_counts["r"] = len([item for item in probable_part_of_speech
                           if item.pos() == "r"])

    most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
    return most_likely_part_of_speech


lemmatizer = WordNetLemmatizer()

populated_island = 'Indonesia was founded in 1945. It contains the ' \
                   'most populated island in the world, Java, ' \
                   'with over 140 million people.'

tokenized_string = word_tokenize(populated_island)
lemmatized_pos = [lemmatizer.lemmatize(i, get_part_of_speech(i))
                  for i in tokenized_string]


try:
    print(f'The lemmatized words are: {lemmatized_pos}')
except:
    print('Expected a variable called `lemmatized_pos`')