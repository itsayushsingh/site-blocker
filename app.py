import time
from datetime import datetime as dt

hosts_path="hosts_new"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","fb.com","fb.me"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
#        print("Working Hours xD")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
#        print("Fun Hours :D")
         with open(hosts_path,'r+') as file:
             content=file.readlines()
             file.seek(0)
             for line in content:
                 if not any(website in line for website in website_list):
                     file.write(line)
             file.truncate()
    time.sleep(5)
