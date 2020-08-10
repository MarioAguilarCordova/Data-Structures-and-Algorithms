# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a
# palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.


def load_dict_with_chars(dict, str):
    for char in str:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


def is_permutation_palindrome(dict, str):
    count = 0
    for key, value in dict.items():
        if len(str) % 2 == 0 and value != 2:
            print(False)
            break
        elif len(str) % 2 != 0 and value == 1:
            count += 1
        if len(str) % 2 != 0 and count > 1:
            print(False)
            break
    print(True)


def main():
    string = "hello"
    chars = {}
    load_dict_with_chars(chars, string)
    is_permutation_palindrome(chars, string)
    print(chars)


main()
