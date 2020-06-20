import time 
from datetime import datetime as dt 
  
# change hosts path according to your OS 
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
# localhost's IP 
redirect = "127.0.0.1"
  
# websites That you want to block 
block_list = ["www.facebook.com","facebook.com", 
      "dub119.mail.live.com","www.dub119.mail.live.com", 
      "www.gmail.com","gmail.com"] 
  
while True: 
  
    # time of your work 
    if (dt.now().hour,dt.now().minute) > (18,0): # Currently Set to be active till the clock shows 06 in the evening. Change the Time as per requiremets in the format (hours,minutes). It should be in 24 hours format.
        print("Working hours...") 
        with open(hosts_path, 'r+') as file: 
            content = file.read() 
            for site in block_list: 
                if site in content: 
                    pass
                else: 
                    # mapping hostnames to your localhost IP address 
                    file.write(redirect + " " + site + "\n") 
    else: 
        with open(hosts_path, 'r+') as file: 
            content=file.readlines() 
            file.seek(0) 
            for line in content: 
                if not any(site in line for site in block_list): 
                    file.write(line) 
  
            # removing hostnmes from host file 
            file.truncate() 
  
        print("Fun hours...") 
    time.sleep(5) 