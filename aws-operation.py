import os
import speech_recognition as sr

while True:

    print("\n")
    os.system("tput setaf 1")
    print("\t\t\t\t\t\t\tWELCOME TO AWS MENU")
    print("\t\t\t\t\t\t\t-------------------")
    os.system("tput setaf 7")
    print("""
                                                    Press 1. To create key pair
                                                    Press 2. To create security group
                                                    Press 3. To launch an instance
                                                    Press 4. To create S3 bucket
                                                    Press 5. To delete key pair
                                                    Press 6. To delete S3 bucket
                                                    Press 7. To start an instance
                                                    Press 8. To stop an instance
                                                    Press 9. To attach extra volume to the instance
                                                    Press 10. To exit from the AWS operations
    """)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start Speaking")
        audio = r.listen(source)
        print("Audio Recorded")
    
    ch = r.recognize_google(audio)
    if ((("create" in ch) or ("generate" in ch)) and (("key" in ch) or ("key pair" in ch))):
       key_name = input("Enter key name :")
       os.system("aws ec2 create-key-pair  --key-name {}".format(key_name))
       print()

    elif ((("create" in ch) or ("generate" in ch)) and (("security group" in ch) or ("firewall" in ch))):
       desc = input("Enter the description :")
       group_name = input("Enter a group name :")
       os.system("aws ec2 create-security-group --group-name {}  --description {}".format(group_name,desc))
       print()

    elif ((("run" in ch) or ("execute" in ch) or ("launch" in ch)) and (("instance" in ch) or ("os" in ch))):
       img_name = input("Enter your image:")
       i_type = input("Enter instance type :")
       key_name = input("Enter your key pair :")
       sg_group = input("Enter Security group id :")
       sub = input("Enter subnet-id :")
       os.system("aws ec2 run-instances --image-id {} --instance-type {} --key-name {} --security-group-ids {} --subnet-id {} --count 1 ".format(img_name,i_type,key_name,sg_group,sub))
       print()

    elif ((("create" in ch) or ("generate" in ch)) and (("s3 bucket" in ch) or ("bucket" in ch))):
       buc_name = input("Unique bucket name :")
       ac_list = input("Unique Access Control List :")
       reg = input("Region for the bucket to be deployed :")
       os.system("aws s3api create-bucket --bucket {} --acl {} --create-bucket-configuration LocationConstraint={} ".format(buc_name,ac_list,reg))       

    elif ((("delete" in ch) or ("terminate" in ch)) and (("key" in ch) or ("key pair" in ch))):
       key_name = input("Name of the key-pair which you want to delete :")
       os.system("aws ec2 delete-key-pair --key-name {} ".format(key_name))
       print()

    elif ((("delete" in ch) or ("terminate" in ch)) and (("bucket" in ch) or ("s3 bucket" in ch))):
       buc_name = input("Unique bucket name which you want to delete :")
       os.system("aws s3api delete-bucket --bucket {}".format(buc_name))
       print()

    elif (("start" in ch) and (("instance" in ch) or ("os" in ch))):
       ins_id = input("Enter instance id which you want to start :")
       os.system("aws ec2 start-instances --instance-ids {}".format(ins_id))
       print()

    elif (("stop" in ch) and (("instance" in ch) or ("os" in ch))):
       ins_id = input("Enter instance id which you want to stop :")
       os.system("aws ec2 stop-instances --instance-ids {}".format(ins_id))
       print()

    elif ((("attach extra volume" in ch) or ("add extra volume" in ch)) and (("instance" in ch) or ("os" in ch))):
       vol_name = input("Enter the device name of the volume which you want to attach ex. /dev/sdh :")
       ins_id = input("Enter your instance id :")
       vol_id = input("Enter volume id :")
       os.system("aws ec2 attach-volume --device {} --instance-id {} --volume-id {}".format(vol_name,ins_id,vol_id))
       print()

    elif ((("exit" in ch) or ("return back" in ch)) and ("menu main" in ch)):
       os.system("exit")
       break

    else:
       print("Invalid option")
    input("Enter to run more aws menu...")
    os.system("clear")
