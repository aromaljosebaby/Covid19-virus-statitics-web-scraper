#from Tkinter import *
from tkinter import *

from bs4 import  BeautifulSoup
import requests
data=[]


def geting_data(country_name):
      info_list=[]
      responce = requests.get('https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/')
      soup = BeautifulSoup(responce.text, 'html.parser')
      data_iterator = iter(soup.find_all('td'))

      while True:
            #countries = {}
            try:
                  country = next(data_iterator).text
                  confirmed_cases = next(data_iterator).text
                  deaths = next(data_iterator).text

                  #countries[country] = [country, confirmed_cases, deaths]
                  data.append(country)
                  data.append(confirmed_cases)
                  data.append(deaths)

            except StopIteration:

                  break
      print(data)


      for i in range(0,len(data)):
            if(data[i]==country_name):
                  info_list.append(data[i])
                  info_list.append(data[i+1])
                  info_list.append(data[i+2])
      print(info_list)
      return info_list


def displaying(country_name):

      info_list=geting_data(country_name)


      '''name='Brazil'
      for i in data:
          if(i.get(name,None)):
              info_list=i.get(name)
              print(info_list[0])'''


      root.destroy()
      win = Tk()
      #info_list=['lol','lolo']
      win.geometry('800x650')
      win.config(bg='black')
      #Label(win, text='Confirmed Cases', font=('Verdana', 13), fg='black', bg='SeaGreen1',
            #padx=10, pady=10, relief=RAISED).place(x=100, y=200)



      Label(win, text=info_list[0], font=('Verdana', 13), fg='black', bg='SeaGreen1', padx=10,
                              pady=10, relief=RAISED).place(x=360, y=60)
      Label(win, text='Confirmed Cases', font=('Verdana', 13), fg='black', bg='IndianRed1',
                              padx=10, pady=10, relief=RAISED).place(x=200, y=200)
      Label(win, text='Deaths', font=('Verdana', 13), fg='black', bg='OrangeRed2',
                              padx=50, pady=10, relief=RAISED).place(x=390, y=200)

      Label(win, text=info_list[1], font=('Verdana', 13), fg='black', bg='thistle1',
            padx=50, pady=10, relief=RAISED).place(x=200, y=300)

      Label(win, text=info_list[2], font=('Verdana', 13), fg='black', bg='thistle3',
            padx=50, pady=10, relief=RAISED).place(x=390, y=300)


      win.mainloop()




#main menu

root=Tk()
root.geometry('800x650')
logo = PhotoImage(file='images/farmer - Copy.gif')
root.config(bg='black')
Label(root, text='Corona Count', font=('Verdana', 30), fg='white', bg='black').pack(side=TOP, pady=10)

# Button(root,text='i need this plz',image=logo).pack(side=TOP)
Label(root, text='Snake n Ladder', font=('Andalus', 20, 'bold'), bg='black', fg='light blue', pady=50,
      image=logo).pack(side=TOP)

country_name_label=Label(root, text='Enter Country Name', font=('Verdana', 13), fg='black', bg='SeaGreen1',padx=10,pady=10,relief=RAISED).place(x=280,y=200)
country_name=Entry(root,font=('Verdana',13),bg='White',fg="black",relief=RAISED)
country_name.place(x=280,y=300)
find_button=Button(root,font=('Verdana',13),bg='DeepSkyBLue3',fg='Black',text=' Find ',command=lambda : displaying(country_name.get())).place(x=350,y=400)
root.mainloop()



