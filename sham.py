print("Welcome to Python Pizza world")
size = input("Which size pizza do you want? s, m, or l: ")
add_pepperoni = input("Do you want pepperoni? y or n: ")
extra_cheese = input("Do you want extra cheese? y or n: ")
bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
        
if extra_cheese == "y":
    bill += 1
    
print(f"The final bill is {bill}") 