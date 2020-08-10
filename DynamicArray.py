'''hi = [1, 2, 3, 4]
hi.reverse()
print(hi)

arr = [1, 2, 3, 4]


def reverse(arr):
    new_arr = []
    for i in range (len(arr), 0):
        new_arr.insert(arr[i])


reverse(arr)'''

# 1. Let us look at the expense list below

expenses = {"January": 2200, "February": 2350, "March": 2600, "April": 2130,
            "May": 2190}

# 1a. In Feb, How many dollars did you spent extra compared to January?

if expenses["January"] > expenses["February"]:
    extra = expenses["January"] - expenses["February"]
else:
    extra = expenses["February"] - expenses["January"]
print(extra)

# 1b. Find out your total expenses in the first quarter (first three months) of the year
sum = 0
i = 0
for key, value in expenses.items():
    if i < 3:
        sum += value

    i += 1

print(sum)

# 1c. Find out if you spent exactly 2000 dollars that month

for key, value in expenses.items():
    if value == 2000:
        print(True)
    else:
        print(False)

# 1d. The month of june has finished and your monthly expense report is 1980

expenses["June"] = 1980
print(expenses)

# 1e. You returned an item that you bought in the month of April and
#    got a refund of 200$. Make a correction to your monthly expense list

correction = expenses["April"]
correction -= 200
expenses["April"] = correction
print(expenses)

# 2. You have a list of your favourite marvel super heroes.

heroes = ['spider-man', 'thor', 'hulk', 'iron man', 'captain america']

# 2a. Length of the list

print(len(heroes))

# 2b. Add 'black panther' at the end of this list
heroes.append('black panther')
print(heroes)
# 2c. You realize you need to add black panther after hulk
heroes.insert(3, 'black panther')
print(heroes)
# 2d. remove thor and hulk, add doctor strange
del heroes[1:3]
print(heroes)
# 2e. sort heroes in alphabetical order

heroes.sort()
print(heroes)

# 3. Make a list of all odd numbers

n = int(input("Give a Number"))
oddnums = []


def odd(n):
    for i in range(n):
        if i % 2 != 0:
            oddnums.append(i)


odd(n)
print(oddnums)
