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
    print("----------------------------------------------------------------")
    position = input("Enter the Position of Applicants              : ")
    doc_link = input("Enter the Google Document Link                : ")
    title    = input("Enter the Interview Title                     : ")
    date     = input("Enter the Interview Date (eg. October 10)     : ")
    time     = input("Enter the Interview Time (eg. 2:00 to 3:00 pm): ")

    return position, doc_link, title, date, time, reject_letter, discord_invitation


def html_text(position, doc_link, title, date, time, name, reject_letter, discord_invitation):
    interview_invitation = f"""<!DOCTYPE html><html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" style="box-sizing:border-box; padding:0px; margin:0px"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet" type="text/css" /><link href="https://fonts.googleapis.com/css?family=Karla" rel="stylesheet" type="text/css" /></head>
<body style="box-sizing: border-box font-family:'Karla'"><div style="box-sizing:border-box; margin-left: auto; margin-right:auto; max-width:500px; background-color:#253a6d;"><img style  ="box-sizing: border-box; margin: auto; border: 0; display:block; max-width:500px; width:100%" src="https://i.imgur.com/3jmX19l.jpg" alt="cover" padding:0px>
        <h1 style="box-sizing: border-box; padding:0px; margin:0px; font-family:'Poppins'; font-size:30px;  text-align: center; color: #f1dfb7">You're Invited!</h1>
        <img style="box-sizing: border-box; margin: auto; display: block; border: 0; width: 100px; max-width:100%" src="https://i.imgur.com/wbLDpc2.png" alt="cookie logo"/>
    <div style="box-sizing: border-box; margin: auto; max-width:350px; text-align: center"><p style="font-size: 16px; font-family:'Poppins'; color: #f1dfb7">Thank you for applying for the position of <strong>{position}</strong> with Cookie Academy. We would like to invite you to join the meeting to interview for the position. Click the button below to see your schedule.</p>
    <a style="margin: auto; max-width: 45%; text-decoration: none; display: block; outline:none; overflow:hidden; background-color:#f1dfb7; color:#253a6d; font-weight: bold; padding:10px 8px; border-radius:10px" href="{doc_link}">Check Schedule</a>
    <p style="box-sizing:border-box; font-size:18px; margin-bottom: 0px; padding: 0px; text-decoration: underline; color:#f1dfb7">Google Meet Info</p><p style="border-box:box-sizing; margin-top: 4px; margin-bottom: 0px; padding:0px; color:#f1dfb7">{title}
     {date}, {time}, {name}</p>
    <a style="margin: auto; max-width: 40%; text-decoration: none; display: block; outline:none; overflow:hidden; background-color:#f1dfb7; color:#253a6d; font-weight: bold; padding:10px 5px; border-radius:10px" href="https://meet.google.com/idb-aotb-pjm">Join Meeting</a>
    <div style="display:flex"><div style="display:flex; margin:auto"><a href="https://www.facebook.com/cookieacademymm" target="blank"><img alt="facebook" height="32" src="https://i.imgur.com/on4VXmE.png" style="display:block; height:auto; padding-right: 25px; border:0;" title="Facebook" width="32"/></a><a href="https://www.facebook.com/cookieacademymm" target="blank"><img alt="instagram" height="32" src="https://i.imgur.com/Xx7nxgi.png" style="display:block; padding-right:25px; height:auto; border:0;" title="Instagram" width="32"/></a><a href="https://discord.com/invite/sMfdX4Pvz5" target="blank"><img alt="discord" height="32" src="https://i.imgur.com/B1rsYUF.png" style="display:block; height:auto; border:0;" title="Discord" width="32"/></a><a href="#" target="blank"></div></div><p style="color: #ebebeb; font-size: 12px; text-decoration: none; margin-bottom:0px">Email: <a style="margin: 2px 0px 0px 0px; font-size: 12px; color: #ebebeb" href="cookieacademy19@gmail.com">cookieacademy19</a></p><p style="margin: 2px 0px 0px 0px; color: #ebebeb; font-size:12px">Human Resource Department</p><p style="margin: 2px 0px 0px 0px; color: #ebebeb; font-size:12px">Cookie Academy © 2021</p></div>
    </div>
</body>
</html>
"""

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
