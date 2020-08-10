# 1.1 Is Unique: Implement an algorithm to determine if a string has
# all unique characters. What if you cannot use additional data structures?


def is_unique(string):
    unique = True
    answer = {}
    for char in string:
        if char in answer:
            answer[char] += 1
        else:
            answer[char] = 1

    print(answer)

    for key, value in answer.items():
        if key != ' ' and value > 1:
            unique = False
            print(unique)
            break

    if unique:
        print(unique)


is_unique("hello")
is_unique("whats up")
is_unique("wow i cannot believe it is not butter!")
