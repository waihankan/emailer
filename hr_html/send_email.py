#!/usr/bin/python3

import yagmail
import json
import csv
from json_html_writer import *
from collections import defaultdict
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

    name_list = columns['Name']
    email_list = columns['Email']
    applicants = dict(zip(name_list, email_list))
    return name_list, email_list, applicants


# load json data 
def load_json(filename):
    with open(filename, "r") as jsonfile:
        data = json.load(jsonfile)
        return data


# mailing process
def mail(invitation, result_type, data, email):
    try:
        yag = yagmail.SMTP("cookieacademy19@gmail.com")

        # Interview Invitation
        if invitation == "0":
            yag.send(to=email, cc="cookieacademy2020@gmail.com", subject=data["subject"]["IL"], contents=data["body"]["interview_invitation"])
            print(termcolor.colored("Sent Interview Invitation", "cyan"))
            
        # Result
        elif invitation == "1":
            # discord invitation
            if result_type == "0":
                yag.send(to=email, cc="cookieacademy2020@gmail.com", subject=data["subject"]["IR"], contents=data["body"]["discord_invitation"])
                print(termcolor.colored("Sent Discord Invitation", "cyan"))
            # rejection letter
            else:
                yag.send(to=email, cc="cookieacademy2020@gmail.com", subject=data["subject"]["IR"], contents=data["body"]["reject_letter"])
                print(termcolor.colored("Sent Rejection Letter", "cyan"))

    except:
        print(termcolor.colored("Error, email was not sent", "red"))


def confirm(email_list, invitation, result_type):
    print("----------------------------------------------------------------")
    print(termcolor.colored(f"Recipients: {email_list}", "yellow", attrs=["bold"]))
    print("----------------------------------------------------------------")

    if len(email_list) == 0:
        print(termcolor.colored("Please enter recipients in hr_applicants.csv", "red"))
    else:
        if invitation == "0":
            print(termcolor.colored("Type of Letter: Invitation Letter", "blue"))
        else:
            if result_type == "0":
                print(termcolor.colored("Type of Letter: Discord Invitation", "blue"))
            else: 
                print(termcolor.colored("Type of Letter: Rejection Letter", "blue"))

        answer = ""
        while answer not in ["y", "n"]:
            answer = input("OK to push to continue [Y/N]? ").lower()
        return answer == "y"


if __name__ == "__main__":
    # Asking all the requirements
    result_type = "0"
    invitation = input("Press 0 for Interview Invitation, 1 for Interview Result: ")
    if invitation == "1":
        result_type = input("Press 0 for Discord Invitation, 1 for Rejection Letter: ")
        if (result_type != "0" and result_type != "1"):
            print(termcolor.colored("Error", "red"))
            print(termcolor.colored("Abort due to wrong input", "red"))
            quit()

    name_list, email_list, applicants = load_applicants("hr_applicants.csv")

    if (invitation == "0"):
        print("----------------------------------------------------------------")
        position = input("Enter the Position of Applicants               : ")
        doc_link = input("Enter the Google Document Link                 : ")
        title    = input("Enter the Interview Title                      : ")
        date     = input("Enter the Interview Date (eg. October 10)      : ")
        time     = input("Enter the Interview Time (eg. 2:00 to 3:00 pm) : ")
        print("----------------------------------------------------------------")
        print("Position      : ", position)
        print("Document Link : ", doc_link)
        print("Title         : ", title)
        print("Date          : ", date)
        print("Time          : ", time)

        if confirm(email_list, invitation, result_type):
            # loop for each applicant
            for name, email in applicants.items():
                update_html(name, position, doc_link, title, date, time)
                print("===========================")
                print(termcolor.colored(f"Name : {name}", "cyan"))
                print(termcolor.colored(f"Email: {email}", "cyan"))
                # load JSON file
                data = load_json("jsonfile.json")
                mail(invitation, result_type, data, email)
            
            print("===========================")
            print(termcolor.colored("********* SUCCESS *********", "green", attrs=["bold"]))
        else:
            print(termcolor.colored("Program Abort", "red"))

    elif (invitation == "1"):
        if confirm(email_list, invitation, result_type):
            # loop for each applicant
            for name, email in applicants.items():
                update_html(name)
                print("===========================")
                print(termcolor.colored(f"Name : {name}", "cyan"))
                print(termcolor.colored(f"Email: {email}", "cyan"))
                # load JSON file
                data = load_json("jsonfile.json")
                mail(invitation, result_type, data, email)

            print("===========================")
            print(termcolor.colored("********* SUCCESS *********", "green", attrs=["bold"]))
        else:
            print(termcolor.colored("Program Abort", "red"))

    else:
        print(termcolor.colored("Abort due to wrong input", "red"))
        quit()
