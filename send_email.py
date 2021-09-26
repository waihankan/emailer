#!/usr/bin/python3
import yagmail
import json
import csv
from json_writer import update_config


# load applicants names
def load_applicants(filename):
    with open(filename, mode="r") as f:
        csv_reader = csv.reader(f)
        list_from_csv = []
        
        for row in csv_reader:
            for string in row:
                list_from_csv.append(string.replace(" ", ""))
    return list_from_csv


# load json data 
def load_json(filename):
    with open(filename, "r") as jsonfile:
        data = json.load(jsonfile)
        return data


# mailing process
def mail(invitation, result_type, applicants, data):
    try:
        yag = yagmail.SMTP("cookieacademy19@gmail.com")

        # Interview Invitation
        if invitation == "0":
                yag.send(to=applicants, cc="cookieacademy2020@gmail.com", subject=data["subject"]["IL"], contents=data["body"]["interview_invitation"])
                print("sent interview invitation")
            
        # Result
        elif invitation == "1":
            # discord invitation
            if result_type == "0":
                yag.send(to=applicants, cc="cookieacademy2020@gmail.com", subject=data["subject"]["IR"], contents=data["body"]["discord_invitation"])
                print("sent discord invitation")
            # rejection letter
            else:
                yag.send(to=applicants, cc="cookieacademy2020@gmail.com", subject=data["subject"]["IR"], contents=data["body"]["reject_letter"])
                print("sent rejection letter")

        print("Email sent successfully")
    except:
        print("Error, email was not sent")


def confirm(applicants, invitation, result_type, data):
    print("recipents: ", end = "")
    print(applicants)
    if invitation == "0":
        print("type of letter: invitation letter")
        print("Review of the email: ")
        print(data["body"]["interview_invitation"])
    else:
        if result_type == "0":
            print("type of letter: discord invitation")
        else: 
            print("type of letter: rejection letter")

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

    applicants = load_applicants("applicants.csv")

    # configure JSON file
    # if the email is for interview, update the config file
    # else don't need to update
    if (invitation == "0"):
        update_config()

    elif (invitation == "1"):
        pass

    else:
        print("Abort due to wrong input")
        quit()
        
    # load JSON file    
    data = load_json("jsonfile.json")

    if confirm(applicants, invitation, result_type, data):
        mail(invitation, result_type, applicants, data)
    else:
        print("Abort")
