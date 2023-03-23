#Using alias and accessig variable
import custom_module_calculator_function as cme
total_value=0

#Get the choices from user
print("Please choose operation choices")
print("1. addition , 2.subract , 3.multiply , 4.division , 5.modulo")

#loop begins here and variable used here verify the requirement file
while True:
    choice = input("Enter choice(1/2/3/4): ")
    a=int(input("Enter the first number "))
    b=int(input("Enter the second number "))
    if choice in ('1','2','3','4','5'):
        if choice == '1':
            total_value=cme.add(a,b)
            print ("The sum of  addition value is = ",total_value )
        elif choice == '2':
            total_value=cme.subtract(a,b)
            print("The sum of subtraction value is = ",total_value)
        elif choice == '3':
            total_value=cme.multiply(a,b)
            print("The sum of multiplication value is = ",total_value)
        elif choice == '4':
            total_value=cme.divide(a,b)
            print("The sum of division value is = ",total_value)
        else:
            total_value=cme.modulo(a,b)
            print("The sum of division value is = ",total_value)
    #code continune/exit based on user choices
    if input('Do You Want To Continue? ') != 'y':
        break