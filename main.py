import os
from time import sleep

password1 = input('Please enter your password : ')
verify = 0
kicker = 0


def clear():
    _ = os.system('cls')


while verify == 0:
    # password to be taken from school database
    password2 = input("Password from database : ")
    if password1 == password2:
        # name to be taken from school database
        name = input("Please enter your name: ")
        print("Welcome " + name + ", you have been registered")
        verify = 1
        level = len(password1)
        if level == 8:
            user = "S"
        elif level == 12:
            user = "T"
        elif level == 16:
            user = "A"
    else:
        print("The passwords do not match. Please try again.")
        kicker = kicker + 1
        if kicker == 3:
            print("You have failed too many times. ")
            quit()
loop = 0
while loop == 0:
    if user == "S":
        function = int(input("What would you like to do? 1) Check Internet Access  2) Go outside 3) Look at timetable  "
                             "4) Get menu for today 5) Exit "))
        if function == 1:
            print("Checking internet access level")
            print("Student Internet Access")
            sleep(10)
            clear()
        elif function == 2:
            print("Start pollution sensors")
            pollution = int(input("Please input outside pollution level ppm: "))
            if 0 <= pollution <= 350:
                print("The outside has a pollution level of " + str(pollution) + " ppm. It is very safe to go out. ")
                sleep(20)
                clear()
            elif 350 <= pollution <= 1000:
                print("The outside has a pollution level of " + str(pollution) + " ppm. It is safe to go out. ")
                sleep(20)
                clear()
            elif 1000 <= pollution <= 2000:
                print(
                    "The outside has a pollution level of " + str(pollution) + "ppm. It is advised to not stay out for "
                                                                               "too long. ")
                sleep(20)
                clear()
            elif 2000 <= pollution <= 5000:
                print("The outside has a pollution level of " + str(pollution) + " ppm. It is advised to take a mask. ")
                sleep(20)
                clear()
            elif 5000 <= pollution <= 40000:
                print("The outside has a pollution level of " + str(pollution) + " ppm. It is advised not to go out. ")
                sleep(20)
                clear()
            elif 40000 < pollution:
                print("The outside has a pollution level of " + str(pollution) + " ppm. Please do not go out. ")
                sleep(20)
                clear()
            else:
                print("This is not a valid level.")
                sleep(10)
                clear()
        elif function == 3:
            # take timetable for database
            o = ["Period 1", "Period 3"]
            print("Timetable for today is")
            print(o)
            sleep(10)
            clear()
        elif function == 4:
            food = 100000
            sleep(100)
            clear()
        elif function == 5:
            quit()
        else:
            print("That is not valid input")
            sleep(10)
            clear()

    elif user == "T":
        function = int(input("What would you like to do? 1) Check Internet Access  2) Go outside 3) Look at timetable  "
                             "4) Get menu for today 5) Exit "))
        if function == 1:
            print("Checking internet access level")
            print("Teacher Internet Access")
            sleep(10)
            clear()
        elif function == 2:
            print("Start pollution sensors")
            pollution = int(input("Please input outside pollution level ppm: "))
            if 0 <= pollution <= 350:
                print("The outside has a pollution level of " + str(pollution) + " ppm. It is very safe to go out. ")
                sleep(20)
                clear()
            elif 350 <= pollution <= 1000:
                print("The outside has a pollution level of " + str(pollution) + " ppm. It is safe to go out. ")
                sleep(20)
                clear()
            elif 1000 <= pollution <= 2000:
                print(
                    "The outside has a pollution level of " + str(pollution) + "ppm. It is advised to not stay out for "
                                                                               "too long. ")
                sleep(20)
                clear()
            elif 2000 <= pollution <= 5000:
                print("The outside has a pollution level of " + str(pollution) + " ppm. It is advised to take a mask. ")
                sleep(20)
                clear()
            elif 5000 <= pollution <= 40000:
                print("The outside has a pollution level of " + str(pollution) + " ppm. It is advised not to go out. ")
                sleep(20)
                clear()
            elif 40000 < pollution:
                print("The outside has a pollution level of " + str(pollution) + " ppm. Please do not go out. ")
                sleep(20)
                clear()
            else:
                print("This is not a valid level.")
                sleep(10)
                clear()
        elif function == 3:
            # take timetable for database
            o = ["Period 1", "Period 3"]
            print("Timetable for today is")
            print(o)
            sleep(10)
            clear()
        elif function == 4:
            food = 10000
            print(food)
            sleep(100)
            clear()
        elif function == 5:
            quit()
        else:
            print("That is not valid input")
            sleep(10)
            clear()
    elif user == "A":
        function = int(input("What would you like to do? 1) Check Internet Access  2) Go outside 3) Look at timetable  "
                             "4) Get menu for today 5) Find a student 6) Exit "))
        if function == 1:
            print("Checking internet access level")
            print("Student Internet Access")
            sleep(10)
            clear()
        elif function == 2:
            print("Start pollution sensors")
            pollution = int(input("Please input outside pollution level ppm: "))
            if 0 <= pollution <= 350:
                print("The outside has a pollution level of " + str(pollution) + " ppm. It is very safe to go out. ")
                sleep(20)
                clear()
            elif 350 <= pollution <= 1000:
                print("The outside has a pollution level of " + str(pollution) + " ppm. It is safe to go out. ")
                sleep(20)
                clear()
            elif 1000 <= pollution <= 2000:
                print(
                    "The outside has a pollution level of " + str(pollution) + "ppm. It is advised to not stay out for "
                                                                               "too long. ")
                sleep(20)
                clear()
            elif 2000 <= pollution <= 5000:
                print("The outside has a pollution level of " + str(pollution) + " ppm. It is advised to take a mask. ")
                sleep(20)
                clear()
            elif 5000 <= pollution <= 40000:
                print("The outside has a pollution level of " + str(pollution) + " ppm. It is advised not to go out. ")
                sleep(20)
                clear()
            elif 40000 < pollution:
                print("The outside has a pollution level of " + str(pollution) + " ppm. Please do not go out. ")
                sleep(20)
                clear()
            else:
                print("This is not a valid level.")
                sleep(10)
                clear()
        elif function == 3:
            # take timetable for database
            o = ["Period 1", "Period 3"]
            print("Timetable for today is")
            print(o)
            sleep(10)
            clear()
        elif function == 4:
            food = 1000
            sleep(100)
            clear()
        elif function == 5:
            student = int(input("Student No. s"))
            # Taken from sensor
            ctrans = input("The location where the RFid is transmitting data from : ")
            print("Student "+str(student)+" is in room " + ctrans)
        elif function == 6:
            quit()
        else:
            print("That is not valid input")
            sleep(10)
            clear()
