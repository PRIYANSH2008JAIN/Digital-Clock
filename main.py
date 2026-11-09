# DEGITAL CLOCK

from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%H")
    mi = time.strftime("%M")
    sec = time.strftime("%S")
    am = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")








    year = time.strftime("%y")
    day = time.strftime("%a")
     

    leb_hr.config(text = hr)
    leb_min.config(text = mi)
    leb_sec.config(text = sec)
    leb_am.config(text = am)

    leb_date.config(text = date)

    leb_mo.config(text = month)
    leb_year.config(text = year)
    leb_day.config(text = day)




    leb_hr.after(200,date_time)


clock = Tk()
clock.title(" **Degital Clock**")
clock.geometry("1000x500")
clock.config(bg="pink")

#************* time


leb_hr=Label(clock,text="00",font=("Time new Roman",60,"bold"),
             bg="black",fg="white")
leb_hr.place(x=100,y=40,height=100,width=100)
leb_hr_txt=Label(clock,text="Hours",font=("Time new Roman",19,"bold"),
             bg="black",fg="white")
leb_hr_txt.place(x=100,y=200,height=30,width=100)





leb_min=Label(clock,text="00",font=("Time new Roman",60,"bold"),
             bg="black",fg="white")
leb_min.place(x=310,y=40,height=100,width=100)
leb_min_txt=Label(clock,text="Min.",font=("Time new Roman",18,"bold"),
             bg="black",fg="white")
leb_min_txt.place(x=310,y=200,height=30,width=100)




leb_sec=Label(clock,text="00",font=("Time new Roman",60,"bold"),
             bg="black",fg="white")
leb_sec.place(x=520,y=40,height=100,width=100)
leb_sec_txt=Label(clock,text="Sec.",font=("Time new Roman",18,"bold"),
             bg="black",fg="white")
leb_sec_txt.place(x=520,y=200,height=30,width=100)



leb_am=Label(clock,text="00",font=("Time new Roman",47,"bold"),
             bg="black",fg="white")
leb_am.place(x=730,y=40,height=100,width=100)
leb_am_txt=Label(clock,text="AM/PM",font=("Time new Roman",17,"bold"),
             bg="black",fg="white")
leb_am_txt.place(x=730,y=200,height=30,width=100)


#******** date 


leb_date=Label(clock,text="00",font=("Time new Roman",60,"bold"),
             bg="black",fg="white")
leb_date.place(x=100,y=280,height=100,width=100)

leb_date_txt=Label(clock,text="Date",font=("Time new Roman",19,"bold"),
             bg="black",fg="white")
leb_date_txt.place(x=100,y=440,height=30,width=100)



leb_mo=Label(clock,text="00",font=("Time new Roman",60,"bold"),
             bg="black",fg="white")
leb_mo.place(x=310,y=280,height=100,width=100)

leb_mo_txt=Label(clock,text="Month",font=("Time new Roman",19,"bold"),
             bg="black",fg="white")
leb_mo_txt.place(x=310,y=440,height=30,width=100)




leb_year=Label(clock,text="00",font=("Time new Roman",60,"bold"),
             bg="black",fg="white")
leb_year.place(x=520,y=280,height=100,width=100)
leb_year_txt=Label(clock,text="year",font=("Time new Roman",18,"bold"),
             bg="black",fg="white")
leb_year_txt.place(x=520,y=440,height=30,width=100)


leb_day=Label(clock,text="00",font=("Time new Roman",35,"bold"),
             bg="black",fg="white")
leb_day.place(x=730,y=280,height=100,width=100)
leb_day_txt=Label(clock,text="Day",font=("Time new Roman",17,"bold"),
             bg="black",fg="white")
leb_day_txt.place(x=730,y=440,height=30,width=100)







date_time()


clock.mainloop()
