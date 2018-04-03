import random
print('Welcome to the General Knowledge Game')
print('What is your name?')
myName = input()
print('You stand a chance to win big, ' + myName)
age = random.randint(1,100)
print('How old are you?')
age = input()
age = int(age)

if age < 10:
    print('You are too young to play, ' + myName)

if age >= 10:
    print('You are old enough to play, ' + myName)


print('What year did Zimbabwe gain independence?')
zimYear = input()
zimYear = int(zimYear)

if zimYear < 1980:
    print('Wrong, ' + myName)
    
if zimYear > 1980:
    print('Wrong, ' + myName)
    
if zimYear == 1980:
    print('Correct, ' + myName)    

print('What year did Botswana gain independence?')
botYear = input()
botYear = int(botYear)

if botYear < 1966:
    print('Wrong, ' + myName)
    
if botYear > 1966:
    print('Wrong, ' + myName)
    
if botYear == 1966:
    print('Correct, ' + myName)

print('What year did South Africa get freedom?')
saYear = input()
saYear = int(saYear)

if saYear < 1994:
    print('Wrong, ' + myName)
    
if saYear > 1994:
    print('Wrong, ' + myName)
    
if saYear == 1994:
    print('Correct, ' + myName)

print('What year did Zambia gain independence?')
zamYear = input()
zamYear = int(zamYear)

if zamYear < 1964:
    print('Wrong, ' + myName)
    
if zamYear > 1964:
    print('Wrong, ' + myName)
    
if zamYear == 1964:
    print('Correct, ' + myName)


print('What year did Malawi gain independence?')
malYear = input()
malYear = int(malYear)

if malYear < 1964:
    print('Wrong, ' + myName)
    
if malYear > 1964:
    print('Wrong, ' + myName)
    
if malYear == 1964:
    print('Correct, ' + myName)

    
