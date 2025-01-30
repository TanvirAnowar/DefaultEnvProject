

def argument_func(*positional, **keywords):
    
    print("Positional:")        
    for pos in positional:
        print(f"positional: {pos}")
    
    print("Keywords:")    
    for key,value in keywords.items():
        print(f"keywords: {key} : {value}")
        
# argument_func(1,2,3,4,5,6,7,8,9,10, name="John", age=25, city="New York")


def password_strength_func(password):
    
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter"
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter"
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit"
    if not any(char in "!@#$%^&*()" for char in password):
        return "Password must contain at least one special character"
    if not all(char.isalnum() or char in "!@#$%^&*()" for char in password):
        return "Password must contain only alphanumeric and special characters"
    if not all(char.isprintable() for char in password):
        return "Password must contain only printable characters"   
    if not all(char.isascii() for char in password):
        return "Password must contain only ASCII characters"
 
    return "Password is strong"

# print(password_strength_func("Tanvirs@123"))

lambda_func = lambda a,b: a+b

# print(lambda_func(10,20))

# ? MAP FUNCTION

def square(a,b):
    return a*b

list_a = [1,2,3,4,5,6,7,8,9,10]
list_b = [11,12,13,14,15,16,17,18,19,20]

list_square = map(square,list_a,list_b)
# print(list(list_square))

new_list = map(lambda a,b:a*b,list_a,list_b)
# print(list(new_list))


# ? filter function

def even(a):
    return a%2==0

filtered_list = filter(even, list_a)
# print(list_a, list(filtered_list))

filtered_list = filter(lambda num: num>3 and num<8, list_a)
print(list_a, list(filtered_list))

