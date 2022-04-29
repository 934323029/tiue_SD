import tkinter as tk
from tkinter import*

class SampleAPP(tk.Tk):
    def __init__(self,*arg,**kwargs):
        tk.Tk.__init__(self,*arg,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        for F in (StartPage,UserPage,RegPage,tovarPage,trimolPage,stramol,sinipar,):
            page_name=F.__name__
            frame=F(parent=container,controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky="nsew")
            self.show_frame("StartPage")
    def show_frame(self,page_name):
        frame=self.frames[page_name]
        frame.tkraise()
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        #self.PhotoImae
        #self.config (bg=black)
        self.controller=controller
        self.controller.title("Pharmacy")
        self.controller.state('zoomed')

        label_welcome=tk.Label(self,text='Asiya  Online Pharmacy ', font = ('Bahnschrift SemiBold',60,'bold'),
                               fg='black',bg= 'red')
        label_welcome.pack(pady=10)
        login_label=tk.Label(self,text='1. Entry Login', font = ('Bahnschrift SemiBold',20,'bold'),
                               fg='black',bg= 'red')
        login_label.pack(pady=10)
        password_label = tk.Label(self, text='2. Entry Passwords', font=('Bahnschrift SemiBold', 20, 'bold'),
                                  fg='black',bg= 'red')
        password_label.pack(pady=10)
        my_login=tk.StringVar()
        login_entry = tk.Entry(self, textvariable=my_login, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        login_entry.pack(pady=10)
        my_password=tk.StringVar()
        password_entry=tk.Entry(self,textvariable=my_password, font = ('Bahnschrift SemiBold',30,'bold'),fg='black')
        password_entry.pack(pady=20)
        def check_login():
            if my_login.get()=='RRR' and my_password.get()=='123':
                controller.show_frame('UserPage')
                """right_label=tk.Label(self,text='Entry correct password',font = ('Bahnschrift SemiBold',30,'bold'),fg='black')
                right_label.pack()"""
            else:
                right_label['text']="Login or password error"
        logpass_button = tk.Button(self, text='Login', command=check_login,font=('Bahnschrift SemiBold', 30, 'bold'), fg='black',bg= 'red')
        logpass_button.pack(pady=10)
        right_label = tk.Label(self,font=('Bahnschrift SemiBold', 30, 'bold'),fg='black')
        right_label.pack(pady=30)

        def reg_profil():
            controller.show_frame('RegPage')
        reg_button=tk.Button(self,text="Create an account",command=reg_profil,font=('Bahnschrift SemiBold', 10, 'bold'), fg='black',bg= 'red')
        reg_button.pack()

    def backGroundImage(self, file):
        pass


class UserPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        #
        self.controller = controller
        def menu():
            controller.show_frame('tovarPage')
        red_button=tk.Button(self,text="PRODUCT",command=menu,font=('Bahnschrift SemiBold', 30, 'bold'), fg='black',bg= 'red')
        red_button.pack(pady=10)

        def menu():
            controller.show_frame('tovarPage')
        red_button=tk.Button(self,text="SEARCH FOR PILLS",command=menu,font=('Bahnschrift SemiBold', 30, 'bold'), fg='black',bg= 'red')
        red_button.pack(pady=10)
        def menu():
            controller.show_frame('tovarPage')
        red_button=tk.Button(self,text="BASKET",command=menu,font=('Bahnschrift SemiBold', 30, 'bold'), fg='black',bg= 'red')
        red_button.pack(pady=10)

        def return_page():

            controller.show_frame('StartPage')

        return_button = tk.Button(self, text='BACK', command=return_page, font=('Bernard MT Condensed', 15, 'bold'),
                                  bg='whitema')
        return_button.pack(pady=10)


class RegPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #
        self.controller = controller

        login2_label = tk.Label(self, text='Create a login', font=('Bahnschrift SemiBold', 30, 'bold'),
                                fg='black',bg='red')
        login2_label.pack(pady=30)
        my_login2 = tk.StringVar()
        login_entry2 = tk.Entry(self, textvariable=my_login2, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        login_entry2.pack(pady=30)
        password2_label = tk.Label(self, text='Create a password', font=('Bahnschrift SemiBold', 30, 'bold'),
                                   fg='black',bg='red')
        password2_label.pack(pady=30)
        my_password2 = tk.StringVar()
        password_entry2 = tk.Entry(self, textvariable=my_password2, font=('Bahnschrift SemiBold', 30, 'bold'),
                                   fg='white',)
        password_entry2.pack(pady=30)

        def sox_profil():
            controller.show_frame('UserPage')

        return_button = tk.Button(self, text='Save', command=sox_profil,font=('Bernard MT Condensed', 15, 'bold')
                                  ,bg='yellow')
        return_button.pack(pady=10)

        def return_page():
            controller.show_frame('StartPage')

        return_button = tk.Button(self, text='Back', command=return_page, font=('Bernard MT Condensed', 15, 'bold'),
                                  bg='white')
        return_button.pack(pady=10)
class tovarPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       #
        self.controller = controller

        def trimol():
            controller.show_frame('trimolPage')

        trimol_button = tk.Button(self, text='Trimol', command=trimol, font=('Bernard MT Condensed', 15, 'bold'))
        trimol_button.pack(pady=10)
        def stramol():
            controller.show_frame('stramol')

        stramol_button =tk.Button(self, text='stramol', command= stramol, font=('Bernard MT Condensed', 15, 'bold'))
        stramol_button.pack(pady=10)

        def sinipar():
            controller.show_frame('sinipar')

        sinipar_button =tk.Button(self, text='sinipar', command= stramol, font=('Bernard MT Condensed', 15, 'bold'))
        sinipar_button.pack(pady=10)

        def teraflyu():
            controller.show_frame('teraflyu')

        teraflyu_button =tk.Button(self, text='teraflyu', command= stramol, font=('Bernard MT Condensed', 15, 'bold'))
        teraflyu_button.pack(pady=10)

        def taylonhot():
            controller.show_frame('taylonhot')

        taylonhot_button = tk.Button(self, text='taylonhot', command=stramol, font=('Bernard MT Condensed', 15, 'bold'))
        teraflyu_button.pack(pady=10)

        def aspirin():
            controller.show_frame('aspirin')

        aspirin_button = tk.Button(self, text='aspirin', command=stramol, font=('Bernard MT Condensed', 15, 'bold'))
        teraflyu_button.pack(pady=10)

        def return_page():
            controller.show_frame('UserPage')

        return_button = tk.Button(self, text='Back', command=return_page, font=('Bernard MT Condensed', 15, 'bold'),
                                  bg='white')
        return_button.pack(pady=10)




class trimolPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #
        self.controller = controller

        f1 = tk.Label(self, text='Specify Quantity', font=('Bernard MT Condensed', 15, 'bold'))
        f1.pack(pady=10)
        ff1 = tk.Label(self, text='Payment', font=(15))
        ff1.pack(pady=10)
        f = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        f.pack(pady=20)
        ff = 7000

        def schet():
            summa = ff
            ff1.config(text=int(summa) * int(f.get()))

        kupit = tk.Button(self, text='Amount for the item', command=schet, font=('Bernard MT Condensed', 15, 'bold'))
        kupit.pack(pady=10)
        f2 = tk.Label(self, text='How many km or meter delivery write', font=('Bernard MT Condensed', 15, 'bold'))
        f2.pack(pady=10)
        ff2 = tk.Label(self, text='Payment', font=(15))
        ff2.pack(pady=10)
        km = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        km.pack(pady=20)
        rastoyanie = 9000

        def dostavka():
            summ = rastoyanie
            ff2.config(text=int(summ) * int(km.get()))

        dostavka_button = tk.Button(self, command=dostavka, text='Shipping cost',
                                    font=('Bernard MT Condensed', 15, 'bold'))
        dostavka_button.pack(pady=10)

        def return_page():
            controller.show_frame('tovarPage')

        return_button = tk.Button(self, text='back', command=return_page, font=('Bernard MT Condensed', 15, 'bold'),
                                  bg='red')
        return_button.pack(pady=10)
class stramol(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #
        self.controller = controller
        f1 = tk.Label(self, text='Enter quantity', font=('Bernard MT Condensed', 15, 'bold'))
        f1.pack(pady=10)
        ff1 = tk.Label(self, text='Payment', font=(15))
        ff1.pack(pady=10)
        f = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        f.pack(pady=20)
        ff = 5000

        def schet():
            summa = ff
            ff1.config(text=int(summa) * int(f.get()))

        kupit = tk.Button(self, text='Amount for the item', command=schet, font=('Bernard MT Condensed', 15, 'bold'))
        kupit.pack(pady=10)
        f2 = tk.Label(self, text='How many km or meter delivery write', font=('Bernard MT Condensed', 15, 'bold'))
        f2.pack(pady=10)
        ff2 = tk.Label(self, text='Payment', font=(15))
        ff2.pack(pady=10)
        km = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        km.pack(pady=20)
        rastoyanie = 9000

        def dostavka():
            summ = rastoyanie
            ff2.config(text=int(summ) * int(km.get()))

        dostavka_button = tk.Button(self, command=dostavka, text='Shipping cost',
                                    font=('Bernard MT Condensed', 15, 'bold'))
        dostavka_button.pack(pady=10)

        def return_page():
            controller.show_frame('tovarPage')

        return_button = tk.Button(self, text='back', command=return_page, font=('Bernard MT Condensed', 15, 'bold'),
                                  bg='white')
        return_button.pack(pady=10)

        def schet():
            summa = ff
            ff1.config(text=int(summa) * int(f.get()))

        class teraflyu(tk.Frame):
            def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                #
                self.controller = controller
                f1 = tk.Label(self, text='Shipping cost', font=('Bernard MT Condensed', 15, 'bold'))
                f1.pack(pady=10)
                ff1 = tk.Label(self, text='Payment', font=(15))
                ff1.pack(pady=10)
                f = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
                f.pack(pady=20)
                ff = 5000

                def schet():
                    summa = ff
                    ff1.config(text=int(summa) * int(f.get()))

                kupit = tk.Button(self, text='Amount for the item', command=schet,
                                  font=('Bernard MT Condensed', 15, 'bold'))
                kupit.pack(pady=10)
                f2 = tk.Label(self, text='How many km or meter delivery write', font=('Bernard MT Condensed', 15, 'bold'))
                f2.pack(pady=10)
                ff2 = tk.Label(self, text='Payment', font=(15))
                ff2.pack(pady=10)
                km = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
                km.pack(pady=20)
                rastoyanie = 9000

                def dostavka():
                    summ = rastoyanie
                    ff2.config(text=int(summ) * int(km.get()))

                dostavka_button = tk.Button(self, command=dostavka, text='shipping cost',
                                            font=('Bernard MT Condensed', 15, 'bold'))
                dostavka_button.pack(pady=10)

                def return_page():
                    controller.show_frame('tovarPage')

                return_button = tk.Button(self, text='back', command=return_page,
                                          font=('Bernard MT Condensed', 15, 'bold'),
                                          bg='white')
                return_button.pack(pady=10)
#
                def return_page():
                    controller.show_frame('tovarPage')

                return_button = tk.Button(self, text='back', command=return_page,
                                          font=('Bernard MT Condensed', 15, 'bold'),
                                          bg='white')
                return_button.pack(pady=10)



class sinipar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f1 = tk.Label(self, text='Enter quantity', font=('Bernard MT Condensed', 15, 'bold'))
        f1.pack(pady=10)
        ff1 = tk.Label(self, text='Payment', font=(15))
        ff1.pack(pady=10)
        f = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        f.pack(pady=20)
        ff = 5000

        def schet():
            summa = ff
            ff1.config(text=int(summa) * int(f.get()))

        kupit = tk.Button(self, text='Amount for the item', command=schet, font=('Bernard MT Condensed', 15, 'bold'))
        kupit.pack(pady=10)
        f2 = tk.Label(self, text='How many km or meter delivery write', font=('Bernard MT Condensed', 15, 'bold'))
        f2.pack(pady=10)
        ff2 = tk.Label(self, text='Payment', font=(15))
        ff2.pack(pady=10)
        km = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        km.pack(pady=20)
        rastoyanie = 9000

        def dostavka():
            summ = rastoyanie
            ff2.config(text=int(summ) * int(km.get()))

        dostavka_button = tk.Button(self, command=dostavka, text='shipping cost',
                                    font=('Bernard MT Condensed', 15, 'bold'))
        dostavka_button.pack(pady=10)

        def return_page():
            controller.show_frame('tovarPage')

        return_button = tk.Button(self, text='Back', command=return_page, font=('Bernard MT Condensed', 15, 'bold'),
                                  bg='white')
        return_button.pack(pady=10)




if __name__=="__main__":
    app=SampleAPP()
    app.geometry('600x500')
    app.mainloop()
