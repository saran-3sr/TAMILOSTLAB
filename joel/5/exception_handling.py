class NotEligibleException(Exception):
    pass

try:
    age=int(input("Enter your Age "))
    if age<18:
        raise NotEligibleException
    else:
        print("You can Vote")

except NotEligibleException:
    print("Not eligible")
except:
    print("Invalid Input")