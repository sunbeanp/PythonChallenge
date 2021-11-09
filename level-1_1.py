
new_ascii = []
new_word = []

a = list(input())                              
for i in range(0, len(a)):
    if a[i] in [' ', '.', '\'', '(', ')']:     
        new_ascii.append(ord(a[i]))
    elif 121 <= ord(a[i]) <= 122:              
        new_ascii.append(ord(a[i]) - 24)
    else:
        new_ascii.append(ord(a[i]) + 2)        
    new_word.append(chr(new_ascii[i]))

sentence = ''                   
for n in range(0, len(new_word)):
    sentence += new_word[n]
print(sentence)
