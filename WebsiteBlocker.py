 #importing the required modules
import datetime
import time


#Copying the hosts file path
#In case of Windows. the path is
# C:\Windows\System32\drivers\etc\host
# In UNIX based systems, Linux, Mac, etc
# Just cd \etc\ and you can view the hosts file
# by the following command: cat hosts
#variable redirect that will redirect to the
#following website. In this case, dishant.me
redirect = "127.0.0.1"

#blocked websites list
websites_list = ["www.facebook.com", "fb.com", "facebook.com", "9gag.com", "www.9gag.com", "youtube.com"]
#from_time = 8
#to_time = 16
#Keeps running, Infinite loop!
while True:
#We write the condition here. checks time
#every 10 seconds, time.sleep(10)
#In python, datetime.datetime (that is datetime object of datetime class)
#has attributes of year, month, day, hour, minute, second, microsecond order
#To specify from what time we need the blocker on, we specify the hour in both
#arguments provided below
    if (datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, 8) < datetime.datetime.now() < datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, 20)) == True:
        print ('Websites are blocked during the working hours...')
        #r+ is a mode in file operation where in we can read a file as well as
        #write in a file.
        with open(r'/etc/host', 'r+') as file:
            data = file.read()
            for i in websites_list:
                if i in data:
                    pass
                else:
                    file.write(redirect + "\t" + i + "\n")


            #time.sleep(10)
    else:
        with open(r'/etc/host', 'r+') as file:
            data = file.readlines()
            #file.seek(0) makes the file object pointer at the beginning of the document of the file
            file.seek(0)
            for content in data:
                if not any(website in content for website in websites_list):
                    file.write(content)
            file.truncate()
        print ('You are free to visit any website you want!')
    time.sleep(60)
