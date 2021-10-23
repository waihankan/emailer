#!/usr/bin/python3

import sys
import yagmail
import csv


# load applicants names
def load_applicants(filename):
    try:
        with open(filename, mode="r") as f:
            csv_reader = csv.reader(f)
            list_from_csv = []
            
            for row in csv_reader:
                for string in row:
                    list_from_csv.append(string.replace(" ", ""))
        return list_from_csv
    except:
        print("FATAL: applicants.csv file not found")
        exit()

def get_text(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            return text
    except:
        print(f"FATAL: {sys.argv[1]} does not exist")

def send_mail(applicants, content):
    try:
        yag = yagmail.SMTP("cookieacademy19@gmail.com")
        yag.send(to=applicants, cc="cookieacademy2020@gmail.com", subject="Invitation from Cookie Academy", contents=content)
    except:
        print("Error: email was not sent")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("looks like the input style is incorrect")
        exit()

    else:
        applicants = load_applicants("applicants.csv")
        content = get_text(sys.argv[1])
        # print(content)
        # print(applicants)
        send_mail(applicants, content)
        print("Email sent successfully")
