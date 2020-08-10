# 1.2 Check Permutation: Given two strings, write a
# method to decide if one is a permutation of the other.


def load_dict_with_chars(dict, str):
    for char in str:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


def load_list_with_chars(list, str):
    for char in str:
        list.append(char)


def is_permuation(str1, str2):

    list1 = []
    list2 = []
    load_list_with_chars(list1, str1)
    load_list_with_chars(list2, str2)

    list1.sort()
    list2.sort()

    if len(list1) != len(list2):
        print(False)

    print(True)


is_permuation("hello", "olleh")
