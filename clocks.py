from functions import is_prime
from functools import reduce
import matplotlib.pyplot as plt


def sum_func(func1, a, func2, b):
    if a >= b:
        return 0
    temp = a
    ans = 0
    while temp <= b:
        ans += func1(temp)
        temp = func2(temp)

    return ans


print(sum_func(lambda x: x, 1, lambda x: x + 1, 10))


def num_integrate(func, lower, upper, terms):
    h = (upper - lower) / terms

    def y(x):
        return func(lower + h * x)

    return h / 3 * (2 * sum(y(i) for i in range(2, terms, 2)) + 4 * sum(y(i) for i in range(1, terms, 2))
                    + y(0) + y(terms))


print(num_integrate(lambda x: x * x, 1, 4, 10))


def accumulate(combiner, term, a, next_term, b, filter_terms=None):
    if a >= b:
        return 0
    temp = a
    ans = 0
    if filter_terms:
        while temp <= b:
            if filter_terms(term(temp)):
                ans = term(temp)
                break
            else:
                temp = next_term(temp)
        while temp < b:
            temp = next_term(temp)
            if filter_terms(temp):
                ans = combiner(ans, term(temp))

        return ans

    else:
        ans = term(temp)

    while temp < b:
        temp = next_term(temp)
        ans = combiner(ans, term(temp))

    return ans


print(accumulate(lambda x, y: x + y, lambda x: x, 1, lambda x: x + 1, 10, is_prime))


def eval_polynom(x, coef):
    return reduce(lambda a, b: a * x + b, reversed(coef))


lst = [1, 3, 0, 5, 0, 1]
print(eval_polynom(2, lst))


def add_vectors(*args):
    # return list(map(sum, zip(args)))
    # return [sum(i[0]) for i in list(zip(args))]
    return list(zip(i for i in args))


# print(add_vectors([1, 2, 3], [0, 1, 0], [2, 2, 1]))


# print(list(zip([1, 2, 3], [0, 1, 0], [2, 2, 1])))
# print(list(zip(vecs)))
# print([i for i in list(zip(vecs))])
# print(list(zip(vecs)))


class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        return Vector(list(sum(i) for i in zip(self.values, other.values)))

    def __str__(self):
        return str(self.values)


def vec_sum(*args):
    return reduce(lambda x, y: x + y, args)


# print(Vector([1, 2, 3]) + Vector([0, 1, 0]))
vecs = [Vector([1, 2, 3]), Vector([0, 1, 0]), Vector([2, 2, 1])]
new_vec = vec_sum(Vector([1, 2, 3]), Vector([0, 1, 0]), Vector([2, 2, 1]))
print(new_vec)


def permutations(lst):
    if len(lst) < 2:
        return lst
    if len(lst) == 2:
        return [lst, [lst[1], lst[0]]]
    ans = list()
    for item in lst:
        temp = lst.copy()
        temp.remove(item)
        for p in permutations(temp):
            ans.append([item] + p)
    return ans


def factorial(n):
    return reduce(lambda x, y: x * y, (i for i in range(1, n + 1)))


probs = [i*0.05 for i in range(21)]
for p in probs:
    print(p, p + p**2 - p**3)

plt.plot(probs, [p + p**2 - p**3 for p in probs])
plt.plot(probs, probs)

plt.xlabel('clock probability')
plt.ylabel('total probability')
plt.title('Clocks')

plt.legend()
plt.show()
