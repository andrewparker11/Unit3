#Andrew Parker
#10/4/17
#betterAdditionGameDemo.py - asks addition problems until the user gets 5

from random import randint

numCorrect = 0
while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    question - 'What is ' + str(num1) + '+' + str(num2) + '?'
    int(input(question))
    answer = int(input(question))
    