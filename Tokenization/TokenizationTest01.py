# *nltk를 이용한 단어 토큰화*
from nltk.tokenize import word_tokenize

print(word_tokenize(
    "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))

from nltk.tokenize import WordPunctTokenizer

print(WordPunctTokenizer().tokenize(
    "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))

# *케라스를 이용한 단어 토큰화*
from tensorflow.keras.preprocessing.text import text_to_word_sequence

print(text_to_word_sequence(
    "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))


