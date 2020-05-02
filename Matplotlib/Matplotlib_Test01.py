import matplotlib as mpl
import matplotlib.pyplot as plt

print('line plot 그리기')
plt.title('test')
plt.plot([1,2,3,4],[2,4,8,6])
plt.plot([1.5,2.5,3.5,4.5],[3,5,8,10])  # 새로운 라인 추가
plt.xlabel('hours')                     # x축의 이름
plt.ylabel('score')                     # y축의 이름
plt.legend(['A student', 'B student'])  #범례 삽입
plt.show()
print('\n')

print('축 그리기')
plt.title('test')
plt.plot([1,2,3,4],[2,4,8,6])
plt.show()
print('\n')