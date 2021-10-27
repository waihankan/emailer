#!/usr/bin/python3


# This is the test file for developers !!! Do NOT use this file. 

import yagmail

content = ["""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link href="https://fonts.googleapis.com/css2?family=Roboto" rel="stylesheet" type="text/css"><title>Congratulations!</title></head>
<body>
    <div style="font-family:'Roboto'; box-shadow: rgb(212, 212, 212) 4px 4px; background-color:rgb(255, 255, 255); color: black; max-width: 500px; margin:auto; border: 2px solid #253a6d;"><div style="text-align:center; margin-top: 25px"><img style="width: 100%; max-width: 100px;" src="https://i.imgur.com/jfyuaOh.png" alt="cookie-logo" /><h1 style="font-family: 'Roboto'; font-weight: 300; margin: 25px 0px 10px 0px; color: #cc080f">WELCOME ABOARD!</h1><p style="margin: 0px; font-size: 19px; font-family: 'Roboto'; font-weight: 300; color: rgb(143, 143, 143);">You have been selected</p><img style=" padding-top: 20px; width: 100%; max-width: 80px;" src="https://i.imgur.com/TeE5qHf.png" alt="balloon" /><div style="max-width: 70%; font-family: 'Roboto'; font-weight: 300; font-size: 15px; color: black; margin: 20px auto;">
    <p style=text-align: center;>Dear Applicant,</p><p style="text-align: center; color:black"><i>Congratulations!</i> This email is to formally offer you a volunteering job for Cookie Academy. We strongly believe that your skills and expertise will help our organization to reach great heights.We are looking forward to working with you. Please contact me in case of any queries.</p></div>    
    <div style="display: flex;"><div style="display: flex; margin:auto; background-color: #2f57be; border-radius: 15px; padding: 4px 9px;"><a href="https://discord.com/invite/sMfdX4Pvz5" target="blank"><img alt="discord" height="32" src="https://i.imgur.com/kvuAayt.png" style="display:block; height:auto; border:0;" title="Discord" width="32" /></a><a style="margin-left: 5px;padding-top: 6px;text-decoration: none; color: white; font-size: 14px;" href="https://discord.com/invite/sMfdX4Pvz5" target="blank">Join Our Discord Channel</a></div></div><div style=" font-family: 'Roboto' ; font-weight: 300; font-size: 13px; color: #7a7a7a; padding-top: 30px; padding-bottom: 35px;"><p style="margin: 3px;">Email: cookieacademy19@gmail.com</p><p style="margin: 3px;">Human Resource Department</p><p style="margin: 3px;">Cookie Academy © 2021</p></div></div></div></div></div></div>
</body>
</html>
"""]

def send_mail(content):
    yag = yagmail.SMTP("cookieacademy19@gmail.com")
    yag.send(to="goddess.gs13@gmail.com", subject="welcome test", contents=content)
    print("success")

if __name__ == "__main__":
    send_mail(content)
