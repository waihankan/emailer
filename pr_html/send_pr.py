#!/usr/bin/python3
import yagmail
import csv
import termcolor
import os

os.system('color')


# load applicants names
def load_applicants(filename):
    with open(filename, mode="r") as f:
        csv_reader = csv.reader(f)
        list_from_csv = []
        
        for row in csv_reader:
            for string in row:
                list_from_csv.append(string.replace(" ", ""))
    return list_from_csv


# mailing process
def send_mail(applicants, content):
    try:
        yag = yagmail.SMTP("cookieacademy19@gmail.com")

        # Event Invitation
        yag.send(to=applicants, cc="cookieacademy2020@gmail.com", subject="Event Invitation", contents=content)
        print(termcolor.colored("***** Sent Invitation Successfully *****", "magenta", attrs=["bold"]))

    except:
        print(termcolor("Error, email was not sent", "red", attrs=["bold"]))


def confirm(applicants):
    print(termcolor.colored(f"Recipents: {applicants}", "yellow"))

    answer = ""
    while answer not in ["y", "n"]:
        answer = input("OK to push to continue [Y/N]? ").lower()
    return answer == "y"


if __name__ == "__main__":
    applicants   = load_applicants("pr_applicants.csv")
    topic        = input("Enter the Session Topic                       : ")
    meeting_link = input("Enter the Meeting link                        : ")
    date         = input("Enter the Interview Date (eg. October 10)     : ")
    time         = input("Enter the Interview Time (eg. 1:00 to 2:00 pm): ")

    content = [f"""
    <!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><metaname="viewport" content="width=device-width, initial-scale=1.0"><link href="https://fonts.googleapis.com/css2?family=Roboto" rel="stylesheet" type="text/css" /></head>
    <body>
        <div style="font-family:'Roboto';  color: black; max-width: 500px; margin:auto; border: 2px solid #253a6d;"><div style="text-align:center; margin-top: 25px"><img style="width: 100%; max-width: 100px;" src="https://i.imgur.com/jfyuaOh.png" alt="cookie-logo" /><h1 style="font-family: 'Roboto'; font-weight: lighter; margin: 25px 0px 10px 0px; color:#cc080f;">Event Invitation!</h1><p style="margin: 0px; font-size: 19px; font-family: 'Roboto'; font-weight: 300; color: rgb(143, 143, 143);">You have successfully registered</p><p style="font-family: 'Roboto'; font-weight: 300;font-size: 18px; margin-top: 20px;">Follow us on Social Media</p><div style="display:flex; margin-top: 10px; margin-bottom: 30px;"><div style="display:flex; margin:auto"><a href="https://www.facebook.com/cookieacademymm" target="blank"><img alt="facebook" height="32" src="https://i.imgur.com/on4VXmE.png" style="display:block; height:auto; padding-right: 25px; border:0;" title="Facebook" width="32" /></a><a href="#" target="blank"><img alt="instagram" height="32" src="https://i.imgur.com/TRncuPi.png" style="display:block; padding-right:25px; height:auto; border:0;" title="Instagram" width="32" /></a><a href="https://discord.com/invite/sMfdX4Pvz5" target="blank"><img alt="discord" height="32"src="https://i.imgur.com/B1rsYUF.png" style="display:block; height:auto; border:0;" title="Discord"width="32" /></a></div></div><div style="max-width: 75%; font-family: 'Roboto'; font-weight: 300; font-size: 15px; color: black; margin: 20px auto;"><p style="text-align: center;">Thank You for registering our Knowledge Sharing Session about {topic}. Make sure that you’re joining the link at the exact time as the announcement. We would appreciate it if you let us know whether you will be attending the Session or not.</p></div><div style="font-size:15px;font-family:'Roboto';font-weight:300;padding:0px 0px 20px 0px"><p style="text-decoration:underline;margin:7px;">Google Meet Info</p><p style="margin:3px;">{topic}</p><p style="margin:1px;">{date}, {time}</p></div><a style="text-decoration:none; color:white; font-size:14px; padding:10px 15px;background-color:#2f57be; border-radius:10px;"href="{meeting_link}">Join Webinar</a>
        <div style=" font-family: 'Roboto' ; font-weight: 300; font-size: 13px; color: #7a7a7a; padding-top: 20px; padding-bottom: 35px;"><p style="margin: 3px;">Email: cookieacademy19@gmail.com</p><p style="margin: 3px;">Public Relations Department</p><p style="margin: 3px;">Cookie Academy © 2021</p></div></div></div></div></div></div>
    </body>
    """]

    if confirm(applicants):
        send_mail(applicants, content)
    else:
        print(termcolor.colored("Abort", "red", attrs=["bold"]))
