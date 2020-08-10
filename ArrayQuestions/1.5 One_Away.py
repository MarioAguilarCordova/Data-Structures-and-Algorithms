# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away


def one_away(string, word):
    count = 0

    for i in range(len(word)):
        if word[i] == string[i]:
            count += 1

    print(True if count >= len(string) - 1 else False)


one_away("pale", "pie")
one_away("pales", "pale")
one_away("pale", "bale")
one_away("pale", "bake")
