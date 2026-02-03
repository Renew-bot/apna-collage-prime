# Student Enrolments

# Given a list of tuples with info(name, subject):

# · list all unique course

# · list students enrolled in English

# · create dictionary (student, set of courses)

info = [ 
    ("Alice" , "Math"),
    ("Bob" , "Science"),
    ("Alice" , "Science"),
    ("Charlie" , "Math"),
    ("Bob" , "Math"),
    ("Alice" , "English"),
    ("Charlie" , "English"),
]

#1
courses_set = set()
for tup in info:
    courses_set.add(tup[1])
print(courses_set)

#2
for tup in info:
    if(tup[1]=="English"):
        print(tup[0])

#3
dict = {}
for name , course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)