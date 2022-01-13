# this is a comment
# TODO bulid this function
def add (num, num2):
    '''
    this is a multi-line comment
    '''


#===============CONDITIONALS=====================
name = 'Dev'
#print(name)

nothing = None  #falsey 
#print(nothing)

is_working = True
car_off = False


if nothing: # HAVE TO INDENT AFTER COLON (:)
    print('This is true') #this gets printed
    num = 7
    print('car is off')
elif car_off:  #else if 
    print('this is the second condition')
    print('this will run if car_off is True')
elif is_working:
    print('This is working')    
else:
    print('This is not true')

#this is another conditional
if is_working:
    print('This is working also')        

#conditionals -> finds first item that is represents true
# it runs thats indented [block or code]

print(15 / 6)
print(15 // 6) #removes remainer (.)

#==================STRING METHODS===============

print("ace of spades".split(" "))
# -> ["ace", "of", "spades"]

print("ace-of-spades".split("-"))
# -> ["ace", "of", "spades"]

print("ace.of.spades".split("."))
# -> ["ace", "of", "spades"]

my_scare = 'boo'
print(my_scare.upper())
# -> "BOO"

print("then I went to the store I like".replace("I", "you"))
# -> 'then you went to the store you like'

food = 'eggs'
print ("eggs" in "green eggs and ham")
#returns True

print(len(food)) # -> 4


#================RANGES===============
"my code rulez"

print("my code rulez"[-1])
# -> 'z'

print("my code rulez"[3:7]) #index 3='c' to 7='e'
# -> 'code'

print("my code rulez"[:2]) #starts index 0 ends at number after (:)
# -> 'my'

#===============LOGICAL OPERATORS================

if 7 == 7: # if  
    print('this is 7')
else:
    print('This is the second condition')

if 7 != 7: # if not 
    print('These are equal, duhh')
else:
    print('This is the second condition') 

if not 7:
    print('This is 7')
else:
    print('this is the second condition')



#=================LISTS - arrays in JS===============
arr = [1, 'two', 3, 'four', True, False, 'hello']
print(arr[1]) 
print(arr[-1]) #starts at the last index

one_through_ten = list(range(10)) #makes a list with 10 indexes starting at 0
print(one_through_ten)

three_through_ten = list(range(3, 10))
print(three_through_ten)


a = [1, 23, 12, 99, 82]
a.sort()
print(a)

a.append(88)
print('After adding 88', a)

a.insert(1, 77)
print('After inserting 77 at index 1', a)

a.pop()
print('popping....', a)

if 23 in a :
    print('This is Michael Jordan number!')
else:
    print('Not in there....')

# HELP!!!!!!!
# help(a) # -> shows all methods on variable
# help(str) -> shows all methods on string
# help(list) -> shows all methods on list
# help(dict) -> shows all methods on Dictionary (objects in JS)
# help(int) # -> shows all methods on integar


#===============DICTIONARY================

cat = {
  "name": 'Hamlet',
  "breed": 'American Shorthair',
  "fav_food": 'Prosciutto'
}

cat["name"]
# -> 'Hamlet'

# print('Do not feed to cat...', cat["fav_food"])
# -> 'Prosciutto'

# print('this is my cats breed...', cat.get("breed"))
# -> 'American Shorthair'

# cat['age'] = 3 #adds key value pair to CAT dict.
# print(cat['age'])
# print('ITEMS', cat.items()) #pairs key/value together then seprates
# print('KEYS', cat.keys())


#==============STRING INTERPOLATION================

# state = "Washington State"
# year = 1889
# n = 42
# my_message = f"{state} was the {n}th state to join the union in {year}."
# print(my_message)

def st_nd_rd_th(n):
  # add one to 13 because range is exclusive at the end.
  if n in range(11, 13 + 1):
    return "th"
  if n % 10 == 1:
    return "st"
  elif n % 10 == 2:
    return "nd"
  elif n % 10 == 3:
    return "rd"
  else:
    return "th"

state = "Washington State"
year = 1889
n = 42
my_message = f"{state} was the {n}{st_nd_rd_th(n)} state to join the union in {year}."
print(my_message)

#2
location = 'California'
number = 6
my_second_message = f'{location} is the {number}th largest economy in the world.'

#3
topic = 'Inflation'
num = 7 
y = 1982
my_third_message = ' {} is at {} percent. Highest since {}'.format(topic, num, y)
print(my_third_message)

#4
name = 'Devyn'
date = 'Oct 25, 2021'
company = 'GA'

my_fourth_message = f' {name} has become a way better engineer since {date} from attending {company} '
print(my_fourth_message)

#5 
event = 'NFL playoffs'
day = 'saturday'
time = '1:00 pm'

my_fifth_message = "I am excited for the {} to start this {} at {}".format(event, day, time)
print(my_fifth_message)







#============LOOPS===========
# n = 0
# while n < 1000:
#   n += 1
#   if n % 2 == 0:
#       print(f'{n} is even...')

# WHILE LOOP
n = True
num = 1
while n: #if n goes to false loops stop
    if num % 2 == 0: #check to see if number is even 
        print(f'{num} is even...')
      
        if num == 750: #check to see if num is 750
            n = False #once at 750 set booklean to false(stops loops)
            print('End program')
    num += 1 #adding one to num 
    print(num)

# FOR LOOP
for i in range(1, 751):
    if i % 2 == 0:
        print(f"{i} is even...", '*****')

        if i == 750:
            print('End program..')



nums = [1,2,3,55,66,44,33,22,11,33,750,44,66,33,33,22]
for i in range(len(nums)):
    element = nums[i]
    if element % 2 == 0: #check to see if number is even 
        print(f'{element} is even...', 'NUMS')
      
        if element == 750: #check to see if num is 750
            n = False #once at 750 set booklean to false(stops loops)
            print('Hi I am 750')



students = [
    {
        "name": "Kimmie",
        "city": "Atlanta"
    },
    {
        "name": "Chris",
        "city": "Salt Lake City"
    },
    {
        "name": "Zack",
        "city": "Los Angeles"
    },

]


for i in range(len(students)):
    student = students[i]
    print(student.get("name"))

    if student.get("city") == 'Los Angeles':
        print(f'{student.get("name")} wins an iPad for {student.get("city")}', 1)
        print(f"{student.get('name')} wins an iPad for {student.get('city')}", 2)

for i in range(len(students)):
    student = students[i]
    print(student.get("city"))

# Iterating through list of students
for student in students:
    print(student)

# Iterating through dict
for key in students[0]: # key to key
    print(key) # string of the key
    print('value', students[0].get(key))

# Iterating through dict PART 2
for key in students[1]: # key to key
    print(key, 'PART 2') # string of the key
    print('value', students[1][key])

# Iterating through dict PART 3
for anything in students[2]: # key to key
    print(anything, 'PART 3') # string of the key
    print('value', students[2][anything])

# Iterating through dict PART 4
for key, value in students[0].items(): # key to key
    print(key, '->', value)


#=================FUNCTIONS===========
def say_hello(friend="Tim"): #if we dont we a not a parameter 'Tim' gets filled 
  print("Hello, {}!".format(friend))

say_hello()
say_hello('Tom')


def move(name, city="Seattle", state="Washington"): #has to at least fill in name when running function 
  msg = "{} is moving to {}, {}"
  msg = msg.format(name, city, state)
  print(msg)


move("Charlie", "Los Angeles", "California")
move(city="San Francisco", name="Mark", state="California")
move("John", state="New York", city="New York") #name is first..


def first_function(language, person="Devyn"):
    message = "{} is making his first {} function"
    message = message.format(person,language)
    print (message)

first_function("python")

def get_cities(students):
    '''Return a [list] of all cities from the students [list] '''
    # TODO Make a empty list
    # TODO Iterate through the list of student
    # TODO Append each city in the dict to empty list
    # TODO return the lisy

    result = []

    for s in students:
        print(s)
        if s.get("city"):
            print(s.get("city"))
            result.append(s.get('city'))

    return result

print('Cities List:' ,get_cities(students))


def get_names(studnets):
    name_results = []

    for s in students:
        print(s)
        if s.get("name"):
            #print(s.get("name"))
            name_results.append(s.get("name"))
    return name_results

print('Name List:', get_names(students))