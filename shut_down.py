from tkinter import *
import os

def restart_btn():
    os.system('shutdown /r /t 1')
def restart_time_btn():
    os.system('shutdown /r /t 20')
def shutdown_btn():
    os.system('shutdown /s /t 1')
def logout_btn():
    os.system('shutdown -1')

soft = Tk()
soft.title('Shut Down App')
soft.geometry('500x500')

restart_button = Button(master=soft, text='Restart', command=restart_btn)
restart_button.grid(row=0, column=0, padx=20, pady=20)

shutdown_button = Button(master=soft, text='Shut Down', command=shutdown_btn)
shutdown_button.grid(row=1, column=0, padx=20, pady=20)

restart_time_button = Button(master=soft, text='Restart Time', command=restart_time_btn)
restart_time_button.grid(row=2, column=0, padx=20, pady=20)

logout_button = Button(master=soft, text='Log Out', command=logout_btn)
logout_button.grid(row=3, column=0, padx=20, pady=20)

soft.mainloop()