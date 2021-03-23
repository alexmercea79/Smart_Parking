import tkinter as tk
import webbrowser
from threading import *


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


def threading_local_server(lbl, lbl2):
    # Call work function
    lbl.config(text="SERVER STATUS: Online", bg='green')
    lbl2.config(bg='green', state='disabled', disabledforeground="black", text='Serverul este pornit')
    t1 = Thread(target=start_local_server)
    t1.start()


def start_local_server():
    import LocalServer
    webbrowser.open('http://127.0.0.1:5000/sms', new=2)

    LocalServer.run_app()


def new_textBox(box, self=None):
    self.box = tk.Text(self, height=1, width=60)
    self.box.grid(row=5, column=2)
    self.box.config(font=("Helvetica", 12))


def threading_detections(text, lbl, lbl2):
    x = text.split("https://www.youtube.com/watch?v=")
    if x[0] is '' and len(x) is 2:
        lbl.config(text='Linkul introdus este corect!', bg='green')
        lbl2.config(text='')
        t2 = Thread(target=retrieve_input, kwargs=dict(text=text))
        t2.start()


    else:
        lbl.config(text='Linkul introdus este incorect!', bg='red')
        lbl2.config(text='Sugestie: Adaugati URL-ul complet al videoclipului!')


def retrieve_input(text):
    print('text= ' + text)
    import detections

    detections.threading_working(text)


def drawing():
    import detections

    detections.draw()

    # label = tk.Label(self, text="This is page 1")
    # label.pack(side="top", fill="both", expand=True)

i=5
j=6
x=2
list_text_box=[]
list_label_text=[]
class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.photo_bg = tk.PhotoImage(file="smart_parking_long.PNG")
        self.background_photo = tk.Label(self, image=self.photo_bg)
        self.background_photo.place(x=70, y=450)

        self.label_delimitare1 = tk.Label(self)
        self.label_delimitare1.grid(row=1, column=2, sticky='w')
        self.label_delimitare1.config(height=2, width=100)

        self.label_server_status = tk.Label(self, text='SERVER STATUS: Offline', bg='red')
        self.label_server_status.grid(row=0, column=2, sticky='w')
        self.label_server_status.config(font=("Helvetica", 12), padx='10', justify='left')

        self.label2 = tk.Label(self, text='Porniti serverul pentru a putea primi mesaje pe telefonul mobil')
        self.label2.grid(row=2, column=2)
        self.label2.config(font=("Helvetica", 12))

        self.label_delimitare2 = tk.Label(self)
        self.label_delimitare2.grid(row=4, column=2, sticky='w')
        self.label_delimitare2.config(height=2, width=100)

        self.button_start_server = tk.Button(self, text='Start Server',
                                             command=lambda: threading_local_server(self.label_server_status,
                                                                                    self.button_start_server))
        self.button_start_server.grid(row=3, column=2)
        self.button_start_server.config(bg='red', font=("Helvetica", 12), height=1, width=30, )

        self.label_text = tk.Label(self, text='Introduceti linkul camerei de supravegheat:')
        self.label_text.grid(row=4, column=2, padx=(0, 292))
        self.label_text.config(font=("Helvetica", 12), padx='10', justify='left')

        self.text_box = tk.Text(self, height=1, width=60)
        self.text_box.grid(row=5, column=2)
        self.text_box.config(font=("Helvetica", 12))
        x=3


        # def create_button():
        #     global i
        #
        #     self.text_box = tk.Text(self, height=1, width=60)
        #     self.text_box.grid(row=i+5, column=2)
        #     self.text_box.config(font=("Helvetica", 12))
        #     i=i+1
        #     print(i)

        self.button_start = tk.Button(self, text='Click Here To Start',
                                      command=lambda: threading_detections(self.text_box.get("1.0", "end-1c"),
                                                                           self.error_message, self.hint_message)
                                      )
        self.button_start.config(height=1, width=30, bg='grey', font=("Helvetica", 12))
        self.button_start.grid(row=6, column=2)

        # self.button_start2 = tk.Button(self, text='New line',
        #                               command=create_button
        #                               )
        # self.button_start2.config(height=1, width=30, bg='grey', font=("Helvetica", 12))
        # self.button_start2.grid(row=7, column=2)

        # self.scrollbar = tk.Scrollbar(root)
        # self.scrollbar.pack(side='right', fill='y')






        self.error_message = tk.Label(self, text='')
        self.error_message.grid(row=7, column=2)
        self.error_message.config(font=("Helvetica", 12), padx='10')

        self.hint_message = tk.Label(self, text='')
        self.hint_message.grid(row=8, column=2)
        self.hint_message.config(font=("Helvetica", 12), padx='10')

        self.button_rerun_schema = tk.Button(self, text='Schema de parcare noua', command=drawing, bg='gray')
        self.button_rerun_schema.grid(row=9, column=2)
        self.button_rerun_schema.config(font=("Helvetica", 12), height=1, width=30)

        self.button_iesire_program = tk.Button(self, text='Iesire Program', command=root.destroy)
        self.button_iesire_program.config(height=1, width=30, font=("Helvetica", 12))
        self.button_iesire_program.grid(row=10, column=2)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.photo_bg = tk.PhotoImage(file="smart_parking_long.PNG")
        self.background_photo = tk.Label(self, image=self.photo_bg)
        self.background_photo.place(x=70, y=450)





        self.label_text = tk.Label(self, text='Camera 1 '+ '(Introduceti linkul camerei de supravegheat)')
        self.label_text.grid(row=4, column=2, padx=(0, 292))
        self.label_text.config(font=("Helvetica", 12), padx='10', justify='left')

        self.text_box = tk.Text(self, height=1, width=60)
        self.text_box.grid(row=5, column=2)
        self.text_box.config(font=("Helvetica", 12))




        def create_button():
            global i,j,x,list_text_box,list_label_text

            self.label_text = tk.Label(self, text='Camera '+str(x)+ '(Introduceti linkul camerei de supravegheat)')
            self.label_text.grid(row=i, column=2, padx=(0, 292))
            self.label_text.config(font=("Helvetica", 12), padx='10', justify='left')
            i = i + 2
            list_label_text.append(self.label_text)


            self.text_box = tk.Text(self, height=1, width=60)
            self.text_box.grid(row=j, column=2)
            self.text_box.config(font=("Helvetica", 12))
            list_text_box.append(self.text_box)








            print(list_text_box)

            j= j+2
            print('i='+str(i))
            print('j=' + str(j))
            x+=1

        def destroy_element(lbl1,lbl2):
            global x,list_text_box,list_label_text

            lbl1.destroy()
            lbl2.destroy()

            list_label_text.pop()
            list_text_box.pop()
            print(list_text_box)
            print(lbl1)

            x-=1



        self.button_start = tk.Button(self, text='Click Here To Start',
                                      command=lambda: threading_detections(self.text_box.get("1.0", "end-1c"),
                                                                           self.error_message, self.hint_message)
                                      )
        global i
        self.button_start.config(height=1, width=30, bg='grey', font=("Helvetica", 12))
        self.button_start.grid(row=i+10, column=2)

        self.button_start2 = tk.Button(self, text='New line',
                                       command=create_button
                                       )
        self.button_start2.config(height=1, width=30, bg='grey', font=("Helvetica", 12))
        self.button_start2.grid(row=i+11, column=2)

        self.button_start3 = tk.Button(self, text='Destroy line',
                                       command=lambda: destroy_element(list_text_box[-1],list_label_text[-1])
                                       )
        self.button_start3.config(height=1, width=30, bg='grey', font=("Helvetica", 12))
        self.button_start3.grid(row=i+12, column=2)

        # self.scrollbar = tk.Scrollbar(root)
        # self.scrollbar.pack(side='right', fill='y')

        self.error_message = tk.Label(self, text='')
        self.error_message.grid(row=7, column=2)
        self.error_message.config(font=("Helvetica", 12), padx='10')

        self.hint_message = tk.Label(self, text='')
        self.hint_message.grid(row=8, column=2)
        self.hint_message.config(font=("Helvetica", 12), padx='10')






class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Program", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Multi-Parking", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()


    root.iconbitmap('smart_parking_short.ico')
    root.title('Smart Parking')

    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x800")
    root.mainloop()
