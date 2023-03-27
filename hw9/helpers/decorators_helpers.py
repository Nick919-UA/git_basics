
def is_email_valid(func):
    def wrapper(email, y, a, z, b, c):
        if "@" in email:
            if "." in email.split("@")[1]:
                func(email, y, a, z, b, c)
            else:
                print("Email invalid without dot!!!!")
        else:
            print("Email invalid without @ !!!!")
    return wrapper

def is_phone_valid(func):
    def wrapper(e, y, a, phone, b, c):
        numbers = str(phone)
        print(e, y, a, phone, b, c)
        print (numbers, len(numbers))
        if numbers.startswith('+') and len(numbers) == 13:
            func(e, y, a, phone, b, c)
        else:
            print("Telephone is invalid! Must start with + and contains 13 numbers!")
    return wrapper