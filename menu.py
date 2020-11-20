import os
import getpass
import speech_recognition as sr

password = getpass.getpass("Password : ")
if password != "menu":
    print("Wrong Password")
    exit()
else:
    while True:
         print("\n")
         os.system("tput setaf 1")
         print("\t\t\t\t\t\t\tWELCOME TO MAIN MENU")
         print("\t\t\t\t\t\t\t--------------------")
         os.system("tput setaf 7")
         print("""
                                                    Press 1 : To run Linux Operations
                                                    Press 2 : To run Docker Opearations
                                                    Press 3 : To run AWS Opearations
                                                    Press 4 : To run Hadoop Operations
                                                    Press 5 : To exit
         """)
         r = sr.Recognizer()
         with sr.Microphone() as source:
         print("Start Speaking")
         audio = r.listen(source)
         print("Speaking Done")

         ch = r.recognize_google(audio)
         if (("linux" in ch) or ("Linux" in ch) or ("linux-operation" in ch) and (("run" in ch) or ("execute" in ch))):
             os.system("python3 linux-operation.py")

         elif (("docker" in ch) or ("Docker" in ch) or ("docker-operation" in ch) and (("run" in ch) or ("execute" in ch))):
             os.system("python3 docker.py")

         elif (("aws" in ch) or ("AWS" in ch) or ("aws-operation" in ch) and (("run" in ch) or ("execute" in ch))):
             os.system("python3 aws-operation.py")

         elif (("hadoop" in ch) or ("Hadoop" in ch) or ("hadoop-operation" in ch) and (("run" in ch) or ("execute" in ch))):
             os.system("python3 hadoop.py")

         elif (("exit" in ch) or ("return" in ch) and (("main menu" in ch) or ("menu" in ch))):
             os.system("exit")
             break

         else:
             print("Invalid Option")

         input("Enter to run more main menu...")
         os.system("clear")


