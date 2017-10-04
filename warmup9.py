#Andrew Parker
#10/4/17
#warmup9.py - asks for a word, Prints it with capitalized vowels

word = input('Give a word: ')
for ch in word:
    if ch is 'a' or ch is 'e' or ch is 'i' or ch is 'o' or ch is 'u':
        print(ch.upper())
    else:
        print(ch)
