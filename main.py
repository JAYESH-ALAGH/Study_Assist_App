from tkinter import *
from datetime import datetime
from tkinter import messagebox
from Chat_Bot import chatbot_final
from PIL import ImageTk, Image
from TEXT_TO_SPEECH import Text_To_Speech
from speech__recognition import speech_to_text
from tkinter.font import Font




greybg = '#e0e0e0'
greyfg = '#636363'
darkgrey = '#3d3d3d'
red = '#ff3030'
blue = '#4733ff'
lightblue = '#7566ff'
green = '#56ff4a'
fontbig=('Arial, 16')
bluegrey = '#484f63'
font_small = ('Arial, 13')
font_big = ('Arial, 16')
bot= 'Study Assist'
timetable_entry_bg = '#fff'
timetablebg = greybg
timetablefg = greyfg
bg = '#f7f7ff'



counter = 66600
running = False
def counter_label(label):
    def count():
        if running:
            global counter
            tt = datetime.fromtimestamp(counter)
            string = tt.strftime("%H:%M:%S")
            display=string

            studytime_time_label['text']=display

            label.after(1000, count)
            counter += 1


    count()


def Start(label):
    global running
    running=True
    counter_label(label)
    time_start['state']='disabled'
    time_stop['state']='normal'
    reset['state']='normal'


def Stop():
    global running
    time_start['state']='normal'
    time_stop['state']='disabled'
    reset['state']='normal'
    running = False

def Reset(label):
    global counter
    counter=66600

    # If rest is pressed after pressing stop.
    if running==False:
        reset['state']='disabled'
        label['text']='00:00:00'

    # If reset is pressed while the stopwatch is running.
    else:
        label['text']='00:00:00'



def newTask(Event):
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        task_list_file = open('task_list.txt', 'a')
        task_list_file.write('\n'+task)
        task_list_file.close()
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():

    task_list_file = open('task_list.txt', 'r')
    tasklist = task_list_file.readlines()
    task_list_file.close()
    dlttask = lb.get(ANCHOR)
    tasklist.remove(dlttask)
    taskfile = open('task_list.txt', 'w')
    taskfile.writelines(tasklist)
    taskfile.close()
    lb.delete(ANCHOR)


def clear_default_task(Event):
    my_entry.delete(0, END)



def enter_pressed(event):
    msg = msg_box.get()
    insert_msg(msg, 'You')

def insert_msg(msg, sender):
    if not msg:
        return
    msg_box.delete(0, END)
    msg_sender = f'{sender}: {msg}\n\n'
    text_widget.configure(cursor='arrow', state=NORMAL)
    text_widget.insert(END, msg_sender)
    text_widget.configure(cursor='arrow', state=DISABLED)
    global incoming
    incoming = chatbot_final(msg)
    msg_bot = f'{bot}: {incoming}\n\n'
    text_widget.configure(cursor='arrow', state=NORMAL)
    text_widget.insert(END, msg_bot)
    text_widget.configure(cursor='arrow', state=DISABLED)

    text_widget.see(END)

def read_pressed(event):
    global incoming
    Text_To_Speech(incoming)

def speech_text(speech):
    value = speech_to_text()
    if value == "Sorry! Could not understand\nPlease try again":
        msg_bot = f'{bot}: {value}\n\n'
        text_widget.configure(cursor='arrow', state=NORMAL)
        text_widget.insert(END, msg_bot)
        text_widget.configure(cursor='arrow', state=DISABLED)

        text_widget.see(END)
    elif value == "Please check your Internet connection":
        msg_bot = f'{bot}: {value}\n\n'
        text_widget.configure(cursor='arrow', state=NORMAL)
        text_widget.insert(END, msg_bot)
        text_widget.configure(cursor='arrow', state=DISABLED)

        text_widget.see(END)
    else:
        insert_msg(value, 'You')






assistant_state = False

def assistant_appear():
    global assistant_state
    if assistant_state == True:
        chatbot_label.place_forget()
        assistant_state = False
    else:
        chatbot_label.place(relwidth=0.265, relx = 0.7, rely=0.15, relheight=0.7)
        assistant_state = True

def changeOnHover(button, colorOnHover, colorOnLeave):

    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))


root = Tk()
root.geometry('1920x1080')
root.title('Study Assist')
root.state('zoomed')
root.iconbitmap('img/logo.ico')
root.configure(bg = bg)




heading_font = Font(family='Roboto', size='30', weight='normal')




main_menu= Menu(root)
root.config(menu=main_menu)
file_menu = Menu(main_menu)

class SubMenuSYSFunc():
    def About_Func():
        global About_pop
        global greybg
        global bluegrey

        About_pop = Toplevel(root)
        About_pop.title("About")
        About_pop.iconbitmap('img/logo.ico')

        About_pop.geometry('330x400')
        About_pop.resizable(width=False, height=False)
        About_pop.config(bg = greybg)

        Label_About_pop = Label(About_pop, text="Study Assist",fg = "#000000", bg=greybg,font = ("Roboto", 23) )
        Label_About_pop.place(relwidth=1)
        Label_Text_1 = Label(About_pop, text="The base motive of the Study Assist App \n is to increase the rate of time\n management and mind concentration skills in\n students which will further increase\n their success rate in both studies \nand physical activities, making \nthem all-rounder champions",fg = "#000000", bg=greybg,font = ("Roboto", 9) )
        Label_Text_1.place(rely=0.2, relwidth = 1)
        Label_Text_2= Label(About_pop, text = "copyright © 2021 Jayesh Alagh & Harshwardhan\nThis Program Comes With ABSOLUTELY NO WARRANTY\nMADE BY: Jayesh Alagh & Harshwardhan\nLinkedIN: Jayesh Alagh\nE-Mail: jayeshalagh@gmail.com\nharschwardhan@gmail.com\nPh No.: 8826272872, 8527626285",fg = "#000000", bg=greybg,font = ("Roboto", 9))
        Label_Text_2.place(rely=0.5, relwidth = 1)
        Label_Text_3= Label(About_pop, text = "Version: 1.0.1",fg = "#000000", bg=greybg,font = ("Roboto", 9))
        Label_Text_3.place(rely=0.8, relwidth = 1)

        Button_About_pop = Button(About_pop, text="OK", command= About_pop.destroy, height=1, width=10, fg = bluegrey, bg=greybg)
        Button_About_pop.place(rely=0.9,relx = 0.37)

main_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='About', command = SubMenuSYSFunc.About_Func)
file_menu.add_command(label='Exit', command = root.quit)


goodmorning = Label(root, text = 'Good Morning!', fg = bluegrey, font =('Verdana, 30'), bg = bg)
goodmorning.place(relx = 0.02, rely = 0.01)


timetable_bg_label = Label(root, bg = timetablebg)

timetable_bg_label.place(relwidth=0.25, rely = 0.14, relx = 0.05, relheight= 0.75)

timetable_entry1 = Entry(timetable_bg_label, bg = timetable_entry_bg, font=fontbig, fg = timetablefg)
timetable_entry1.place(relwidth = 0.98, relx = 0.01, rely = 0.05, relheight= 0.11)
timetable_entry1.insert(0,'8:00-10:00 ~ School Classes')

timetable_entry2 = Entry(timetable_bg_label, bg = timetable_entry_bg, font=fontbig, fg = timetablefg)
timetable_entry2.place(relwidth = 0.98, relx = 0.01, rely = 0.16, relheight= 0.11)
timetable_entry2.insert(0,'10:00-10:30 ~ Break')

timetable_entry3 = Entry(timetable_bg_label, bg = timetable_entry_bg, font=fontbig, fg = timetablefg)
timetable_entry3.place(relwidth = 0.98, relx = 0.01, rely = 0.27, relheight= 0.11)
timetable_entry3.insert(0,'10:30-01:00 ~ School Classes')

timetable_entry4 = Entry(timetable_bg_label, bg = timetable_entry_bg, font=fontbig, fg = timetablefg)
timetable_entry4.place(relwidth = 0.98, relx = 0.01, rely = 0.38, relheight= 0.11)
timetable_entry4.insert(0,'01:00-03:00 ~ Recreation')

timetable_entry5 = Entry(timetable_bg_label, bg = timetable_entry_bg, font=fontbig, fg = timetablefg)
timetable_entry5.place(relwidth = 0.98, relx = 0.01, rely = 0.49, relheight= 0.11)
timetable_entry5.insert(0,'03:00-07:00 ~ Self-Studies')

timetable_entry6 = Entry(timetable_bg_label, bg = timetable_entry_bg, font=fontbig, fg = timetablefg)
timetable_entry6.place(relwidth = 0.98, relx = 0.01, rely = 0.6, relheight= 0.11)
timetable_entry6.insert(0,'07:00-08:30 ~ Sports')

timetable_entry7 = Entry(timetable_bg_label, bg = timetable_entry_bg, font=fontbig, fg = timetablefg)
timetable_entry7.place(relwidth = 0.98, relx = 0.01, rely = 0.71, relheight= 0.11)
timetable_entry7.insert(0,'08:30-09:30 ~ Dinner')

timetable_entry8 = Entry(timetable_bg_label, bg = timetable_entry_bg, font=fontbig, fg = timetablefg)
timetable_entry8.place(relwidth = 0.98, relx = 0.01, rely = 0.82, relheight= 0.11)
timetable_entry8.insert(0,'09:30-11:30 ~ Revision')

timetable_heading = Label(root, bg = timetablebg, font=fontbig, text = 'Today', fg = bluegrey)
timetable_heading.place(relwidth = 0.25, rely = 0.1, relx = 0.05, relheight = 0.05)




studytracker = Label(root, bg = '#f0f0f0')
studytracker.place(relwidth = 0.15, relheight = 0.3, relx = 0.375, rely = 0.1)

studytracker_label = Label(studytracker, text = 'Study Tracker', fg = bluegrey, font = fontbig, bg = '#f0f0f0')
studytracker_label.place(relwidth = 1)

studytime_time_label = Label(studytracker, fg = green, bg='#f0f0f0', text = '00:00:00', font = ('Roboto-Thin, 40'))
studytime_time_label.place(relheight=0.3, relwidth=1, rely = 0.15)

button_frame_studytimer = Frame(studytracker)
button_frame_studytimer.place(relwidth = 0.8, relheight = 0.2, rely = 0.55, relx = 0.1)

time_start = Button(button_frame_studytimer,text='Start',font=('Helvetica, 14'),bg=blue, relief = FLAT, fg = '#fff',bd=0, activebackground = lightblue, activeforeground = '#fff', command= lambda: Start(studytime_time_label))
time_start.pack(fill=BOTH, expand=True, side=LEFT)

time_stop = Button(button_frame_studytimer,text='Stop',font=('Helvetica, 14'),bg=blue, relief = FLAT, fg = '#fff',bd=0, activebackground = lightblue, activeforeground = '#fff', command=Stop)
time_stop.pack(fill=BOTH, expand=True, side=LEFT)

reset = Button(studytracker, text='Reset',width=6, state= 'disabled',command=lambda:Reset(studytime_time_label), bg = '#f0f0f0', fg = bluegrey, font = ('Arial, 11'), bd = 0, activebackground = '#f0f0f0', activeforeground=greyfg)
reset.place(relwidth = 1, rely = 0.75)


changeOnHover(time_start, '#7566ff' , blue)
changeOnHover(time_stop, '#7566ff' , blue)




sticky_label = Label(root, text = 'Stickies', fg = bluegrey, bg = bg, font = fontbig)
sticky_label.place(relwidth = 0.15, relx = 0.375, rely = 0.43 )

reminder_1 = Text(root, bg = '#faff6e',fg = bluegrey, font=('Vedana, 13'), relief=FLAT)
reminder_1.place(relwidth = 0.15, relheight = 0.2, relx = 0.375, rely = 0.48)
reminder_1.insert(END, '\n  Exam Monday\n\n   Chapter 3\n   Physics')

reminder_2 = Text(root, bg = '#faff6e',fg = bluegrey, font=('Verdana, 13'), relief=FLAT)
reminder_2.place(relwidth = 0.15, relheight = 0.2, relx = 0.375, rely = 0.72)




todo_list_bg = Label(root, bg = greybg)
todo_list_bg.place(relwidth=0.35, relheight=0.8, relx=0.6, rely=0.1)

todo_label = Label(todo_list_bg, text = 'To-Do List', bg = greybg, fg = bluegrey, font= fontbig)
todo_label.place(relwidth = 1, relheight = 0.1)

lb = Listbox(todo_list_bg,width=25,height=8,font=('Arial, 15'),bd=0,fg=darkgrey,highlightthickness=0,selectbackground=greybg,activestyle="none",bg = '#fff')
lb.place(relheight = 0.6, relwidth = 0.95, relx=0.025, rely = 0.29)

tasklist_file = open('task_list.txt', 'r')
task_list = tasklist_file.readlines()

tasklist_file.close()

for item in task_list:
    if item != '':
        lb.insert(END, item)


sb = Scrollbar(lb)
sb.place(relheight = 1, relwidth=0.05, relx = 0.95)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(todo_list_bg,font=('Helvetica', 15), fg = greyfg, relief=FLAT)
my_entry.place(rely = 0.1, relwidth = 0.95, relheight=0.08, relx = 0.025)

my_entry.bind('<Return>', newTask)
my_entry.insert(0, 'Enter task..')
my_entry.bind('<Button-1>', clear_default_task)

button_frame = Frame(todo_list_bg)
button_frame.place(rely = 0.18 , relwidth = 0.95, relheight = 0.1, relx = 0.025)



addTask_btn = Button(button_frame,text='+    Add Task',font=('Helvetica, 14'),bg='#fff',command=lambda: newTask(None), relief = FLAT, fg = blue, activebackground = greybg, activeforeground = blue, bd=0)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


delTask_btn = Button(button_frame,text='Delete',font=('Helvetica, 14'),bg='#fff',padx=20,pady=10,command=deleteTask, relief = FLAT, fg = red, activebackground = greybg, activeforeground = red, bd=0)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)




chatbot_label = Label(root, bg = '#a1a1a1')

text_widget = Text(chatbot_label, bg = '#fff', fg = 'black', font = font_small, padx = 5, pady = 5, relief=FLAT)
text_widget.place(relheight=0.9, relwidth=1)
text_widget.configure(cursor='arrow', state=DISABLED)

scrollbar = Scrollbar(text_widget)
scrollbar.place(relheight=1, relx=0.974)
scrollbar.configure(command=text_widget.yview)

bottom_label_chatbot = Label(chatbot_label, bg = '#a1a1a1', height= 10)
bottom_label_chatbot.place(relwidth=1, rely= 0.9, relheight = 0.1)


msg_box = Entry(bottom_label_chatbot, bg= '#fff', fg = '#000000', font=font_small, relief=FLAT)
msg_box.place(relwidth=0.41, relheight= 0.95, rely=0.01, relx=0.201)
msg_box.bind('<Return>', enter_pressed)


send_image = ImageTk.PhotoImage(file='img/send.ico')

send_button = Button(bottom_label_chatbot, image=send_image, bg = '#a1a1a1',bd=0, activebackground='#a1a1a1',relief=FLAT , command=lambda: enter_pressed(None))
send_button.place(relx=0.62, rely=0.01, relheight=0.95 , relwidth=0.18)

mic_image = ImageTk.PhotoImage(file='img/mic.ico')

mic_button = Button(bottom_label_chatbot, image=mic_image, bg = '#a1a1a1', relief=FLAT,bd=0, activebackground='#a1a1a1',command=lambda: speech_text(None))
mic_button.place(relx=0.011, rely= 0.01, relheight=0.95, relwidth=0.18)


speaker_image= ImageTk.PhotoImage(file='img/speaker.ico')

read_button = Button(bottom_label_chatbot, image=speaker_image, bg = '#a1a1a1',bd=0, activebackground='#a1a1a1',relief=FLAT, command= lambda: read_pressed(None))
read_button.place(relx=0.81, rely=0.01, relheight=0.95 , relwidth=0.18)


chat_img = ImageTk.PhotoImage(file='img/Chat.ico')

assistant_button = Button(root, image = chat_img, bg = bg, command= assistant_appear, bd = 0, activebackground = bg)
assistant_button.place(relwidth=0.04, relheight=0.07, relx = 0.95, rely = 0.9)

root.mainloop()
