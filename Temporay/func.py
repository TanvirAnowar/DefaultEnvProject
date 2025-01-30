

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

print(lambda_func(10,20))