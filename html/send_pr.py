#!/usr/bin/python3

import yagmail

content = ["""
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><metaname="viewport" content="width=device-width, initial-scale=1.0"><link href="https://fonts.googleapis.com/css2?family=Roboto" rel="stylesheet" type="text/css" /></head>
<body>
    <div style="font-family:'Roboto'; background-image:linear-gradient(180deg, white, #fafafa, #f5f5f5); color: black; max-width: 500px; margin:auto; border: 2px solid #253a6d;"><div style="text-align:center; margin-top: 25px"><img style="width: 100%; max-width: 100px;" src="https://i.imgur.com/0fMDYhg.png" alt="cookie-logo" /><h1 style="font-family: 'Roboto'; font-weight: lighter; margin: 25px 0px 10px 0px">Event Invitation!</h1><p style="margin: 0px; font-size: 19px; font-family: 'Roboto'; font-weight: 300; color: rgb(143, 143, 143);">You have successfully registered</p><p style="font-family: 'Roboto'; font-weight: 300;font-size: 18px; margin-top: 20px;">Follow us on Social Media</p><div style="display:flex; margin-top: 10px; margin-bottom: 30px;"><div style="display:flex; margin:auto"><a href="https://www.facebook.com/cookieacademymm" target="blank"><img alt="facebook" height="32" src="https://i.imgur.com/on4VXmE.png" style="display:block; height:auto; padding-right: 25px; border:0;" title="Facebook" width="32" /></a><a href="#" target="blank"><img alt="instagram" height="32" src="https://i.imgur.com/TRncuPi.png" style="display:block; padding-right:25px; height:auto; border:0;" title="Instagram" width="32" /></a><a href="https://discord.com/invite/sMfdX4Pvz5" target="blank"><img alt="discord" height="32"src="https://i.imgur.com/B1rsYUF.png" style="display:block; height:auto; border:0;" title="Discord"width="32" /></a></div></div><div style="max-width: 75%; font-family: 'Roboto'; font-weight: 300; font-size: 15px; color: black; margin: 20px auto;"><p style="text-align: center;">Thank You for registering our Knowledge Sharing Session about Medicine Pathway. Make sure that you’re joining the link at the exact time as the announcement. We would appreciate it if you let us know whether you will be attending the Session or not.</p></div><a style="text-decoration:none; color:white; font-size:14px; padding:10px 15px;background-color:#2f57be; border-radius:10px;"href="#">Join Webinar</a>
    <div style=" font-family: 'Roboto' ; font-weight: 300; font-size: 13px; color: #7a7a7a; padding-top: 20px; padding-bottom: 35px;"><p style="margin: 3px;">Email: cookieacademy19@gmail.com</p><p style="margin: 3px;">Public Relation Department</p><p style="margin: 3px;">Cookie Academy © 2021</p></div></div></div></div></div></div>
</body>
"""]


def send_mail(content):
    yag = yagmail.SMTP("cookieacademy19@gmail.com")
    yag.send(to="goddess.gs13@gmail.com", subject="pr html test", contents=content)
    print("success")

if __name__ == "__main__":
    send_mail(content)