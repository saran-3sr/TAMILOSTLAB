class NotEligibleToVoteException(Exception):
    pass

age = int(input("Enter your age: "))

if age < 18:
    raise NotEligibleToVoteException("You must be at least 18 years old to vote.")
else:
    print("You are eligible to vote.")
