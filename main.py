from tkinter import *
from tkinter import ttk
import requests

window = Tk()
window.title("Weather App")
window.minsize(width=540,height=360)
window.config(bg="skyblue", padx=30,pady=30)
# photo = PhotoImage(file="weather1.png")
# Label(window,image=photo).pack()


def get_weather_data():
    text = city_name.get()
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={text}&appid=3b9bfec8aee83b002af691e207be944f").json()
    city_n.config(text=data["name"])
    city_weather_.config(text=data["weather"][0]["main"])
    weather_d.config(text=data["weather"][0]["description"])
    temp_m.config(text=int(data["main"]["temp_min"]-273.15))
    temp_max.config(text=int(data["main"]["temp_max"]-273.15))
    pressure.config(text=data["main"]["pressure"])
    humidity.config(text=data["main"]["humidity"])
    wind.config(text=f"{data['wind']['speed']} mph")


name = Label(text="Welcome to the world",font=("Arial",20,"normal"), bg="skyblue", width=30)
name.grid(column=0, row=0, columnspan=4)

list_of_dist = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name = StringVar()
com = ttk.Combobox(values=list_of_dist, width=30,font=("Arial",13,"normal"),textvariable=city_name)
com.grid(column=0, row=1,columnspan=4,pady=20)

city = Label(text="City Name",font=("Arial",13,"normal"), bg="skyblue")
city.grid(column=0, row=2)
city_n = Label(text = "",font=("Arial",13,"normal"),bg="skyblue")
city_n.grid(column=2,row=2,columnspan=2)
#
city_weather = Label(text="Weather",font=("Arial",13,"normal"), bg="skyblue")
city_weather.grid(column=0, row=3)
city_weather_ = Label(text = "",font=("Arial",13,"normal"),bg="skyblue")
city_weather_.grid(column=2,row=3,columnspan=2)
#
weather_description = Label(text="Weather Description",font=("Arial",13,"normal"), bg="skyblue")
weather_description.grid(column=0, row=4)
weather_d = Label(text = "",font=("Arial",13,"normal"),bg="skyblue")
weather_d.grid(column=2,row=4,columnspan=2)

city_temperature = Label(text="Temperature",font=("Arial",13,"normal"), bg="skyblue")
city_temperature.grid(column=0, row=5,rowspan=2)
min_temp = Label(text="Min.",font=("Arial",13,"normal"), bg="skyblue")
min_temp.grid(column=2, row=5)
temp_m = Label(text = "",font=("Arial",13,"normal"),bg="skyblue")
temp_m.grid(column=2,row=6)
max_temp = Label(text="Max.",font=("Arial",13,"normal"), bg="skyblue")
max_temp.grid(column=3, row=5)
temp_max = Label(text = "",font=("Arial",13,"normal"),bg="skyblue")
temp_max.grid(column=3,row=6)

city_pressure = Label(text="Pressure",font=("Arial",13,"normal"), bg="skyblue")
city_pressure.grid(column=0, row=7)
pressure = Label(text = "",font=("Arial",13,"normal"),bg="skyblue")
pressure.grid(column=2,row=7,columnspan=2)

city_humidity = Label(text="Humidity",font=("Arial",13,"normal"), bg="skyblue")
city_humidity.grid(column=0, row=8)
humidity = Label(text = "",font=("Arial",13,"normal"),bg="skyblue")
humidity.grid(column=2,row=8,columnspan=2)

city_wind = Label(text="Wind Speed",font=("Arial",13,"normal"), bg="skyblue")
city_wind.grid(column=0, row=9)
wind = Label(text = "",font=("Arial",13,"normal"),bg="skyblue")
wind.grid(column=2,row=9,columnspan=2)

for colon in range(2,10):
    if colon == 5:
        rowspan = 2
        col = Label(text=":",bg="skyblue")
        col.grid(column=1,row=colon,rowspan=rowspan)
    elif colon == 6:
        pass
    else:
        col = Label(text=":",bg="skyblue")
        col.grid(column=1, row=colon)

done = Button(text="Done",font=("Arial",13,"normal"),width=6, command=get_weather_data)
done.grid(column=3,row=1)


window.mainloop()