from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    Climate_label1.config(text=data["weather"][0]["main"])
    desc_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    press_label1.config(text=data["main"]["pressure"])





win = Tk()

win.title("Weather checker")
win.config(bg = 'pink')
win.geometry("500x570")

name_label = Label(win,text="Weather checker",
                       font = ('Times new Roman',30,"bold"))
name_label.place(x = 25 , y = 50, height=50 ,width=450)

city_name = StringVar()
list_names = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text = 'Weather checker' ,values=list_names,
                       font = ('Times new Roman',20,"bold"),textvariable=city_name)
com.place(x= 25 , y = 120, height=50 ,width=450)



Climate_label = Label(win,text="Weather Climate",
                       font = ('Times new Roman',20))
Climate_label.place(x = 25 , y = 260, height=50 ,width=210)

Climate_label1 = Label(win,text="",
                       font = ('Times new Roman',20))
Climate_label1.place(x = 250 , y = 260, height=50 ,width=210)

desc_label = Label(win,text="Weather Description",
                       font = ('Times new Roman',17))
desc_label.place(x = 25 , y = 330, height=50 ,width=210)

desc_label1 = Label(win,text="",
                       font = ('Times new Roman',20))
desc_label1.place(x = 250 , y = 330, height=50 ,width=210)

temp_label = Label(win,text="Weather temperature",
                       font = ('Times new Roman',17))
temp_label.place(x = 25 , y = 400, height=50 ,width=210)

temp_label1 = Label(win,text="",
                       font = ('Times new Roman',20))
temp_label1.place(x = 250 , y = 400, height=50 ,width=210)

press_label = Label(win,text="Weather pressure",
                       font = ('Times new Roman',17))
press_label.place(x = 25 , y = 470, height=50 ,width=210)

press_label1 = Label(win,text="",
                       font = ('Times new Roman',17))
press_label1.place(x = 250 , y = 470, height=50 ,width=210)


done_button = Button(win,text="Confirm",
                       font = ('Times new Roman',20,"bold"),command=data_get)

done_button.place(y= 190 , height=50, width=100 , x= 200)



win.mainloop()