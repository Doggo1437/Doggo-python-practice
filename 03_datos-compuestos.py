from httpx import get


list = ["diego doggo","Ziulog",True,1.85]
tuple = ("diego doggo","Ziulog",True,1.85)

list[0] = "Ziulog"
# tuple[0] = "Ziulog" is not possible because tuples cant be modified


# creating a set -> can be accessed by index & cannot store duplicate data
set= {"diego doggo","Ziulog",True,1.85,"Ziulog"}

# print(set{1}) this will not access the data


# creating a dictionary (dict)
people = {
   'diego doggo': {
       'nickname': 'ziulog',
       'is_hungry': True,
       'height': 1.85,
       'duplicate_data': 'Ziulog'
   },
   'Daniel Ozil': {
       'nickname': 'Leekun',
       'is_hungry': False,
       'height': 1.80
   },
   'Issack Saya': {
       'nickname': 'Dupin',
       'height': 1.80,
       'duplicate_data': 'isaack'
   }}

# this is a dictionary with nested dictionaries, we can access the data by using the keys
# print(people['diego doggo']['nickname'])
# print(people['Issack Saya']['is_hungry']) # this will return an error because the key is not present in the dictionary

# get() # this is a method that can be used to access the data in the dictionary, 
       # it will return None if the key is not present in the dictionary
print(people.get('Issack Saya').get('is_hungry')) # this will return None because the key is not present in the dictionary