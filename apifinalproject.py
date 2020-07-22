

#sys.path.append("/home/venkat/python_ project")
#api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon} 
import requests
from tkinter import *
import tkinter as tk
import csv
import matplotlib.pyplot as plt
from datetime import datetime
print("Hello")
print("This is the Weather project")
#cityname=input("Enter the city you want find the weather")
#######################################################

global x,y,w,c,we,temp_min,temp_max,wind_speed,humidity,pressure,ts,date


root=tk.Tk()
root.configure(background='grey')
#entry of string also, use of griad

def save():
    global cityname
    cityname=entry.get()
    print(cityname)
    

photo=PhotoImage(file="C:\\Users\\venkat\\Desktop\\pyth\\cartoon.gif")
#photo2=PhotoImage(file="dankmeme.gif")
#label2=Label(root,image=photo2)
label=Label(root, image=photo)
label.pack()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()  # <-- move focus to this widget

root.bind("<Escape>", lambda e: root.destroy())
    
city=Label(root,text="Enter the city",fg='green')

entry=Entry(root)
button=Button(root,text="Proceed",fg="red",command=save)
for_esc=Label(root,text="Press 'esc' to exit after clicking 'Proceed'")


city.pack()
entry.pack()
button.pack()
for_esc.pack()
#label2.pack()
root.mainloop()


root2=tk.Tk()
root2.configure(background='green')
garb="Not Available right now"
display_temp_min=StringVar()
display_temp_min.set(garb)
display_date=StringVar()
display_date.set(garb)
display_name=StringVar()
display_name.set(garb)
display_wind_speed=StringVar()
display_wind_speed.set(garb)
display_humidity=StringVar()
display_humidity.set(garb)
display_pressure=StringVar()
display_pressure.set(garb)
display_latitude=StringVar()
display_latitude.set(garb)
display_longitude=StringVar()
display_longitude.set(garb)
display_temp_max=StringVar()
display_temp_max.set(garb)
#function to act on cityname
global leng
def leng():
    
    r= requests.get("http://api.openweathermap.org/data/2.5/weather?appid=c9cc431a11c9bf05cc82aee6b6cc08dd&q="+cityname+"&units=metric")
# Print the status code of the response.
#print(r.json())
#Note: Need for api key c9cc431a11c9bf05cc82aee6b6cc08dd
    global x,y,w,c,we,temp_min,temp_max,wind_speed,humidity,pressure,ts,date
    
    x=r.json()
    if x['cod']!=0:
        
        y=x['main']
        w=x['wind']
        c=x['coord']
        display_name.set("The location is: "+str(x['name']))
        display_latitude.set("The Latitude is: "+str(c['lat']))
        display_longitude.set("The longitude is: "+str(c['lon']))
        we=x['weather']
        temp_min=y['temp_min']
        display_temp_min.set("This is the minimum temperature: "+str(temp_min)+"degree Celsius")
        temp_max=y['temp_max']
        display_temp_max.set("This is the maximum temperature: "+str(temp_max)+"degree Celsius")
        humidity=y['humidity']
        display_humidity.set("The humidity is: "+str(humidity)+"%")
        wind_speed=w['speed']
        lol=wind_speed
        display_wind_speed.set("The wind speed is "+str(lol))
        pressure=y['pressure']
        display_pressure.set("The pressure is: "+str(pressure))
        
        ts=int(x['dt'])
        date=(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d '))
        display_date.set("The date today is: "+str(date))
        
        
        print("This weather has been recorded on ",date)
        print("The location entered is ",x['name'])
        print("This place has coordinates as longitude ",c['lon']," and latitude of ",c['lat'])
        print("Minimum temperature today is ",temp_min," degree celsius")
        print("Wind Speed today is ",wind_speed," mph")
        print("The humidity today is ",humidity," percent")
        print("The pressure today is ",pressure)
        #myData = [["date","minimum temp", "maximum temp", "wind speed","humidity","pressure"]]  
        myData1=[[date,temp_min,temp_max,wind_speed,humidity,pressure]]
        myFile = open("C:\\Users\\venkat\\Desktop\\pyth\\weather.csv", 'a',newline='')  
        with myFile as csvfile:  
            writer = csv.writer(myFile)
            writer.writerows(myData1)
        
        csvfile.close()
    
    else:
        print("Sorry the entered city does not exist")    

ko=Button(root2,text="Would you like to know the weather, please click me!",command=leng)

root2.overrideredirect(True)
root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
root2.focus_set()  # <-- move focus to this widgetla
root2.bind("<Escape>", lambda f: root2.destroy())

loc_label2=Label(root2,textvariable=display_date,fg='red')
loc_label=Label(root2,textvariable=display_temp_min,fg='blue')
loc_label3=Label(root2,textvariable=display_name,fg='orange red')
loc_label4=Label(root2,textvariable=display_latitude,fg='deep sky blue')
loc_label5=Label(root2,textvariable=display_longitude,fg='gold2')
loc_label6=Label(root2,textvariable=display_temp_max,fg='HotPink2')
loc_label7=Label(root2,textvariable=display_wind_speed,fg='black')
loc_label8=Label(root2,textvariable=display_humidity,fg='maroon4')
loc_label9=Label(root2,textvariable=display_pressure,fg='cyan2')


def humidity_function():
    x=[]
    y=[]
        
        
    with open('C:\\Users\\venkat\\Desktop\\pyth\\weather.csv', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append((row[0]))
            y.append(float(row[3]))



    plt.plot(x,y, marker='o')
    plt.title('Data from the CSV File: date and humidity')
      
    plt.xlabel('date')
    plt.ylabel('humididty')

    
    plt.show()

def max_temp_function():
    x=[]
    y=[]

    with open('C:\\Users\\venkat\\Desktop\\pyth\\weather.csv', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append((row[0]))
            y.append(float(row[2]))
           


    plt.plot(x,y, marker='o')

    plt.title('Data from the CSV File: date and maximum temperature')

    plt.xlabel('date')
    plt.ylabel('maximum temp in centigrade')
     
    def P():
        plt.show()

def min_temp_function():
      x=[]
      y=[]
        

      with open('C:\\Users\\venkat\\Desktop\\pyth\\weather.csv', 'r') as csvfile:
          plots= csv.reader(csvfile, delimiter=',')
          for row in plots:
                  x.append((row[0]))
                  y.append(float(row[1]))
               


      plt.plot(x,y, marker='o')
       
      plt.title('Data from the CSV File: date and minimum temperature')

      plt.xlabel('date')
      plt.ylabel('minimum temp in centigrade')
       
      def P():
    
          plt.show()

def pressure_function():    
    x=[]
    y=[]
        

    with open('C:\\Users\\venkat\\Desktop\\pyth\\weather.csv') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append((row[0]))
            y.append(float(row[4]))



    plt.plot(x,y, marker='o')

    plt.title('Data from the CSV File: date and pressure')

    plt.xlabel('date')
    plt.ylabel('pressure in pascals')
     
    
    plt.show()

def wind_speed_function():
    x=[]
    y=[]


    with open('C:\\Users\\venkat\\Desktop\\pyth\\weather.csv', 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append((row[0]))
            y.append(float(row[3]))



    plt.plot(x,y, marker='o')

    plt.title('Data from the CSV File: date and windspeed')

    plt.xlabel('date')
    plt.ylabel('windspeed')
     
    def P():
        plt.show()

button1=Button(root2,text="humidty grapgh, click me",command=humidity_function)
button2=Button(root2,text="maximum temperature grapgh, click me",command=max_temp_function)
button3=Button(root2,text="minimum temperature, click me",command=min_temp_function)
button4=Button(root2,text="pressure grapgh, click me",command=pressure_function)
button5=Button(root2,text="windspeed grapgh, click me",command=wind_speed_function)
quitlabel=Label(root2,text="text esc to quit",fg='red')
ko.pack()
loc_label3.pack()
loc_label2.pack()
loc_label4.pack()
loc_label5.pack()
loc_label.pack()
loc_label6.pack()
loc_label7.pack()
loc_label8.pack()
loc_label9.pack()

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
quitlabel.pack()
root2.mainloop()
#############################





















