#!/usr/bin/python3
import yagmail
import json
import csv
from json_html_writer import *
from collections import defaultdict


# load applicants names
# def load_applicants(filename):
#     with open(filename, mode="r") as f:
#         csv_reader = csv.reader(f)
#         list_from_csv = []
        
#         for row in csv_reader:
#             for string in row:
#                 list_from_csv.append(string.replace(" ", ""))
#     print(list_from_csv)
#     return list_from_csv


def load_applicants(filename):
    columns = defaultdict(list)
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k, v) in row.items():
                columns[k].append(v)

    name_list = columns['Name']
    email_list = columns['Email']
    zip_iterator = zip(name_list, email_list)
    applicants = dict(zip_iterator)

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
            print("sent interview invitation")
            
        # Result
        elif invitation == "1":
            # discord invitation
            if result_type == "0":
                yag.send(to=email, cc="cookieacademy2020@gmail.com", subject=data["subject"]["IR"], contents=data["body"]["discord_invitation"])
                print("sent discord invitation")
            # rejection letter
            else:
                yag.send(to=email, cc="cookieacademy2020@gmail.com", subject=data["subject"]["IR"], contents=data["body"]["reject_letter"])
                print("sent rejection letter")

        print("Email sent successfully")
    except:
        print("Error, email was not sent")


def confirm(email_list, invitation, result_type, data):
    print("--------------------------------------------------")
    print("Recipents: ", end = "")
    print(email_list)
    print("--------------------------------------------------")
    if invitation == "0":
        print("Type of Letter: Invitation Letter")
        print("Review of the email: ")
        # print(data["body"]["interview_invitation"])
    else:
        if result_type == "0":
            print("Type of Letter: Discord Invitation")
        else: 
            print("Type of Letter: Rejection Letter")

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
            print('error')
            print("Abort due to wrong input")
            quit()

    name_list, email_list, applicants = load_applicants("applicants.csv")

    # configure JSON file
    # if the email is for interview, update the config file
    # else don't need to update
    if (invitation == "0"):
        # update_config()
        position, doc_link, title, date, time, reject_letter, discord_invitation = update_config()
        # print(position)
        # print(doc_link)
        # print(title)
        # print(date)
        # print(time)

        for name, email in applicants.items():
            # print("=============")
            # print(name)
            # print(email)
            # print(applicants)
            # print("=============")

            html_text(position, doc_link, title, date, time, name, reject_letter, discord_invitation)
            # load JSON file    
            data = load_json("jsonfile.json")

            if confirm(email_list, invitation, result_type, data):
                mail(invitation, result_type, data, email)
            else:
                print("Abort")

    elif (invitation == "1"):
        data = load_json("jsonfile.json")
        if confirm(email_list, invitation, result_type, data):
            mail(invitation, result_type, data, email)
        # pass

    else:
        print("Abort due to wrong input")
        quit()
        

    # for name, email in applicants.items():
    #     print("=============")
    #     print(name)
    #     print(email)
    #     print(applicants)
    #     print("=============")

    #     html_text(name)
    #     # load JSON file    
    #     data = load_json("jsonfile.json")

    # if confirm(email_list, invitation, result_type, data):
    #     mail(invitation, result_type, data, email)
    # else:
    #     print("Abort")
