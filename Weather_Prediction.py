from tkinter import *
from tkinter import ttk
import requests



def data_get(): 


        city = city_name.get()
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=1b3537245f6d8cf3f1d87bdae9149a9a").json()
        w_label_1.config(text=data["weather"][0]["main"])
        wb_label_1.config(text=data["weather"][0]["description"])
        temp_label_1.config(text=str(data["main"]["temp"]-273.15))
        pre_label_1.config(text=data["main"]["pressure"])


win = Tk ()
win.title("Know Your weather")
win.config(bg="light blue")
win.geometry("500x570")


name_label = Label(win, text= "Weather Today ", font =("Times New Roman", 22, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()

list_name=  ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar",
"Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]


com = ttk.Combobox(win, text= "Weather Predicted By The GOAT",values =list_name, font =("Times New Roman", 15, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)


w_label = Label(win, text= "Weather Climate", font =("Bahnschrift Condensed", 15))
w_label.place(x=25, y=260, height=50, width=210)  

w_label_1 = Label(win, text= "", font =("Bahnschrift Condensed", 15))
w_label_1.place(x=250, y=260, height=50, width=210)  


wb_label = Label(win, text= "Weather Description", font =("Bahnschrift Condensed", 15))
wb_label.place(x=25, y=330, height=50, width=210)

wb_label_1 = Label(win, text= "", font =("Bahnschrift Condensed", 15))
wb_label_1.place(x=250, y=330, height=50, width=210)


temp_label = Label(win, text= "Temperature", font =("Bahnschrift Condensed", 15))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label_1 = Label(win, text= "", font =("Bahnschrift Condensed", 15))
temp_label_1.place(x=250, y=400, height=50, width=210)


pre_label = Label(win, text= "Pressure", font =("Bahnschrift Condensed", 15))
pre_label.place(x=25, y=470, height=50, width=210)

pre_label_1 = Label(win, text= "", font =("Bahnschrift Condensed", 15))
pre_label_1.place(x=250, y=470, height=50, width=210)



done_button =Button(win, text= "Done", font =("Times New Roman", 20, "bold"), command=data_get)
done_button.place(y=190 , height=50 , width=100 , x=200)




win.mainloop()
