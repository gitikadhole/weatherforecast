from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def getWeather():
    try:
        city=textfield.get()

        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        name.config(text="Current Weather")

        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=5d67330e48a37bcd78015b835f8917"
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","Feels","Like",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather Forecast","Invalid Entry")

root=Tk()
root.title("Weather Forecast")
root.geometry("900x500+300+200")
root.resizable(False,False)

#search box
Search_image=PhotoImage(file="C:/Users/Gitika Dhole/Downloads/noun-search-bar-1376433.png")
myimage=Label(image=Search_image)
myimage.place(x=10,y=20)

textfield = tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=150,y=50)
textfield.focus()

Search_icon=PhotoImage(file="C:/Users/Gitika Dhole/Downloads/9035054_search_circle_icon (1).png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",command=getWeather)
myimage_icon.place(x=540,y=40)

logo_image=PhotoImage(file="C:/Users/Gitika Dhole/Downloads/1530389_weather_clouds_storm_sunny_icon.png")
logo=Label(image=logo_image)
logo.place(x=50,y=120)

Frame_image=PhotoImage(file="C:/Users/Gitika Dhole/Downloads/SeekPng.com_blue-gradient-png_498283.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.place(x=60,y=360)

name=Label(root,font=("arial",20,"bold"))
name.place(x=420,y=150)
clock=Label(root,font=("Helvetica",20))
clock.place(x=420,y=180)

label1=Label(root,text="Wind",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=370)

label2=Label(root,text="Humidity",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=260,y=370)

label3=Label(root,text="Description",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=450,y=370)

label4=Label(root,text="Pressure",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=680,y=370)

t=Label(font=("arial",30,"bold"),fg="#ee666d")
t.place(x=420,y=210)
c=Label(font=("arial",15,"bold"))
c.place(x=420,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=130,y=400)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=290,y=400)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=490,y=400)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=710,y=400)
root.mainloop()
