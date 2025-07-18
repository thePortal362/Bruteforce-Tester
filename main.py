import time
import random
import os

#Definition of Variables
FourDigitLst = ["6279", "0152", "7530", "8624", "1972", "4389", "9825", "5647", "0789", "1234"]

#Definition of functions

#Main Loop

while True:
    os.system('clear')
    print("""\033[35m
  ___          _        __                  _____       _           
 | _ )_ _ _  _| |_ ___ / _|___ _ _ __ ___  |_   _|__ __| |_ ___ _ _ 
 | _ \ '_| || |  _/ -_)  _/ _ \ '_/ _/ -_)   | |/ -_|_-<  _/ -_) '_|
 |___/_|  \_,_|\__\___|_| \___/_| \__\___|   |_|\___/__/\__\___|_|  \033[0m""")
    print("")
    print(" \033[34mBy yawnetx\033[0m")
    print("")
    print(" 1. 4 Digit Phone Pin")
    print(" 2. 8 Digit Website Login")
    print("")
    mode_select = input(" >")
    time.sleep(0.5)

    if mode_select == "1":
        test_pin = random.choice(FourDigitLst)
        os.system('clear')
        while True:
            print("\033[34m What's the Pin?\033[0m")
            #print(test_pin)
            inp_pass = input(" >")
            if inp_pass == test_pin:
                os.system('clear')
                while True:
                    os.system('clear')
                    print("\033[32m Access Granted!\033[0m")
                    print(" The code was", test_pin)
                    print(" Press \033[31me\033[0m to exit")
                    if input(" >") == "e":
                        break
                    time.sleep(0.5)
                break
            else:
                print("\033[31m Code was wrong\033[0m")
                print("")
    elif mode_select == "2":
        os.system('clear')
        print(" Coming soon")
        time.sleep(1)
        os.system('clear')

    elif mode_select == "quit":
        os.system('clear')
        break
