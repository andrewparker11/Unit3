#Andrew Parker
#10/4/17
#warmup9.py - asks for a word, Prints it with capitalized vowels

from random import randint

numCorrect = 0
while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    question = 'What is ' + str(num1) + ' + ' + str(num2) + '?'
    answer = int(input(question))
    if num1 + num2 == answer:
        print('Correct!')
        numCorrect += 1
    else:
        print('The answer was', num1+num2)
        
print('Congradulations! You Win! ')
