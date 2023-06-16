#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    signs = [".", "?", ":"]
    char = 0

    while char < len(text):
        if text[char] in signs:
            print(text[char] + "\n")
            char += 1
            while text[char] == " ":
                char += 1
        else:
            print(text[char], end="")
            char += 1
