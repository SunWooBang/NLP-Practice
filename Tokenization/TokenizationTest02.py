#*nltk를 이용한 문장 토큰화*
from nltk.tokenize import sent_tokenize
text = "His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to mae sure no one was near."
print(sent_tokenize(text))

#문장에 온점이 많이 나오는 경우
from nltk.tokenize import sent_tokenize
text="I am actively looking for Ph.D. students. and you are a Ph.D student."
print(sent_tokenize(text))

#kss를 이용한 한국어 문장 토큰화
import kss
text='나는 관대하다. 관 씨 집안 3대 독자다. 내 이름은 대하다. 그래서 나는 관대하다'
print(kss.split_sentences(text))