#!/usr/bin/python3

import yagmail
import csv
import termcolor
import os
import sys

os.system('color')


def load_applicants(filename):
    with open(filename, mode="r") as f:
        csv_reader = csv.reader(f)
        list_from_csv = []
        
        for row in csv_reader:
            for string in row:
                list_from_csv.append(string.replace(" ", ""))
    return list_from_csv


def find_pdf(filename):
    for root, dirs, files in os.walk(r"./"):
        for name in files:
            if name == filename:
                return os.path.abspath(os.path.join(root, name))              


# mailing process
def send_mail(applicants, content, attachment):
    try:
        yag = yagmail.SMTP("cookieacademy21@gmail.com")

        # validate attachment
        if find_pdf(attachment) == None:
            sys.exit(1)
        else:
            # Event Invitation
            yag.send(to=applicants, cc="cookieacademy2020@gmail.com", bcc="cookieacademy19@gmail.com", subject="Students ID & Classroom Invitation Link", contents=content, attachments=find_pdf(attachment))
            print(termcolor.colored("***** Sent Invitation Successfully *****", "green", attrs=["bold"]))

    except SystemExit:
        print(termcolor.colored("Cannot find attachment. Please recheck the attachment filename. Aborting...", "red"))
    except:
        print(termcolor("Error, email was not sent", "red"))


def confirm(applicants):
    print(termcolor.colored(f"Recipents: {applicants}", "yellow", attrs=["bold"]))

    if len(applicants) == 0:
        print(termcolor.colored("Please enter recipents in academic_applicants.csv", "red"))
    else:
        answer = ""
        while answer not in ["y", "n"]:
            answer = input("OK to push to continue [Y/N]? ").lower()
        return answer == "y"


if __name__ == "__main__":
    applicants     = load_applicants("academic_applicants.csv")
    class_name     = input("Enter the Name of the Class     : ")
    classroom_link = input("Enter the Google Classroom link : ")
    attachment     = input("Enter the Name of Attachment    : ")

    content = [f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link href="https://fonts.googleapis.com/css2?family=Roboto" rel="stylesheet"><title>Students ID & Classroom Invitation!</title></head>
    <body><div style="font-family:'Roboto'; box-shadow: rgb(212, 212, 212) 4px 4px; background-color:rgb(255, 255, 255); color: black; max-width: 500px; margin:auto; border: 2px solid #253a6d;"><div style="text-align:center; margin-top: 25px"><img style="width: 100%; max-width: 100px;" src="https://i.imgur.com/jfyuaOh.png" alt="cookie-logo" /><div style="max-width: 65%; font-family: 'Roboto'; font-weight: 300; font-size: 15px; color: #253a6d; margin: 20px auto;"><p style="text-align: center;">Thank You for joining {class_name} at <i>Cookie Academy</i>. You can check your name, email and student ID number in the attachment below.</p></div><a style="text-decoration: none; color: white; font-size: 14px; padding: 10px 15px; background-color: #00b9e7; border-radius: 10px;" href="{classroom_link}">Join Classroom</a><p style="font-family: 'Roboto'; font-weight: 300;font-size: 16px; margin-top: 30px;">Follow us on Social Media</p><div style="display:flex; margin-top: 10px; margin-bottom: 15px;"><div style="display:flex; margin:auto"><a href="https://www.facebook.com/cookieacademymm" target="blank"><img alt="facebook" height="30" src="https://i.imgur.com/on4VXmE.png" style="display:block; height:auto; padding-right: 25px; border:0;" title="Facebook" width="30" /></a><a href="#" target="blank"><img alt="instagram" height="30" src="https://i.imgur.com/TRncuPi.png" style="display:block; padding-right:25px; height:auto; border:0;" title="Instagram" width="30" /></a><a href="https://discord.gg/HDk38j7wJv" target="blank"><img alt="discord" height="30" src="https://i.imgur.com/B1rsYUF.png" style="display:block; height:auto; border:0;" title="Discord" width="30" /></a></div></div><div style=" font-family: 'Roboto' ; font-weight: 300; font-size: 13px; color: #7a7a7a; padding-top: 10px; padding-bottom: 35px;"><p style="margin: 3px;">Email: cookieacademy21@gmail.com</p><p style="margin: 3px;">Academic Department</p><p style="margin: 3px;">Cookie Academy © 2021</p></div></div></div></div></div></div></body>
    </html>"""]

    if confirm(applicants):
       send_mail(applicants, content, attachment)
    else:
       print(termcolor.colored("Program Abort", "red"))
