#!/usr/bin/python3


# This is the test file for developers !!! Do NOT use this file. 

import yagmail

content = ["""
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link href="https://fonts.googleapis.com/css2?family=Roboto" rel="stylesheet" type="text/css"><title>Congratulations!</title></head>
<body>
    <div style="font-family:'Roboto'; box-shadow: rgb(212, 212, 212) 4px 4px; background-color:rgb(255, 255, 255); color: black; max-width: 500px; margin:auto; border: 2px solid #253a6d;"><div style="text-align:center; margin-top: 25px"><img style="width: 100%; max-width: 100px;" src="https://i.imgur.com/jfyuaOh.png" alt="cookie-logo" /><h1 style="font-family: 'Roboto'; font-weight: 300; margin: 25px 0px 10px 0px; color: #cc080f">WE'RE SORRY!</h1><img style=" padding-top: 20px; width: 100%; max-width: 90px;" src="https://i.imgur.com/kIEQzSr.png" alt="bear" /><div style="max-width: 75%; font-family: 'Roboto'; font-weight: 300; font-size: 15px; color: black; margin: 20px auto;"><p style="text-align:center;">Dear Applicant,</p><p style="text-align: center; color: black">We appreciate your interest in <i>Cookie Academy </i> and the time you’ve invested in applying for the volunteering. We ended up moving forward with another candidate, but we’d like to thank you for talking to our team and giving us the opportunity to learn about your skills and accomplishments. We will be advertising more positions in the coming months. We hope you’ll keep us in mind and we encourage you to apply again. We wish you good luck with your job search and professional future endeavors.</p></div><p style="font-family: 'Roboto'; font-weight: 300;font-size: 13px; margin-top: 25px; margin-bottom: 0px;">Follow us on Social Media</p><p style="font-family: 'Roboto'; font-weight: 300;font-size: 13px; margin: 0px;"> for more volunteering positions</p><div style=" display:flex; margin-top: 10px; margin-bottom: 10px;"><div style="display:flex; margin:auto"><a href="https://www.facebook.com/cookieacademymm" target="blank"><img alt="facebook" height="32" src="https://i.imgur.com/Yk7PQyx.png" style="display:block; height:auto; padding-right: 25px; border:0;" title="Facebook" width="32" /></a><a href="#" target="blank"><img alt="instagram" height="32" src="https://i.imgur.com/HPGn5Rw.png" style="display:block; padding-right:25px; height:auto; border:0;" title="Instagram" width="32" /></a><a href="https://discord.com/invite/sMfdX4Pvz5" target="blank"><img alt="discord" height="32" src="https://i.imgur.com/kvuAayt.png" style="display:block; height:auto; border:0;" title="Discord" width="32" /></a></div></div><div style=" font-family: 'Roboto' ; font-weight: 300; font-size: 13px; color: #7a7a7a; padding-top: 30px; padding-bottom: 35px;"><p style="margin: 3px;">Email: cookieacademy19@gmail.com</p><p style="margin: 3px;">Human Resource Department</p><p style="margin: 3px;">Cookie Academy © 2021</p></div></div></div></div></div></div>
</body>
</html>

"""]


def send_mail(content):
    yag = yagmail.SMTP("cookieacademy19@gmail.com")
    yag.send(to="goddess.gs13@gmail.com", subject="reject test", contents=content)
    print("success")

if __name__ == "__main__":
    send_mail(content)
