# Variables and Constants

Pizza = 12
Delivery_Cost = 2.5
App_Discount = 0.25
Tuesday = 0.5


# Intialize charge variable 0
charge=0

print("\nBPP Pizza Price Calculator")
print("==========================")


# Input validation for the number of pizzas
while True:
    try:
        number_of_pizzas = int(input("How many pizzas do you need?: "))
        if number_of_pizzas<=0:
            raise ValueError("Please enter a positive integer!")
        break
    except ValueError:
        print("Please enter a valid positive integer!")
        
        
# Input validation for delivery option
while True:
    Delivery = input("Is delivery required? (Y/N): ").lower()
    if Delivery == 'y' or Delivery == 'n':
        break
    else:
        print('Please answer "Y" or "N".')
        
        
        

# Input validation for Tuesday discount
while True:
    Tuesday = input("Is it Tuesday? (Y/N): ").lower()
    if Tuesday == 'y' or Tuesday == 'n':
        break
    else:
        print('Please answer "Y" or "N".')
        
        
        

# Input validation for app discount
while True:
    App = input("Did the customer use the app? (Y/N): ").lower()
    if App == 'y' or App == 'n':
        break
    else:
        print('Please answer "Y" or "N".')



# Apply free delivery for three or more pizzas
if number_of_pizzas>=3 and Delivery == 'y':
    charge +=5
elif Delivery == 'y':
    charge +=Delivery_Cost


# Apply discount if it's Tuesday or the customer used the app
    if Tuesday == 'y' or App == 'y':
        charge -= charge * App_Discount
    

# Apply App Discount
if App == 'y':
    charge += (1-App_Discount)

total_price = Pizza * number_of_pizzas + charge
    

print(f"Total price :£{total_price:.2f}")








