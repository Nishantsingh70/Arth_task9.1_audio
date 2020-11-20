import os
import speech_recognition as sr

while True:  

    print("\n")
    os.system("tput setaf 1")
    print("\t\t\t\t\t\t\tWELCOME TO LINUX MENU")
    print("\t\t\t\t\t\t\t---------------------")
    os.system("tput setaf 7")
    print("""
                                                    Press 1. To see date
                                                    Press 2. To see calender
                                                    Press 3. To run calculator
                                                    Press 4. Create User
                                                    Press 5. Create Directory
                                                    Press 6. See the RAM Usage
                                                    Press 7. See the CPU Information
                                                    Press 8. Check the IP address
                                                    Press 9. Create file
                                                    Press 10. To scan ip using nmap
                                                    Press 11. To go out from linux operations
    """)
    r = sr.Recognizer()
    with sr.Microphone() as source:
    print("Start Speaking")
    audio = r.listen(source)
    print("Speaking Done")

    ch = r.recognize_google(audio)
    if ((("run" in ch) or ("execute" in ch)) or ("see" in ch) and (("date" in ch) or ("date command" in ch))):
        os.system("date")
        print()

    elif ((("run" in ch) or ("execute" in ch)) or ("see" in ch) and (("cal" in ch) or ("calender" in ch))):
        os.system("cal")
        print()

    elif ((("run" in ch) or ("execute" in ch)) or ("see" in ch) and (("bc" in ch) or ("binary calculator" in ch))):
        os.system("bc")
        print()

    elif ((("create" in ch) or ("add" in ch)) and (("user" in ch) or ("new user" in ch))):
        print("Enter user name :",end ='')
        u_name = input()
        os.system("useradd {}".format(create_user))
        print()

    elif ((("create" in ch) or ("make" in ch)) and (("folder" in ch) or ("directory" in ch))):
        print("Enter directory name :",end ='')
        d_name = input()
        os.system("mkdir {}".format(d_name))
        print()

    elif ((("see" in ch) or ("total free" in ch)) or ("watch" in ch) and (("ram" in ch) or ("RAM" in ch))):
        os.system("free -m")

    elif ((("see" in ch) or ("total" in ch) or ("run" in ch)) and (("CPU utilization" in ch) or ("cpu information" in ch) or ("cpu" in ch))):
        os.system("lscpu")

    elif ((("watch" in ch) or ("see" in ch) or ("run" in ch)) and (("ip address" in ch) or ("ip" in ch))):
        os.system("ifconfig")

    elif ((("make" in ch) or ("create" in ch)) and ("file" in ch)):
        print("Enter file name :",end = '')
        f_name = input("Enter the file name")
        location = input("Enter the location :")
        os.system("touch {}/{}".format(location,f_name))
        print()
  
    elif ((("run" in ch) or ("execute" in ch) or ("see" in ch)) and (("connectivity" in ch) or ("ping" in ch))):
        print("Enter IP :",end = '')
        ip = input()
        os.system("ping {}".format(ip))
        print()

    elif ((("exit" in ch) or ("return" in ch) or ("back" in ch)) and (("main menu" in ch) or ("from linux menu"))):
        os.system("exit")
        break
       
    else:
        print("Invalid Choice")
    input("Enter to run more linux menu...")
    os.system("clear")

