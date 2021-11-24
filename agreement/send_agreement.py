#!/usr/bin/python3

from collections import defaultdict
import yagmail
import csv
import termcolor
import os

os.system('color')


def load_applicants(filename):
    columns = defaultdict(list)
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k, v) in row.items():
                columns[k].append(v)

    email_list = columns['Email']
    time_list = columns['Time']
    applicants = dict(zip(email_list, time_list))
    return email_list, time_list, applicants


# mailing process
def send_mail(email, content):
    try:
        yag = yagmail.SMTP("cookieacademy19@gmail.com")

        # Event Invitation
        yag.send(to=email, cc="cookieacademy2020@gmail.com", subject="Course Timeline Agreement", contents=content)

    except:
        print(termcolor("Error, email was not sent", "red"))


def confirm(email_list):
    print(termcolor.colored(f"Recipients: {email_list}", "yellow", attrs=["bold"]))

    if len(email_list) == 0:
        print(termcolor.colored("Please enter recipients in agreement_applicants.csv", "red"))
    else:
        answer = ""
        while answer not in ["y", "n"]:
            answer = input("OK to push to continue [Y/N]? ").lower()
        return answer == "y"

# update html every loop
def update_html(time):

    content = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"><link href="https://fonts.googleapis.com/css2?family=Roboto" rel="stylesheet" type="text/css"><title>Timeline and Curriculum</title></head><body><div style="font-family:'Roboto'; box-shadow: rgb(212, 212, 212) 4px 4px; background-color:rgb(255, 255, 255); color: black; max-width: 500px; margin:auto; border: 2px solid #253a6d;"><div style="text-align:center; margin-top: 25px"><img style="width: 100%; max-width: 100px;" src="https://i.imgur.com/jfyuaOh.png" alt="cookie-logo" /><div style="max-width: 60%; font-family: 'Roboto'; font-weight: 300; font-size: 15px; color: #253a6d; margin: 20px auto;"><p style="text-align: center;">We would like to invite you to join this meeting for a discussion on the Course Timeline & Curriculum.</p><p style="text-align: center; color:red">Time: {time}</p></div><div><a style="text-decoration: none; color: white; font-size: 14px; padding: 8px 8px; background-color: #627c74; border-radius: 10px; margin-right: 5px;" target="_" href="https://drive.google.com/file/d/1pm6k4_j-V23QGNNwYjWC5sC89cuQoox8/view?usp=sharing">View Agreement</a><a style="text-decoration: none; color: white; font-size: 14px; padding: 8px 8px; background-color: #253a6d; border-radius: 10px; margin-left: 5px;" target="_" href="https://meet.google.com/wbn-ynet-wyr">Join Meeting</a></div><p style="font-family: 'Roboto'; font-weight: 300;font-size: 13px; margin-top: 30px;">Follow us on Social Media</p><div style="display:flex; margin-top: 10px; margin-bottom: 15px;"><div style="display:flex; margin:auto"><a href="https://www.facebook.com/cookieacademymm" target="blank"><img alt="facebook" height="30" src="https://i.imgur.com/on4VXmE.png" style="display:block; height:auto; padding-right: 25px; border:0;" title="Facebook" width="30" /></a><a href="#" target="blank"><img alt="instagram" height="30" src="https://i.imgur.com/TRncuPi.png" style="display:block; padding-right:25px; height:auto; border:0;" title="Instagram" width="30" /></a><a href="https://discord.com/invite/sMfdX4Pvz5" target="_"><img alt="discord" height="30" src="https://i.imgur.com/B1rsYUF.png" style="display:block; height:auto; border:0;" title="Discord" width="30" /></a></div></div><div style=" font-family: 'Roboto' ; font-weight: 300; font-size: 13px; color: #7a7a7a; padding-top: 10px; padding-bottom: 35px;"><p style="margin: 3px;">Email: cookieacademy21@gmail.com</p><p style="margin: 3px;">Contact : 09776738837, 09880039003</p><p style="margin: 3px;">Academic Department</p><p style="margin: 3px;">Cookie Academy © 2021</p></div></div></div></div></div></div></body></html>    
    """

    return content


if __name__ == "__main__":
    email_list, time_list, applicants = load_applicants("agreement_applicants.csv")

    # print("applicants = ", applicants)
    # print("email_list = ", email_list)
    # print("time_list = ", time_list)
    if confirm(email_list):
        print("\n===========================================================")
        for email, time in applicants.items():
            content = update_html(time)
            print(termcolor.colored(email, "magenta", attrs=["bold"]) + "\t\t" + termcolor.colored(time, "cyan", attrs=["bold"]))
            send_mail(email, content)
        print("===========================================================")
        print(termcolor.colored("************************* SUCCESS *************************\n", "green", attrs=["bold", "blink"]))
    else:
       print(termcolor.colored("Program Abort", "red"))
