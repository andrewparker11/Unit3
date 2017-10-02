#Andrew Parker
#10/2/17
#warmup8.py - find the sum of all positive intergers less than 100,00 that are divisible by 3, 10 and 17

total = 0
for i in range(0,100000):
    if i%3==0 and i%10 == 0 and i%17 == 0:
      total = total + i  
print(total)