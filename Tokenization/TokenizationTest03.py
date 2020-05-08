print("한국어 특성상 단어 단위 토큰화가 아닌 형태소 토큰화를 해주어야한다. \n")

#NLTK 품사 태깅
from nltk.tokenize import word_tokenize
text="I am actively looking for Ph.D. students. and you are a Ph.D. student."
print(word_tokenize(text))

#konlpy 형태소 분석기. Okt, 메캅, 코모란, 한나눔, 꼬꼬마 제공.
'''
morphs: 형태소 추출
pos: 품사 태깅 
nouns: 명사 추출
'''
#Okt 이용.(konlpy)

from konlpy.tag import Okt  
okt=Okt()  
print(okt.morphs("싸늘하다. 비수가 날아와 가슴에 꽂힌다."))
print(okt.pos("싸늘하다. 비수가 날아와 가슴에 꽂힌다."))
print(okt.nouns("싸늘하다. 비수가 날아와 가슴에 꽂힌다."))

# kkma 이용.(konlpy)
from konlpy.tag import Kkma
kkma=Kkma()
print(kkma.morphs("싸늘하다. 비수가 날아와 가슴에 꽂힌다."))
print(kkma.pos("싸늘하다. 비수가 날아와 가슴에 꽂힌다."))
print(kkma.nouns("싸늘하다. 비수가 날아와 가슴에 꽂힌다."))