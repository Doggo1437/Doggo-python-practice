monthly_income = 1000000
monthly_expenses = 1000001

if monthly_income > 10000:
    if monthly_income - monthly_expenses > 2500:
        print("NOW you are good to live anywhere")
    elif monthly_income - monthly_expenses < 0:
        print("You are on deficit")
    else:
        print("On what are you wasting your money?")
elif monthly_income > 1000:
    if monthly_expenses < 400:
        print("You'll be ok living in latam")
    else:
        print("You probably need a second job")
elif monthly_income > 500:
            print("You can live in venezuela")
else:
            print("You are poor")
            
            
            
