from tkinter import *





def display():

    if ((x.get() == 1 ) and  (aa.get()==1) and  (ii.get()==1) and (hh1.get()==1) and (hh11.get()==1) and (y.get()==0) and (z.get()==0)):

        #role ="Your suitable role is cloud support Engineer"



        label_role = Label(frame, text="Your suitable role is cloud support Engineer")

        label_role.pack(side="bottom")



        #print(" Your suitable role is cloud support Engineer")

    elif ((y.get() == 1) and  (ff.get()==1) and  (ii.get()==1) and (kk.get() ==1) and (ii2.get()==1) and (hh11.get()==1) and (x.get()==0) and (z.get()==0)):



        label_role = Label(frame, text="Your suitable role is Product Manager")

        label_role.pack(side="bottom")

        #Product Manager

    elif ((z.get() == 1) and (dd.get()==1) and  (jj.get()==1) and (ee.get()==1) and  (jj3.get()==1) and (jj33.get()==1) and (x.get()==0) and (y.get()==0)):

        #print("Your suitable role is Devops Engineer")

         label_role = Label(frame, text="Your suitable role is DevOps Engineer")

         label_role.pack(side="bottom")

    elif ((z.get() == 1) and (dd.get() == 1) and (jj.get() == 1) and (ee.get() == 1) and (jj3.get() == 1) and (jj33.get() == 1) and (x.get() == 0) and (y.get() == 0)):

    # print("Your suitable role is Devops Engineer")

         label_role = Label(frame, text="Your suitable role is DevOps Engineer")

         label_role.pack(side="bottom")

def display_role(role):

    label_role = Label(frame, text=role)

    label_role.pack(side="bottom")





window = Tk()

window.title('Welcome to cloud career Planner')



canvas=Canvas(window ,height=700 ,width= 800)

canvas.pack()

role = ""





frame=Frame(window ,bg ='blue')

frame.place(relx=0.1 ,rely=0.1 ,relwidth=0.8 ,relheight=0.8)



framecodelevl=Frame(frame ,bg ='yellow')

framecodelevl.place(relx=0.05 ,rely=0.2 ,relwidth=0.2 ,relheight=0.55)



framebsm=Frame(frame ,bg ='green')

framebsm.place(relx=0.25,rely=0.2 ,relwidth=0.2 ,relheight=0.55)



frameexp=Frame(frame ,bg ='orange')

frameexp.place(relx=0.45 ,rely=0.2 ,relwidth=0.2 ,relheight=0.55)



framecert=Frame(frame ,bg ='purple')

framecert.place(relx=0.65,rely=0.2 ,relwidth=0.2 ,relheight=0.55)



Tops=Frame(frame, width = 150, height =10,bd=10,relief="flat")

Tops.pack(side=TOP)

lblInfo= Label(Tops, font=("times",14,'bold') ,text=" Your Cloud career planner" ,bd=5,anchor="w"   )

lblInfo.grid(row=0,column=0)





x = IntVar()

y = IntVar()

z = IntVar()

checkbox1 = Checkbutton(framecodelevl, text='Beginners', variable=x, onvalue=1, offvalue=0, command=display)

checkbox2 = Checkbutton(framecodelevl, text='Intermediate', variable=y, onvalue=1, offvalue=0, command=display)

checkbox3 = Checkbutton(framecodelevl, text='Advanced', variable=z, onvalue=1, offvalue=0, command=display)

checkbox1.pack()

checkbox2.pack()

checkbox3.pack()



"""

checkbox1.config(padx=5,pady=10)

checkbox1.config(anchor='w')

checkbox1.config(padx=5,pady=10,width=250,height=50)

checkbox2.config(padx=5,pady=10,anchor='w',width=250,height=50)

checkbox3.config(padx=5,pady=10,anchor='w',width=250,height=50)



"""

aa = IntVar()

bb = IntVar()

cc = IntVar()

dd = IntVar()

ee = IntVar()

ff = IntVar()

gg = IntVar()

hh = IntVar()

ii = IntVar()

jj = IntVar()

kk = IntVar()

ll = IntVar()

checkbox11 = Checkbutton(framebsm, text='Persistence', variable=aa, onvalue=1, offvalue=0, command=display)

checkbox22 = Checkbutton(framebsm, text='Adaptability', variable=bb, onvalue=1, offvalue=0, command=display)

checkbox33 = Checkbutton(framebsm, text='Future Orientation', variable=cc, onvalue=1, offvalue=0, command=display)

checkbox44 = Checkbutton(framebsm, text='orientation to detail', variable=dd, onvalue=1, offvalue=0, command=display)

checkbox55 = Checkbutton(framebsm, text='Problem solving', variable=ee, onvalue=1, offvalue=0, command=display)

checkbox66 = Checkbutton(framebsm, text='Customer oriented', variable=ff, onvalue=1, offvalue=0, command=display)

checkbox77 = Checkbutton(framebsm, text='Big picture', variable=gg, onvalue=1, offvalue=0, command=display)

checkbox88 = Checkbutton(framebsm, text='Conscientious', variable=hh, onvalue=1, offvalue=0, command=display)

checkbox99 = Checkbutton(framebsm, text='Eff Comm', variable=ii, onvalue=1, offvalue=0, command=display)

checkbox111 = Checkbutton(framebsm, text='Team oriented', variable=jj, onvalue=1, offvalue=0, command=display)

checkbox222 = Checkbutton(framebsm, text='Critical thinking', variable=kk, onvalue=1, offvalue=0, command=display)

checkbox333 = Checkbutton(framebsm, text='Growth mindset', variable=ll, onvalue=1, offvalue=0, command=display)



checkbox11.pack()

checkbox22.pack()

checkbox33.pack()

checkbox44.pack()

checkbox55.pack()

checkbox66.pack()

checkbox77.pack()

checkbox88.pack()

checkbox99.pack()

checkbox111.pack()

checkbox222.pack()

checkbox333.pack()



"""Experience check boxes """

hh1 = IntVar()

ii2 = IntVar()

jj3 = IntVar()

kk4 = IntVar()



checkbox111 = Checkbutton(frameexp, text='No Experience', variable=hh1, onvalue=1, offvalue=0, command=display)

checkbox222 = Checkbutton(frameexp, text='0-2 years', variable=ii2, onvalue=1, offvalue=0, command=display)

checkbox333 = Checkbutton(frameexp, text='2-5 years', variable=jj3, onvalue=1, offvalue=0, command=display)

checkbox444 = Checkbutton(frameexp, text='5+ years', variable=kk4, onvalue=1, offvalue=0, command=display)



checkbox111.pack()

checkbox222.pack()

checkbox333.pack()

checkbox444.pack()



""" Check boxes for Certifications """



hh11 = IntVar()

ii22 = IntVar()

jj33 = IntVar()

kk44 = IntVar()

ll33 = IntVar()

mm44 = IntVar()



checkbox1111 = Checkbutton(framecert, text='AZ-900', variable=hh11, onvalue=1, offvalue=0, command=display)

checkbox2222 = Checkbutton(framecert, text='AZ-104', variable=ii22, onvalue=1, offvalue=0, command=display)

checkbox3333 = Checkbutton(framecert, text='AZ-204', variable=jj33, onvalue=1, offvalue=0, command=display)

checkbox4444 = Checkbutton(framecert, text='AZ-303', variable=kk44, onvalue=1, offvalue=0, command=display)

checkbox5555 = Checkbutton(framecert, text='AZ-304', variable=ll33, onvalue=1, offvalue=0, command=display)

checkbox6666 = Checkbutton(framecert, text='AZ-400', variable=mm44, onvalue=1, offvalue=0, command=display)



checkbox1111.pack()

checkbox2222.pack()

checkbox3333.pack()

checkbox4444.pack()

checkbox5555.pack()

checkbox6666.pack()





button1 = Button(frame, text='my career',bg ='orange',command=display)

button1.pack(side="bottom")



window.mainloop()