#!/usr/bin/python3

import json

def update_html(name, position=None, doc_link=None, title=None, date=None, time=None):
    # rejection letter
    reject_letter = f"""
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link href="https://fonts.googleapis.com/css2?family=Roboto" rel="stylesheet" type="text/css"><title>Congratulations!</title></head>
<body>
    <div style="font-family:'Roboto'; box-shadow: rgb(212, 212, 212) 4px 4px; background-color:rgb(255, 255, 255); color: black; max-width: 500px; margin:auto; border: 2px solid #253a6d;"><div style="text-align:center; margin-top: 25px"><img style="width: 100%; max-width: 100px;" src="https://i.imgur.com/jfyuaOh.png" alt="cookie-logo" /><h1 style="font-family: 'Roboto'; font-weight: 300; margin: 25px 0px 10px 0px; color: #cc080f">WE'RE SORRY!</h1><img style=" padding-top: 20px; width: 100%; max-width: 90px;" src="https://i.imgur.com/kIEQzSr.png" alt="bear" /><div style="max-width: 75%; font-family: 'Roboto'; font-weight: 300; font-size: 15px; color: black; margin: 20px auto;"><p style="text-align:center;">Dear {name},</p><p style="text-align: center; color: black">We appreciate your interest in <i>Cookie Academy </i> and the time you’ve invested in applying for the volunteering. We ended up moving forward with another candidate, but we’d like to thank you for talking to our team and giving us the opportunity to learn about your skills and accomplishments. We will be advertising more positions in the coming months. We hope you’ll keep us in mind and we encourage you to apply again. We wish you good luck with your job search and professional future endeavors.</p></div><p style="font-family: 'Roboto'; font-weight: 300;font-size: 13px; margin-top: 25px; margin-bottom: 0px;">Follow us on Social Media</p><p style="font-family: 'Roboto'; font-weight: 300;font-size: 13px; margin: 0px;"> for more volunteering positions</p><div style=" display:flex; margin-top: 10px; margin-bottom: 10px;"><div style="display:flex; margin:auto"><a href="https://www.facebook.com/cookieacademymm" target="blank"><img alt="facebook" height="32" src="https://i.imgur.com/Yk7PQyx.png" style="display:block; height:auto; padding-right: 25px; border:0;" title="Facebook" width="32" /></a><a href="#" target="blank"><img alt="instagram" height="32" src="https://i.imgur.com/HPGn5Rw.png" style="display:block; padding-right:25px; height:auto; border:0;" title="Instagram" width="32" /></a><a href="https://discord.gg/HDk38j7wJv" target="blank"><img alt="discord" height="32" src="https://i.imgur.com/kvuAayt.png" style="display:block; height:auto; border:0;" title="Discord" width="32" /></a></div></div><div style=" font-family: 'Roboto' ; font-weight: 300; font-size: 13px; color: #7a7a7a; padding-top: 30px; padding-bottom: 35px;"><p style="margin: 3px;">Email: cookieacademy19@gmail.com</p><p style="margin: 3px;">Human Resource Department</p><p style="margin: 3px;">Cookie Academy © 2021</p></div></div></div></div></div></div>
</body>
</html>
"""

    # discord invitation letter
    discord_invitation = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link href="https://fonts.googleapis.com/css2?family=Roboto" rel="stylesheet" type="text/css"><title>Congratulations!</title></head>
<body>
    <div style="font-family:'Roboto'; box-shadow: rgb(212, 212, 212) 4px 4px; background-color:rgb(255, 255, 255); color: black; max-width: 500px; margin:auto; border: 2px solid #253a6d;"><div style="text-align:center; margin-top: 25px"><img style="width: 100%; max-width: 100px;" src="https://i.imgur.com/jfyuaOh.png" alt="cookie-logo" /><h1 style="font-family: 'Roboto'; font-weight: 300; margin: 25px 0px 10px 0px; color: #cc080f">WELCOME ABOARD!</h1><p style="margin: 0px; font-size: 19px; font-family: 'Roboto'; font-weight: 300; color: rgb(143, 143, 143);">You have been selected</p><img style=" padding-top: 20px; width: 100%; max-width: 80px;" src="https://i.imgur.com/TeE5qHf.png" alt="balloon" /><div style="max-width: 70%; font-family: 'Roboto'; font-weight: 300; font-size: 15px; color: black; margin: 20px auto;">
    <p style=text-align: center;>Dear {name},</p><p style="text-align: center; color:black"><i>Congratulations!</i> This email is to formally offer you a volunteering job at <i>Cookie Academy</i>. We strongly believe that your skills and expertise will help our organization to reach great heights. We are looking forward to working with you. Please contact me in case of any queries.</p></div>    
    <div style="display: flex;"><div style="display: flex; margin:auto; background-color: #2f57be; border-radius: 15px; padding: 4px 9px;"><a href="https://discord.gg/HDk38j7wJv" target="blank"><img alt="discord" height="32" src="https://i.imgur.com/kvuAayt.png" style="display:block; height:auto; border:0;" title="Discord" width="32" /></a><a style="margin-left: 5px;padding-top: 6px;text-decoration: none; color: white; font-size: 14px;" href="https://discord.gg/HDk38j7wJv" target="blank">Join Our Discord Channel</a></div></div><div style=" font-family: 'Roboto' ; font-weight: 300; font-size: 13px; color: #7a7a7a; padding-top: 30px; padding-bottom: 35px;"><p style="margin: 3px;">Email: cookieacademy19@gmail.com</p><p style="margin: 3px;">Human Resource Department</p><p style="margin: 3px;">Cookie Academy © 2021</p></div></div></div></div></div></div>
</body>
</html>
"""
    
    # invitation letter
    interview_invitation = f"""<!DOCTYPE html><html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" style="box-sizing:border-box; padding:0px; margin:0px"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet" type="text/css" /><link href="https://fonts.googleapis.com/css?family=Karla" rel="stylesheet" type="text/css" /></head>
<body style="box-sizing: border-box font-family:'Karla'"><div style="box-sizing:border-box; margin-left: auto; margin-right:auto; max-width:500px; background-color:#253a6d;"><img style  ="box-sizing: border-box; margin: auto; border: 0; display:block; max-width:500px; width:100%" src="https://i.imgur.com/hY9kal9.jpg" alt="cover" padding:0px>
        <h1 style="box-sizing: border-box; padding:0px; margin:0px; font-family:'Poppins'; font-size:30px;  text-align: center; color: #f1dfb7">You're Invited!</h1>
        <img style="box-sizing: border-box; margin: auto; display: block; border: 0; width: 100px; max-width:100%" src="https://i.imgur.com/wbLDpc2.png" alt="cookie logo"/><div style="box-sizing: border-box; margin: auto; max-width:350px; text-align: center"><p style="font-size: 17px; font-family:'Poppins'; color: #f1dfb7">Dear {name},</p><p style="font-size: 16px; font-family:'Poppins'; color: #f1dfb7">Thank you for applying for the position of <strong>{position}</strong> with Cookie Academy. We would like to invite you to join the meeting to interview for the position. Click the button below to see your schedule.</p>
    <a style="margin: auto; max-width: 45%; text-decoration: none; display: block; outline:none; overflow:hidden; background-color:#f1dfb7; color:#253a6d; font-weight: bold; padding:10px 8px; border-radius:10px" href="{doc_link}">Check Schedule</a>
    <p style="box-sizing:border-box; font-size:18px; margin-bottom: 0px; padding: 0px; text-decoration: underline; color:#f1dfb7">Google Meet Info</p><p style="border-box:box-sizing; margin-top: 4px; margin-bottom: 0px; padding:0px; color:#f1dfb7">{title}
     {date}, {time}</p>
     <a style="margin: auto; max-width: 40%; text-decoration: none; display: block; outline:none; overflow:hidden; background-color:#f1dfb7; color:#253a6d; font-weight: bold; padding:10px 5px; border-radius:10px" href="https://meet.google.com/idb-aotb-pjm">Join Meeting</a>
    <div style="display:flex"><div style="display:flex; margin:auto"><a href="https://www.facebook.com/cookieacademymm" target="blank"><img alt="facebook" height="32" src="https://i.imgur.com/on4VXmE.png" style="display:block; height:auto; padding-right: 25px; border:0;" title="Facebook" width="32"/></a><a href="https://www.facebook.com/cookieacademymm" target="blank"><img alt="instagram" height="32" src="https://i.imgur.com/HPGn5Rw.png" style="display:block; padding-right:25px; height:auto; border:0;" title="Instagram" width="32"/></a><a href="https://discord.gg/HDk38j7wJv" target="blank"><img alt="discord" height="32" src="https://i.imgur.com/B1rsYUF.png" style="display:block; height:auto; border:0;" title="Discord" width="32"/></a><a href="#" target="blank"></div></div><p style="color: #ebebeb; font-size: 12px; text-decoration: none; margin-bottom:0px">Email: <a style="margin: 2px 0px 0px 0px; font-size: 12px; color: #ebebeb" href="cookieacademy19@gmail.com">cookieacademy19</a></p><p style="margin: 2px 0px 0px 0px; color: #ebebeb; font-size:12px">Human Resource Department</p><p style="margin: 2px 0px 0px 0px; color: #ebebeb; font-size:12px">Cookie Academy © 2021</p></div>
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
