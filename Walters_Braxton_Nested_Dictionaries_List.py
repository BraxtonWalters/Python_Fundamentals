# 1.) -------------------------------------------------------------------------------
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

"""
Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
Change the last_name of the first student from 'Jordan' to 'Bryant'
In the sports_directory, change 'Messi' to 'Andres'
Change the value 20 in z to 30
"""
x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["z"] = 30

# print(x)
# print(students)
# print(sports_directory["soccer"])
# print(z[0]["z"])

# 2). -------------------------------------------------------------------------------

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterate_dictionary(arr): 
    for i in arr:
        # the dum way
        # first_name = i["first_name"]
        # last_name = i["last_name"] 
        print(f"first name -- {i['first_name']}, last name -- {i['last_name']}")

iterate_dictionary(students)

# 3). -------------------------------------------------------------------------------

"""
Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
Michael
John
Mark
KB
And iterateDictionary2('last_name', students) should output:
Jordan
Rosales
Guillen
Tonel
"""

def iterate_dictionary2(key, arr):
    for i in arr:
        print(i[key])

# iterate_dictionary2("first_name", students)
# iterate_dictionary2("last_name", students)

# 4). -----------------------------------------------------------------------------

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
"""
Iterate Through a Dictionary with List Values
Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
"""
# output:
# 7 LOCATIONS   8 INSTRUCTORS
# San Jose         Michael
# Seattle          Amy
# Dallas           Eduardo
# Chicago          Josh
# Tulsa            Graham
# DC               Patrick
# Burbank          Minh
#                  Devon

def print_info(some_dict):
    # iter thro the dict 
    for i in some_dict:
        # storing the key in a var here
        val = some_dict[i]
        # testing
        # print(val)
        # counting the list and printing the statement
        print(f"{len(val)} {i}")
        # iter thro the list of the key we stored
        for item in val:
            # printing each string in the list
            print(item)
# That took way longer than it should have...

# print_info(dojo)