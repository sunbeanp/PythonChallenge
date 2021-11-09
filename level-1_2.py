
import string

a = input()
before = "abcdefghijklmnopqrstuvwxyz"
after = "cdefghijklmnopqrstuvwxyzab"

sentence = a.maketrans(before, after)
print(a.translate(sentence))
