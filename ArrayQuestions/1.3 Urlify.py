# 1.3 Write a method to replace all spaces in a string with '%20'. You may assume that
# the string has sufficient space at the end to hold the additional characters, and that
# you are given the "true" length of the string.


def urlify(str):
    new_str = ""
    for i in range(len(str)):
        if str[i] == " ":
            new_str += "%20"
        else:
            new_str += str[i]
    print(new_str)


urlify("Mr wutface mgee")