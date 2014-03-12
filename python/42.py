import string
from helpers import test, triangle_number, is_triangle_number

def word_to_value(word):
    value = 0

    for letter in word:
        value += string.lowercase.index(letter.lower()) + 1

    return value

def count_triangle_words(words):
    count = 0

    for word in words:
        value = word_to_value(word)

        if is_triangle_number(value):
            count += 1

    return count


test(triangle_number(1),1)
test(triangle_number(5),15)
test(triangle_number(10),55)
test(is_triangle_number(55),True)
test(is_triangle_number(56),False)
test(word_to_value('SKy'), 55)

with open('words.txt') as f:
    words = [w.strip('"') for w in f.read().split(',')]
    print count_triangle_words(words)
