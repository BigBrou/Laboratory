from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben_hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]


# 막대기가 기본 값이 0.8
xs = [i + 0.1 for i, _ in enumerate(movies)]

# 왼쪽 x 축 위치
plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)
#plt.show()





#Histogram
from collections import Counter

grades = [83, 95, 91, 87, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

print(histogram)

plt.bar([x for x in histogram.keys()], histogram.values(), 8)   #x axis for keys y axis for values, height 8
plt.axis([-5, 105, 0, 5])                                           #x range between -5 and 105 / y range between 0 and 5
plt.xticks([10 * i for i in range(11)])                             #x label = xticks
plt.ylabel("# of Students")
plt.xlabel("Distribution of Exam 1 Grades")
#plt.show()





mentions = [500, 505]
years = [2013, 2014]

plt.bar(years, mentions, 0.8, color = "red")
plt.xticks(years)
#plt.ticklabel_format(useOffest=False) # 지금은 사용되는 지 잘 모르겠음

plt.axis([2012, 2015, 450, 510])
plt.ylabel("# of times I heard someone say 'data Science'")
plt.title("Look at this 'Hugh' Increase!")
plt.show()
