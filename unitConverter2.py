#Andrew Parker
#10/2/17
#unitConverter.py - converts stuff except now improved 

print(' 1)Kilometers to Miles ')
print(' 2)Kilograms to Pounds ')
print(' 3)Liters to Gallons ')
print(' 4)Celsius to Fahrenheit ')
print(' 5)quit ')
print(' Choose a number: ')

uc = int(input('Enter an interger: '))
if uc == 1:
    kilm = int(input('How many kilometers? '))
    print((kilm*0.621371), 'miles')
elif uc == 2:
    kilg = int(input('How many kilograms? '))
    print((kilg*2.20462), 'pounds')
elif uc == 3:
    lit = int(input('How many liters? '))
    print((lit*0.264172), 'gallons')
elif uc == 4:
    deg = int(input('How many degrees in Celsius? '))
    print((deg*9/5)+32, 'degrees fahrenheit')
elif uc == 5:
    break
elif uc == 1,2,3,4,5:
   