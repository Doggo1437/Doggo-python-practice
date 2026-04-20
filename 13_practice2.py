
## num_check = (input("Is it even or is it odd: "))

## if (type(num_check) == type(0)) and (num_check % 2 == 0)
# print("ITS EVEN")
## elif (type(num_check) == type(0)) and (num_check % 2 > 0):
##   print("its odd")
## elif (type(num_check) == type("")) and (len(num_check) % 2 == 0):
##     print("not a number, but ITS EVEN")
## elif (type(num_check) == type("")) and (len(num_check) % 2 > 0):
##     print("not a number, but its odd")
## else:
##     print("Not a valid input")
    

while True:
    num_check1 = input("enter something: ")
try:
    num_check1 = int(num_check1) 
    if num_check1 % 2 == 0:
                print("ITS EVEN")
    else:
                print("its odd")
except ValueError:
        print("thats not a number..")
        if len(num_check1) % 2 == 0:
            print(" but ITS EVEN")
        else:
            print(" but its odd")
if num_check1.lower() == "exit":
        print("Goodbye!")
        break    
    

    
        