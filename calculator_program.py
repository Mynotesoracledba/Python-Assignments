

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function modulos two numbers
def modulo(x, y):
    return x % y

#define the integer to get final value
total_value=0

#Get the choices from user
print("Please the operation choices")
print("1. addition , 2.subract , 3.multiply , 4.division , 5.modulo")

#loop begins here
while True:
    choice = input("Enter choice(1/2/3/4): ")
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    if choice in ('1','2','3','4','5'):
        if choice == '1':
            total_value=add(a,b)
            print ("The sum of  addition value is = ",total_value )
        elif choice == '2':
            total_value=subtract(a,b)
            print("The sum of subtraction value is = ",total_value)
        elif choice == '3':
            total_value=multiply(a,b)
            print("The sum of multiplication value is = ",total_value)
        elif choice == '4':
            total_value=divide(a,b)
            print("The sum of division value is = ",total_value)
        else:
            total_value=modulo(a,b)
            print("The sum of division value is = ",total_value)
    #code continune/exit based on user choices
    if input('Do You Want To Continue? ') != 'y':
        break