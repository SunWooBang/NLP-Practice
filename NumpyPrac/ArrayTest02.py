import numpy as np
'''numpy 슬라이싱 연습!'''
a = np.array([[2, 3, 4],[5, 6, 7]])
b = a[0:2, 0:2]
print("<a배열>")
print(a)

print("<b배열>")
print(b)
print('\n')

#다차원 배열 슬라이싱 -> 각 차원별로 범위 지정!
print("<범위지정 슬라이싱1>")
b=a[0, :] #a배열의 첫째 행 출력
print(b)

print("<범위지정 슬라이싱2>")
b=a[1, 1] #a배열의 2행2열 요소 출력
print(b)
print('\n')

print("<정수 인덱싱>")
a = np.array([[20,40], [50,60], [100,300]])
b = a[[2, 1],[1, 0]]    # a[[row2, row1],[col1, col0]]
print(b)
print('\n')

print("<Numpy 연산 - 요소끼리의 사칙연산>")
#Numpy를 이용하여 배열간 연산 용이함
x = np.array([1,2,3])
y = np.array([4,5,6])
b = np.add(x, y)        # 행렬 요소끼리 덧셈
print('덧셈: '+b)
b = np.substract(x, y)  # 행렬 요소끼리 뺄셈
print('뺄셈: '+b)
b = np.multiply(b, x)   # 행렬 요소끼리 곱셈
print('곱셈: '+b)
b = np.divide(b, x)     # 행렬 요소끼리 나눗셈
print('나눗셈: '+b)
print('\n')

print("<Numpy 연산 - 행렬간 행렬곱>")
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.dot(a, b)
print(c)
