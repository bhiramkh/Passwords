import string
import random

def length_password():
    length_pass=input("Please enter password length!")
    return length_pass

def password_generator():
    random_string=string.ascii_lowercase
    string_output=""
    pass_length=length_password()
    if not pass_length.isdigit():
        length_password()
    else:
        pass_length=int(pass_length)
    #Check whether an uppercase character is desirable
    uppercase=input("Enter Y if you wish your password to contain at least one uppercase letter!").strip().upper()
    #Check whether a digit is required
    digit=input("Enter Y if you wish your password to contain at least a digit!").strip().upper()
    #Check whether a symbol is required
    symbols=input("Enter symbols which you wish your password to contain!").strip().upper()
    characteristics={
        "uppercase": string.ascii_uppercase if uppercase=="Y" else "",
        "digits": string.digits if digit=="Y" else "",
        "symbols": symbols if symbols in string.punctuation else ""
    }

    for charact in characteristics.values():
        if not charact=="":
            random_string=random_string+charact
            string_output=string_output+"".join(random.choices(charact, k=1))
            pass_length-=1
            if pass_length==0:
                break
    string_output=string_output+"".join(random.choices(random_string, k=pass_length))
    #Reshuffle string to avoid predictable patterns
    pass_list=list(string_output)
    random.shuffle(pass_list)
    return " ".join(pass_list)

myNewPassword=password_generator()
print("The generated password is", myNewPassword,".")
