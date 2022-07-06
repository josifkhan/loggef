




from os import uname as u
from sys import exit as e
import time,os
#colors
r="\033[1;33m"
re="\033[0;37m"
g="\033[1;32m"
e="\033[1;0m"
os.system('clear')
print(f"""
                     OFFICIAL ANOUNCEMENTS{r}
        >>'LOGGEF' WILL BE REMOVED ON '15 July - 2022'<<{g}
                     <<HOPE YOU ENJOYED!>>
                         {re}Md Josif Khan

{e}""")
time.sleep(5)
if 'aarch64' in str(u()[4]):
    import loggef
elif 'arm' in str(u()[4]):
    import loggef32
else:
    print("System not supported")
    e()