import sys
import json
import requests
import csv
import socket
from tkinter import *


def trigger_api(ip):
  querystring = {"ip": ip}
  url = "https://geo.ipify.org/api/v1?apiKey=at_LHZrfcs9aoOIVLAmHfZdyGOj9hzKW&ipAddress="+ip

  response =  requests.request('GET', 'http://ip-api.com/json/'+ip)

  if(200 == response.status_code):
    return json.loads(response.text)
  else:
    return None


root = Tk()
root.title('Geolocation Tracker')
root.geometry("800x500")

def location():
  ip=requests.get('https://api.ipify.org').text #public ip

  # print("Getting details for IP: " + ip+".....")
  l1.config(text="Getting details for IP: " + ip+".....")
  # print("Details:")
  l2.config(text="Details:")
  api_response = trigger_api(ip)
  
  for x in  api_response:

      print(x,":",api_response[x])

  l3.config(text='Status : ' + api_response['status'])
  l4.config(text='Country : ' + api_response['country'])
  l5.config(text='CountryCode : ' + api_response['countryCode'])
  l6.config(text='Region : ' + api_response['region'])
  l7.config(text='RegionName : ' + api_response['regionName'])
  l8.config(text='City : ' + api_response['city'])
  l9.config(text='Zip : ' + api_response['zip'])
  l10.config(text='LAT : ' + str(api_response['lat']))
  l11.config(text='LON : ' + str(api_response['lon']))
  l12.config(text='Timezone : ' + api_response['timezone'])
  l13.config(text='ISP : ' + api_response['isp'])
  l14.config(text='ORG : ' + api_response['org'])
  l15.config(text='AS : ' + api_response['as'])
  l16.config(text='Query : ' + api_response['query'])

#   status : success
# country : India
# countryCode : IN
# region : TN
# regionName : Tamil Nadu
# city : Chennai
# zip : 600004
# lat : 13.0878
# lon : 80.2785
# timezone : Asia/Kolkata
# isp : Hathway IP over Cable Internet Access
# org : Hathway Cable and Datacom Limited
# as : AS17488 Hathway IP Over Cable Internet
# query : 115.97.93.214

bg = PhotoImage(file="bg.png")

label=Label(root,image=bg)
label.place(x=0,y=0,relwidth=1,relheight=1)

button = Button(root, text="Click me to get your location!", padx=20, pady=10, command=location, bg='white')
button.pack()

l1 = Label(root,text="IP?",fg="white",bg="black")
l1.pack(pady=3)
l1.config(font=("Courier", 12))
l2 = Label(root,text="Details?",fg="white",bg="black")
l2.pack(pady=3)
l1.config(font=("Courier", 12))
l3 = Label(root,text="Status?",fg="white",bg="black")
l3.pack(pady=3)
l3.config(font=("Courier", 12))
l4 = Label(root,text="Country?",fg="white",bg="black")
l4.pack(pady=3)
l4.config(font=("Courier", 12))
l5 = Label(root,text="CountryCode?",fg="white",bg="black")
l5.pack(pady=3)
l5.config(font=("Courier", 12))
l6 = Label(root,text="Region?",fg="white",bg="black")
l6.pack(pady=3)
l6.config(font=("Courier", 12))
l7 = Label(root,text="RegionName?",fg="white",bg="black")
l7.pack(pady=3)
l7.config(font=("Courier", 12))
l8 = Label(root,text="City?",fg="white",bg="black")
l8.pack(pady=3)
l8.config(font=("Courier", 12))
l9 = Label(root,text="ZIP?",fg="white",bg="black")
l9.pack(pady=3)
l9.config(font=("Courier", 12))
l10 = Label(root,text="LAT?",fg="white",bg="black")
l10.pack(pady=3)
l10.config(font=("Courier", 12))
l11 = Label(root,text="LON?",fg="white",bg="black")
l11.pack(pady=3)
l11.config(font=("Courier", 12))
l12 = Label(root,text="Timezone?",fg="white",bg="black")
l12.pack(pady=3)
l11.config(font=("Courier", 12))
l13 = Label(root,text="ISP?",fg="white",bg="black")
l13.pack(pady=3)
l13.config(font=("Courier", 12))
l14 = Label(root,text="ORG?",fg="white",bg="black")
l14.pack(pady=3)
l14.config(font=("Courier", 12))
l15 = Label(root,text="AS?",fg="white",bg="black")
l15.pack(pady=3)
l15.config(font=("Courier", 12))
l16 = Label(root,text="Query?",fg="white",bg="black")
l16.pack(pady=3)
l16.config(font=("Courier", 12))

root.mainloop()


if __name__ == "__main__":
  # location()
  print("Check GUI")

print(socket.gethostbyname(socket.gethostname()))