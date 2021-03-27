import pywhatkit
number=input("Enter a number: ")
sms= input("Enter your sms: ")
hour=int(input())
min=int(input())
pywhatkit.sendwhatmsg(number,sms,hour,min)