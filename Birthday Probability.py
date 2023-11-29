from math import prod
import matplotlib.pyplot as plt


def probability(n):
    return 1 - prod((365-i)/365 for i in range(2, n))


x = [i for i in range(2, 366)]

y = [probability(i) for i in x]

plt.plot(x, y)

plt.xlabel('people')
plt.ylabel('probability')
plt.title('Birthday')

plt.show()
