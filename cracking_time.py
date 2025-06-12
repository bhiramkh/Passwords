import string
import sys

def time_converter(timeToConvert, type_in="seconds", type_out="millennium"):
    #Accepts time in seconds by default
    #Converts time to a more readable format for humans
    time_dict={
        "seconds": 60,
        "minutes": 60,
        "hours": 24,
        "days": 30,
        "months": 12,
        "years": 10,
        "decade": 10,
        "century":10,
        "millennium": 1
    }
    final_time=" "
    position=-1
    start=False
    conversion=timeToConvert
    list_time=list(time_dict)
    in_list=True if type_in in list_time and type_out in list_time else False
    if not in_list:
        raise ValueError("Invalid input or output time unit!")
        sys.exit()
    if list_time.index(type_in)<list_time.index(type_out):
        for k, v in time_dict.items():
            position+=1
            if k==type_out or conversion<v:
                break
            else:
                if k==type_in and start==False:
                    start=True
                if start:
                    conversion/=v
    else:
        raise ValueError("Invalid input or output time unit!")
        sys.exit()
    type_time=list_time[position]
    final_time = f"{conversion:.2f} " + type_time
    return final_time
  

#Estimate password crack time
def crack_time():
    #Prompts the user for password to be analysed
    pass_analyse=input("Please enter the password for analysis!")
    len_pass=len(pass_analyse)
    if len_pass==0:
        #Check whether the password entered is valid
        print("Invalid password entered!")
        sys.exit()
    else:
        choice=""
        attack_speed=0
        #Attacks and speed (nb_attemps/second)
        attack={
            "Online (throttled)": 10,
            "Online (fast)": 1000,
            "Offline (basic hardware)": 1000000,
            "Offline (GPU cluster)": 1000000000,
            "Offline (nation state)": 1000000000000,
        }
        attack_shortcut={}
        print("Choose a type of attack from the following: ")
        for key in attack.keys():
            key_extract=key.replace("(", "").replace(")", "").split()
            key_word=key_extract[1][0].lower()
            attack_shortcut[key]=key_word
            print(f"- {key_extract[1]} -> {key_word}")
        #Prompts the user for the type of attack
        attack_choice=input("Your chosen attack type is: ").lower()
        for k,v in attack_shortcut.items():
            if attack_choice==v:
                choice=k
                attack_speed=attack[k]
        if attack_speed==0:
            print("Invalid attack entered!")
            sys.exit()
        #A password can contain any of the following types of characters
        size={
            "lowercase": string.ascii_lowercase,
            "uppercase": string.ascii_uppercase,
            "digits": string.digits,
            "symbols": string.punctuation
        }
        #Determine character set size
        charact_size=0
        for char in size.values():
            charact_size+=len(char) if any(p in char for p in pass_analyse) else 0
        #Determine the number of combinations
        #The higher nb_combi is the higher the cracking time
        nb_combi=charact_size**len_pass
        #Determine avergae attempts needed
        avg_attempt=nb_combi/2
        #Determine the cracking time
        estimate_time=avg_attempt/attack_speed
        #Display results
        print("-"*40)
        print("Password entered:", pass_analyse)
        print("Attack chosen:", choice)
        print("-"*40)
        print("Total number of combinations", nb_combi)
        print("Average number of attempts", avg_attempt)
        print("Estimated cracking time", time_converter(estimate_time))
      

print(time_converter(600, type_in="minutes", type_out="years"))
crack_time()
