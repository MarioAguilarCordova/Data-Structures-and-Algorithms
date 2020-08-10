'''def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break

        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
'''

stock_prices = {}

file = open("nyc_weather.csv", encoding="utf8")
with file as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

print(stock_prices)
# 1a. What was the average temperate in first week of Jan

result = 0
i = 0
for key, value in stock_prices.items():
    i += 1
    result += value
    if i == 7:
        print(result/i)

# 1b. What was the maximum temperature in the first 10 days of Jan

maximum = 0
for key, value in stock_prices.items():
    maximum = max(maximum, value)

print(maximum)

# 2a. What was the temperature on Jan 9?

print(stock_prices['09-Jan'])

# 2b. What was the temperature on Jan 4?

print(stock_prices['04-Jan'])

# 3a. poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file
# in python and print every word and its count as show below. Think about the best data structure
# that you can use to solve this problem and figure out why you selected that specific data structure.

text_file = {}

comma = ","
exclamation = "!"
period = "."
semi = ";"
colon = ":"
empty = ""

word_count = {}
with open("poem.txt", "r") as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token.lower()
            token.replace(comma, empty)
            token.replace(exclamation, empty)
            token.replace(colon, empty)
            token.replace(semi, empty)
            token.replace(period, empty)
            token = token.replace('\n', '')
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1

print(word_count)

