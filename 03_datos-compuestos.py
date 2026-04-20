list = ["diego doggo","Ziulog",True,1.85]
tuple = ("diego doggo","Ziulog",True,1.85)

list[0] = "Ziulog"
# tuple[0] = "Ziulog" is not possible because tuples cant be modified


# creating a set -> can be accessed by index & cannot store duplicate data
set= {"diego doggo","Ziulog",True,1.85,"Ziulog"}

# print(set{1}) -> won't access the element 


# creating a dictionary (dict)
dict = {
    'name':'diego doggo',
    'nickname':'ziulog',
    'is_hungry':True,
    'height':1.85,
    'duplicate_data':'Ziulog'
    }
print(dict['duplicate_data'])