import time
import tkinter as tk
import webbrowser
from threading import *
from tkinter.tix import ScrolledWindow


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






def start_all_cameras():
    for link in links:
        print(link[1])
        threading_all_detections(link[1])
        time.sleep(1)
    print()



def threading_all_detections(text):
    x = text.split("https://www.youtube.com/watch?v=")
    if x[0] is '' and len(x) is 2:
        t2 = Thread(target=retrieve_input, kwargs=dict(text=text))
        t2.start()
    else:
        print('nevalid')

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


i = 5
j = 6
x = 2
list_text_box = []
list_label_text = []
links = []


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
        x = 3

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

        self.button_start_all = tk.Button(self, text='Click Here To All Cameras',
                                          command=lambda: start_all_cameras()
                                          )
        self.button_start_all.config(height=1, width=30, bg='grey', font=("Helvetica", 12))
        self.button_start_all.pack()

        self.label_text = tk.Label(self, text='Introduceti linkul camerei de supravegheat')
        self.label_text.config(font=("Helvetica", 12), padx='10', justify='left')
        self.label_text.pack()

        self.text_box1 = tk.Text(self, height=1, width=60)
        self.text_box1.config(font=("Helvetica", 12))
        self.text_box1.pack()

        self.label_text = tk.Label(self, text='Introduceti numele camerei de supravegheat')
        self.label_text.config(font=("Helvetica", 12), padx='10', justify='left')
        self.label_text.pack()

        self.text_box2 = tk.Text(self, height=1, width=60)
        self.text_box2.config(font=("Helvetica", 12))
        self.text_box2.pack()

        self.button_add = tk.Button(self, text='Click Here To Add',
                                    command=lambda: add_link(self.text_box1.get("1.0", "end-1c"),self.label_text1,self.text_box2.get("1.0", "end-1c"))
                                    )


        # threading_detections(self.text_box.get("1.0", "end-1c"),
        #                      self.error_message, self.hint_message)
        global i
        self.button_add.config(height=1, width=30, bg='grey', font=("Helvetica", 12))
        self.button_add.pack()

        self.label_text1 = tk.Label(self, text='')
        self.label_text1.config(font=("Helvetica", 12), padx='10', justify='left')
        self.label_text1.pack()


        self.label_text = tk.Label(self, text='Stergeti linkul')
        self.label_text.config(font=("Helvetica", 12), padx='10', justify='left')
        self.label_text.pack()

        self.text_box = tk.Text(self, height=1, width=60)
        self.text_box.config(font=("Helvetica", 12))
        self.text_box.pack()


        def add_link(lbl_link, lbl_dynamic, lbl_name):
            global links
            # print(lbl_link)
            gasit_nume = 0
            gasit_link = 0
            # print(lbl_name)
            # f = open('free_spaces_cameras/parking_cameras.txt', 'r')
            for link in links:
                print(link[0])
                if link[0] == lbl_name:
                    gasit_nume = 1
                # print(gasit_nume)
                if link[1] == lbl_link:
                    gasit_link = 1
            if lbl_link == '' or lbl_name == '':
                print('please add valid text')
                lbl_dynamic.configure(text='Textul introdus este invalid', bg='red')
            elif gasit_nume is 1:
                print('please add valid text')
                lbl_dynamic.configure(text='Acest nume este deja utilizat!', bg='red')
            elif gasit_link is 1:
                print('please add valid text')
                lbl_dynamic.configure(text='Acest link este deja utilizat!', bg='red')
            else:

                lbl_dynamic.configure(text='Linkul introdus este corect', bg='green')
                f = open('parking_data/parking_cameras.txt', 'a')
                # print(lbl_link)
                lbl_add = lbl_name + ' = ' + lbl_link
                # print(lbl_add)
                f.write('\n' + lbl_add)
                f.close()

                f = open('parking_data/parking_cameras.txt', 'r')
                lines = f.readlines()
                lines[-1] = lines[-1].split(' = ')
                links.append(lines[-1])
                print(links)



                self.text_label.config(font=("Helvetica", 12), text='\n'.join(map(str, Extract1(links))))
                self.text_label2.config(font=("Helvetica", 12), text='\n'.join(map(str, Extract2(links))))

        def remove_link(lbl1,lbl2):
            if lbl1 == '':
                print('please add valid text')
                lbl2.configure(text='Textul introdus este invalid', bg='red')
            else:
                lbl2.configure(text='Textul introdus este corect', bg='green')
                for link in links:
                    if lbl1 == link[0]:




                        print('este egal lol')
                        links.remove(link)
                        print(links)
                        self.text_label.config(font=("Helvetica", 12), text='\n'.join(map(str, Extract1(links))))
                        self.text_label2.config(font=("Helvetica", 12), text='\n'.join(map(str, Extract2(links))))

                        with open('parking_data/parking_cameras.txt','r+') as f:
                            lines = f.readlines()
                            f.seek(0)
                            for line in lines:
                                if lbl1 not in line :
                                    print(line)
                                    f.write(line)
                            f.truncate()





        self.button_remove = tk.Button(self, text='Click Here To Remove',
                                    command=lambda: remove_link(self.text_box.get("1.0", "end-1c"),self.label_text2)
                                    )
        self.button_remove.config(height=1, width=30, bg='grey', font=("Helvetica", 12))
        self.button_remove.pack()

        self.label_text2 = tk.Label(self, text='')
        self.label_text2.config(font=("Helvetica", 12), padx='10', justify='left')
        self.label_text2.pack()


        self.error_message = tk.Label(self, text='')
        self.error_message.config(font=("Helvetica", 12), padx='10')
        self.error_message.pack()

        self.hint_message = tk.Label(self, text='')
        self.hint_message.config(font=("Helvetica", 12), padx='10')
        self.hint_message.pack()

        f = open('parking_data/parking_cameras.txt', 'r')
        lines = f.readlines()
        global links
        for line in lines:
            line = line.rstrip('\n')
            line = line.split(' = ')
            links.append(line)
        print(links)
        # links_showed = list(list(zip(*lst))[0]
        def Extract1(lst):
            return list(list(zip(*lst))[0])
        def Extract2(lst):
            return list(list(zip(*lst))[1])

        self.text_labeld = tk.Label(self)
        self.text_labeld.config(padx='50',anchor='n', justify='left', font=("Helvetica", 12),)
        self.text_labeld.pack(side='left', fill='y')
        self.text_label = tk.Label(self)
        self.text_label.config(anchor='n',justify='left',font=("Helvetica", 12), text='\n'.join(map(str, Extract1(links))))
        self.text_label.pack(side='left',fill='y')

        self.scrollbar = tk.Scrollbar(self, orient="vertical")

        # Pack the scroll bar
        # Place it to the right side, using tk.RIGHT



        self.text_label2 = tk.Label(self)
        self.text_label2.config(padx=20,anchor='n', justify='left', font=("Helvetica", 12), text='\n'.join(map(str, Extract2(links))))
        self.text_label2.pack(side='left',fill='y')

        # self.canvas = tk.Canvas(self,width=300, height=300, bg='white')
        # self.canvas.pack(expand='yes', fill='both')






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
    root.wm_geometry("1100x800")

    root.mainloop()
