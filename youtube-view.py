import time
import webbrowser
import os

url = str(input("Enter your video url in ->\"url here \"<-  : "))
n = input("Enter refresh rate(seconds) : ")
browser_default = input("Enter your default browser in ->\"browser here \"<-  : ")
while (1):
    os.system(" killall -9 " + browser_default)
    time.sleep(int(n))
    webbrowser.open(url)
    print('Successfully Viewed')
