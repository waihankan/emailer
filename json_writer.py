#!/usr/bin/python3

import json


def update_config():
    # rejection letter
    reject_letter = """Greetings,

    We appreciate your interest in Cookie Academy and the time you’ve invested in applying for the volunteering.

    We ended up moving forward with another candidate, but we’d like to thank you for talking to our team and giving us the opportunity to learn about your skills and accomplishments.

    We will be advertising more positions in the coming months. We hope you’ll keep us in mind and we encourage you to apply again.

    We wish you good luck with your job search and professional future endeavors.

    Best,

    Cookie Academy HR department

    Wai
    HR Department
    Cookie Academy
    cookieacademy19@gmail.com"""


    # discord invitation letter"
    discord_invitation = """Greetings,

    Congratulations! This email is to formally offer you a volunteering job for Cookie Academy. We strongly believe that your skills and expertise will help our organization to reach great heights.\n
    Here is the discord link of our server - https://discord.com/invite/sMfdX4Pvz5

    We are looking forward to working with you.

    Please contact me in case of any queries.
    

    Yours’ sincerely, 

    Wai
    HR Department
    Cookie Academy
    cookieacademy19@gmail.com"""


    # Request User Data for Interview Invitation
    position = input("Enter the Position of applicants: ")
    doc_link = input("Enter the Google Document Link: ")
    print("Enter the meeting information: ")
    no_of_lines = 4
    meeting_link = ""
    for i in range(no_of_lines):
        meeting_link+=input()+"\n"

    interview_invitation = f"""Greetings,

    Thank you for applying for the position of {position} with Cookie Academy.

    We would like to invite you to join the meeting to interview for the position and here is the link for individuals respectively - {doc_link} 

    Here is the detail of google meet:

    {meeting_link}
    Please email me at cookieacademy19@gmail.com if you have any questions or need to reschedule. We would be appreciated if you let us know whether you will be attending the meeting or not. Note: If you’re not accepted by the host at the exact time, please wait for a while. We will try our best to let you in.


    Sincerely,

    Wai
    HR Department
    Cookie Academy
    cookieacademy19@gmail.com"""


    # pre-processing before dumping JSON
    info = {
            "subject" : {
                "IR": "Interview Result",
                "IL": "Invitation Letter"
                }, 
            
            "body" : {
                "interview_invitation": interview_invitation,
                "reject_letter": reject_letter,
                "discord_invitation": discord_invitation
            }
            }

    with open("jsonfile.json", "w") as jsonfile:
        json.dump(info, jsonfile)
