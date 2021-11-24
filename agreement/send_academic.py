#!/usr/bin/python3

from collections import defaultdict
from agreement import *
import yagmail
import csv
import termcolor
import os
import sys

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
        print(termcolor.colored("***** Sent Invitation Successfully *****", "green", attrs=["bold"]))

    except:
        print(termcolor("Error, email was not sent", "red"))


def confirm(email_list):
    print(termcolor.colored(f"Recipients: {email_list}", "yellow", attrs=["bold"]))

    if len(email_list) == 0:
        print(termcolor.colored("Please enter recipients in academic_applicants.csv", "red"))
    else:
        answer = ""
        while answer not in ["y", "n"]:
            answer = input("OK to push to continue [Y/N]? ").lower()
        return answer == "y"



if __name__ == "__main__":
    email_list, time_list, applicants = load_applicants("academic_applicants.csv")

    print("applicants = ", applicants)
    print("email_list = ", email_list)
    print("time_list = ", time_list)
    if confirm(email_list):
        for email, time in applicants.items():
            content = update_html(time)
            send_mail(email, content)
        print("=======================")
        print(termcolor.colored("****** SUCCESS ******", "green", attrs=["bold"]))
    else:
       print(termcolor.colored("Program Abort", "red"))
