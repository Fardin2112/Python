first_num = input("Enter Number :")
operator = input("Enter operator(+,-,*,%,/) :")
second_num = input("Enter Second Number :")

first_num = int(first_num)
second_num = int(second_num)

if operator == "+" :
    print(first_num + second_num)
elif operator == "-" :
    print(first_num - second_num)
elif operator == "*" :
    print(first_num * second_num)        
elif operator == "/" :
    print(first_num / second_num)
elif operator == "%" :
    print(first_num % second_num)
else :
    print("enter valid operator please.")
