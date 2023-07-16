# I-tracler Install/////////
green="\033[0;32m"        # Green
import os
os.system('clear')
import os
import sys
import time
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
delay_print(green+'%37s' % '   INSTALL....\n')
print()
os.system('sudo su')
os.system('pip install termcolor')
os.system('pip install colorama')
os.system('chmod +x *')
os.system('apt upgrade & update -y')
os.system('apt install figlet -y')
os.system('apt install ruby -y')
os.system('gem install lolcat')
os.system('pkg install whois -y')
os.system('pkg install termux-api -y')
os.system('apt install make -y')
os.system('make install')
os.system('source start-truecallerjs.sh')
os.system('sv-enable truecallerjs')
os.system('sv up truecallerjs')
os.system('python3 track.py')