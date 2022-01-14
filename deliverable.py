# ALL README MATERIAL GETS TESTED HERE
#1
idx = 'abcde'.index('d')
idx = idx + 11
print(idx)
idx = idx * 2
print('second print', idx)

#2
num = 33
is_even = num % 2 == 0 
print(is_even)
print(not is_even)

#3
str1 = 'marker'
num = len('whiteboard') - len(str1)
print(num)
str2 = 'bootcamp'
print(str2[num].upper())
char = str2[num].lower()
print(char + '!')

#4 
sentence = 'welcome to bootcamp prep'
last_char = sentence[len(sentence) - 1]
print('LAST', last_char)
print(sentence.index(last_char))

#5 
age = 30 
if age == 30:
    print('Older than 30')
else:
    print('younger than 30')

#6
str = 'pizza'
if len(str) > 10:
    print('long string')
else: 
    print('short string')
if str[0] == 'p':
    print('starts with p')

#7
num = 15 
if num % 3 == 0:
    print('divisible by 3')
elif num % 5 == 0:
    print('divisible by 5') 

#8
num = 50
if num % 3 == 0:
    print('divisible by 3')
if num % 5 == 0:
    print('divisible by 5')

#9
str = 'General Assembly'
if str[0] == str[0].upper():
    print('Starts with a capital')
if str[len(str)-1] == str[len(str)-1].upper():
    print('Ends with a capital!')

#10
num = -44
if num > 0:
    print('positive')
elif num < 0:
    print('negative')
else:
    print(0) 
if num % 2 == 0:
    print('even')
else:
    print('odd')



#=======Conditional=======
num = 11
if num > 5:
    print('if')

num = 5 
if num > 5:
    print('if')
else:
    print('else')


#======Functions====

def check_number (num):
    if num > 0:
        return 'positive'
    elif num < 0:
        return 'negative'
    else:
        return 'zero'