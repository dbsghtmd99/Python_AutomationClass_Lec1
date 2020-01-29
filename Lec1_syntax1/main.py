# exercise
# 1-1
list_a = [171500, 172000, 174500, 170500, 174000]
print("min : {}".format(min(list_a)))
print("max : {}".format(max(list_a)))
print("========================================")

# 1-2
dict_a = {"12/02": 171500, "12/03": 172000, "12/04": 174500, "12/05": 170500, "12/06": 174000}

# 1-3
print("12/05 : {}".format(dict_a["12/05"]))
print("========================================")

# 2-1
score1 = [51, 32, 88, 86, 15]
score2 = [78, 64, 94, 42, 50]

# 2-2
sum = []
for i in range(0, 5):
    sum.append(score1[i] + score2[i])
print(sum)
print("========================================")

# 2-3
Letter = []
for i in sum:
    if i / 2 >= 90:
        val = 'A'
    elif i / 2 >= 80:
        val = 'B'
    elif i / 2 >= 70:
        val = 'C'
    elif i / 2 >= 60:
        val = 'D'
    else:
        val = 'F'
    Letter.append(val)

print(Letter)
print("========================================")

# 3-1
for i in range(2, 10):
    for j in range(1, 10):
        print(str(i) + "*" + str(j) + "=" + str(i * j))
print("========================================")

# 3-2

a = 2

while a < 10:
    b = 1
    while b < 10:
        print(str(a) + "*" + str(b) + "=" + str(a * b))
        b += 1
    a += 1
print("========================================")


# 4-1
def fact(n):
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        return n * fact(n - 1)


print(fact(5))
print("========================================")


# 4-2
def swap(inputList):
    inputList.sort(reverse=True)
    return inputList


inputList = [10, 20]
print(swap(inputList))
