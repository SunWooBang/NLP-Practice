import numpy as np

print('\n <<np.array() 연습>>')

#1차원 배열
a = np.array([1,2,3,4,5,6])
print(type(a))
print(a, '\n')

#2차원 배열
a = np.array([[1,2,3,4],[60,70,80,90]])    #array()에는 하나의 리스트만 들어가므로 리스트의 리스트를 넣어야 함
print(a, '\n')

print('\n<<ndarray 초기화>>')
print('.zeros() 사용 ')
a = np.zeros((4,7)) #모든 값이 0인 4 x 7 배열 생성
print(a, '\n')

print('.ones() 사용 ')
a = np.ones((3,4)) #모든 값이 1인 3 x 4 배열 생성
print(a, '\n')

print('.full() 사용 ')
a = np.full((5,3), 13) # 모든 값이 특정 상수 13인 배열 생성
print(a, '\n')

print('.eye() 사용 ')
a = np.eye(5) # 대각선으로는 1이고 나머지는 0인 2차원 배열을 생성.(5 x 5)
print(a, '\n')

print('.random() 사용 ')
a = np.random.random((3,2)) # 임의의 값으로 채워진 배열 생성
print(a, '\n')


print('.arange() 사용 ')
a = np.arange(15) # 0부터 14까지(0~n-1)
print(a)

a = np.arange(0, 15, 3) #0부터 14까지 +3씩 적용
print(a, '\n')

print('.reshape() 사용')
a = np.array(np.arange(30)).reshape((5,6))  #0부터19까지의 다차원 배열 생성(4 x 3)
print(a, '\n')
