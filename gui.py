import time
import tkinter as tk
from tkinter import ttk
import webbrowser
from threading import *


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


def threading_local_server(lbl, lbl2):
    lbl.config(text="SERVER STATUS: Online", bg='green')
    lbl2.config(bg='green', state='disabled', disabledforeground="black", text='Serverul este pornit')
    t1 = Thread(target=start_local_server)
    t1.start()


def start_local_server():
    import server
    webbrowser.open('http://127.0.0.1:5000/sms', new=2)

    server.run_app()


def start_all_cameras(lbl1, lbl2):
    if not links:
        lbl1.config(text='Lista camerelor este goala', bg='red')
        lbl2.config(text='Sfat: Va rugam introduceti o camera!')
    else:
        lbl1.config(text='Camerele sunt pornite!', bg='green')
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
        lbl2.config(text='Sugestie: Adăugați URL-ul complet al videoclipului!')


def retrieve_input(text):
    print('Text Input= ' + text)
    import detections

    detections.threading_working(text)


def drawing(text, lbl, lbl2):
    import detections
    x = text.split("https://www.youtube.com/watch?v=")
    if x[0] is '' and len(x) is 2:
        lbl.config(text='Linkul introdus este corect!', bg='green')
        lbl2.config(text='')
        detections.draw(text)

    else:
        lbl.config(text='Linkul introdus este incorect!', bg='red')
        lbl2.config(text='Sugestie: Adaugati URL-ul complet al videoclipului!')


links = []


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.photo_bg = tk.PhotoImage(file="smart_parking_long_e.PNG")
        self.background_photo = tk.Label(self, image=self.photo_bg)
        self.background_photo.place(x=200, y=480)

        self.label_delimitare1 = tk.Label(self)
        self.label_delimitare1.pack()
        self.label_delimitare1.config()

        self.label_server_status = tk.Label(self, text='SERVER STATUS: Offline', bg='red')
        self.label_server_status.pack(anchor='w')
        self.label_server_status.config(font=("Helvetica", 12), padx='10', justify='left')

        self.label2 = tk.Label(self, text='Porniți serverul pentru a putea primi mesaje pe telefonul mobil')
        self.label2.pack(anchor='w')
        self.label2.config(font=("Helvetica", 12))

        self.label_delimitare2 = tk.Label(self)
        self.label_delimitare2.pack()
        self.label_delimitare2.config(height=2, width=100)

        self.button_start_server = tk.Button(self, text='Pornire Server',
                                             command=lambda: threading_local_server(self.label_server_status,
                                                                                    self.button_start_server))
        self.button_start_server.pack()
        self.button_start_server.config(bg='red', font=("Helvetica", 12), height=1, width=30, )

        self.label_text = tk.Label(self, text='Introduceți linkul camerei de supravegheat:')
        self.label_text.pack()
        self.label_text.config(font=("Helvetica", 12), padx='10', justify='left')

        self.text_box = tk.Text(self, height=1, width=60)
        self.text_box.pack()
        self.text_box.config(font=("Helvetica", 12))

        self.label_delimitare3 = tk.Label(self)
        self.label_delimitare3.pack()
        self.label_delimitare3.config(height=1, width=100)

        self.button_start = tk.Button(self, text='Pornește Camera',
                                      command=lambda: threading_detections(self.text_box.get("1.0", "end-1c"),
                                                                           self.error_message, self.hint_message)
                                      )
        self.button_start.config(height=1, width=30, bg='grey', font=("Helvetica", 12))
        self.button_start.pack()

        self.button_rerun_schema = tk.Button(self, text='Schemă de Parcare Nouă',
                                             command=lambda: drawing(self.text_box.get("1.0", "end-1c"),
                                                                     self.error_message, self.hint_message), bg='gray')
        self.button_rerun_schema.pack()
        self.button_rerun_schema.config(font=("Helvetica", 12), height=1, width=30)

        self.error_message = tk.Label(self, text='')
        self.error_message.pack()
        self.error_message.config(font=("Helvetica", 12), padx='10')

        self.hint_message = tk.Label(self, text='')
        self.hint_message.pack()
        self.hint_message.config(font=("Helvetica", 12), padx='10')

        self.button_iesire_program = tk.Button(self, text='Ieșire Program', command=root.destroy)
        self.button_iesire_program.config(height=1, width=30, font=("Helvetica", 12))
        self.button_iesire_program.pack()


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # self.photo_bg = tk.PhotoImage(file="smart_parking_long.PNG")
        # self.background_photo = tk.Label(self, image=self.photo_bg)
        # self.background_photo.place(x=70, y=450)

        self.label_delimitare2 = tk.Label(self)
        self.label_delimitare2.pack()
        self.label_delimitare2.config(height=1, width=100)

        self.button_start_all = tk.Button(self, text='Pornește Toate Camerele',
                                          command=lambda: start_all_cameras(self.label_text3, self.label_text4)
                                          )
        self.button_start_all.config(height=1, width=30, bg='grey', font=("Helvetica", 12))
        self.button_start_all.pack()

        self.label_text3 = tk.Label(self, text='')
        self.label_text3.config(font=("Helvetica", 12), padx='10', justify='left')
        self.label_text3.pack()

        self.label_text4 = tk.Label(self, text='')
        self.label_text4.config(font=("Helvetica", 12), padx='10', justify='left')
        self.label_text4.pack()

        self.label_text = tk.Label(self, text='Introduceți linkul camerei de supravegheat')
        self.label_text.config(font=("Helvetica", 12), padx='10', justify='left')
        self.label_text.pack()

        self.text_box1 = tk.Text(self, height=1, width=60)
        self.text_box1.config(font=("Helvetica", 12))
        self.text_box1.pack()

        self.label_delimitare2 = tk.Label(self)
        self.label_delimitare2.pack()
        self.label_delimitare2.config(height=1, width=100)

        self.label_text = tk.Label(self, text='Introduceți numele camerei de supravegheat')
        self.label_text.config(font=("Helvetica", 12), padx='10', justify='left')
        self.label_text.pack()

        self.text_box2 = tk.Text(self, height=1, width=60)
        self.text_box2.config(font=("Helvetica", 12))
        self.text_box2.pack()

        self.button_add = tk.Button(self, text='Adaugă Camera',
                                    command=lambda: add_link(self.text_box1.get("1.0", "end-1c"), self.label_text1,
                                                             self.text_box2.get("1.0", "end-1c"), self.text_box1,
                                                             self.text_box2)
                                    )

        self.button_add.config(height=1, width=30, bg='grey', font=("Helvetica", 12))
        self.button_add.pack()

        self.label_text1 = tk.Label(self, text='')
        self.label_text1.config(font=("Helvetica", 12), padx='10', justify='left')
        self.label_text1.pack()

        self.label_text = tk.Label(self, text='Ștergeti numele camerei de supravegheat')
        self.label_text.config(font=("Helvetica", 12), padx='10', justify='left')
        self.label_text.pack()

        self.text_box = tk.Text(self, height=1, width=60)
        self.text_box.config(font=("Helvetica", 12))
        self.text_box.pack()

        def add_link(lbl_link, lbl_dynamic, lbl_name, lbl_clear_text, lbl_clear_link):
            global links
            # print(lbl_link)
            gasit_nume = 0
            gasit_link = 0
            # print(lbl_name)
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

                import re
                y = re.search('t=[1-9]+[a-z]*&', lbl_link)
                print(lbl_link)
                print('Reformat y= ' + str(y))
                if y is not None:
                    y = re.findall('t=[1-9]+[a-z]*&', lbl_link)
                    lbl_link = lbl_link.replace(str(y[0]), '')

                lbl_add = lbl_name + ' = ' + lbl_link
                lbl_clear_text.delete("1.0", "end-1c")
                lbl_clear_link.delete("1.0", "end-1c")
                print('dsad= ' + str(lbl_add))
                if len(links) == 0:
                    f.write(lbl_add)
                else:

                    f.write('\n' + lbl_add)
                f.close()

                f = open('parking_data/parking_cameras.txt', 'r')
                lines = f.readlines()
                lines[-1] = lines[-1].split(' = ')
                links.append(lines[-1])
                print('lungime= ' + str(len(links)))

                self.text_label.config(font=("Helvetica", 12), text='\n'.join(map(str, Extract1(links))))
                self.text_label2.config(font=("Helvetica", 12), text='\n'.join(map(str, Extract2(links))))

                self.mycanvas.update_idletasks()
                self.mycanvas.configure(scrollregion=self.mycanvas.bbox("all"))
                self.mycanvas.yview_moveto(1)

        def remove_link(lbl1, lbl2, lbl_clear_text):
            gasit_nume = 1
            for link in links:
                print(link[0])
                if link[0] == lbl1:
                    gasit_nume = 0
                # print(gasit_nume)

            if lbl1 == '':
                print('introdu text valid')
                lbl2.configure(text='Textul introdus este invalid', bg='red')
            elif gasit_nume == 1:
                print('Acest nume nu este gasit')
                lbl2.configure(text='Acest nume nu a fost gasit', bg='red')

            elif gasit_nume == 0:
                lbl2.configure(text='Textul introdus este corect', bg='green')
                for link in links:
                    if lbl1 == link[0]:

                        print('este egal lol')
                        links.remove(link)
                        print('lungime este egala cu ' + str(len(links)))
                        if len(links) == 0:
                            self.text_label.config(font=("Helvetica", 12),
                                                   text='Lista este goala. Va rugam introduceti un loc de parcare!')
                            self.text_label2.config(font=("Helvetica", 12), text='')
                        else:
                            self.text_label.config(font=("Helvetica", 12), text='\n'.join(map(str, Extract1(links))))
                            self.text_label2.config(font=("Helvetica", 12), text='\n'.join(map(str, Extract2(links))))

                        with open('parking_data/parking_cameras.txt', 'r+') as f:
                            lines = f.readlines()
                            print('lungimea fisierului= ' + str(len(lines)))
                            f.seek(0)
                            for line in lines:
                                to_check = line.split(' = ')
                                if len(lines) == 1 and to_check[0] == lbl1:
                                    f.truncate(0)

                                if to_check[0] != lbl1:
                                    print('linia: ' + str(line))
                                    # if lbl1 not in line:
                                    print('De verificat = ' + str(to_check[0]) + ' lbl1= ' + str(lbl1))
                                    # print(to_check[0])

                                    f.write(line)
                                    f.truncate()
                lbl_clear_text.delete("1.0", "end-1c")
                self.mycanvas.update_idletasks()
                self.mycanvas.configure(scrollregion=self.mycanvas.bbox("all"))

        self.button_remove = tk.Button(self, text='Șterge Camera',
                                       command=lambda: remove_link(self.text_box.get("1.0", "end-1c"),
                                                                   self.label_text2,
                                                                   self.text_box)
                                       )
        self.button_remove.config(height=1, width=30, bg='grey', font=("Helvetica", 12))
        self.button_remove.pack()

        self.label_text2 = tk.Label(self, text='')
        self.label_text2.config(font=("Helvetica", 12), padx='10', justify='left')
        self.label_text2.pack()

        self.label_delimitare2 = tk.Label(self)
        self.label_delimitare2.pack()
        self.label_delimitare2.config(height=1, width=100, text='Lista locurilor de parcare:', font=("Helvetica", 18),
                                      anchor='w', padx=10)

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

        self.wrapper1 = tk.LabelFrame(self)
        self.wrapper1.pack(fill='both', expand='yes', padx=10, pady=10)

        self.mycanvas = tk.Canvas(self.wrapper1)
        self.mycanvas.pack(side='left', fill='both', expand='yes')

        self.yscrollbar = ttk.Scrollbar(self.wrapper1, orient='vertical', command=self.mycanvas.yview)
        self.yscrollbar.pack(side='right', fill='y')

        self.mycanvas.configure(yscrollcommand=self.yscrollbar.set)

        self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion=self.mycanvas.bbox('all')))

        self.myframe = tk.Frame(self.mycanvas)
        self.mycanvas.create_window((0, 0), window=self.myframe, anchor='nw')

        # # tk.Button(self.myframe, text="My Button 1 ").pack()
        # self.text_label5 = tk.Label(self.myframe)
        # self.text_label5.config(anchor='n', text='ceau', justify='left', font=("Helvetica", 12))
        # self.text_label5.pack(side='left',anchor='nw')
        # self.text_label6 = tk.Label(self.myframe)
        # self.text_label6.config(text='ceau', justify='left', font=("Helvetica", 12))
        # self.text_label6.pack(side='left',anchor='nw')
        self.text_label = tk.Label(self.myframe)
        if links == []:

            self.text_label.config(anchor='n', justify='left', font=("Helvetica", 12),
                                   text='Lista este goală. Vă rugăm introduceți un loc de parcare!')
        else:
            self.text_label.config(anchor='n', justify='left', font=("Helvetica", 12),
                                   text='\n'.join(map(str, Extract1(links))))

        self.text_label.pack(side='left', fill='y')

        self.text_label2 = tk.Label(self.myframe)
        if not links:

            self.text_label2.config(padx=20, anchor='n', justify='left', font=("Helvetica", 12),
                                    text='')
        else:
            self.text_label2.config(padx=20, anchor='n', justify='left', font=("Helvetica", 12),
                                    text='\n'.join(map(str, Extract2(links))))

        self.text_label2.pack(side='left', fill='y')

        # self.text_label


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        label = tk.Label(self, text="", )
        label.config(font=("Courier", 10))
        label.pack(side="top", anchor='w')

        label = tk.Label(self, text="Manual de Utilizare")
        label.config(font=("Courier", 30, 'underline'))
        label.pack(side="top", anchor='w')

        label = tk.Label(self, text="", )
        label.config(font=("Courier", 14))
        label.pack(side="top", anchor='w')

        self.wrapper1 = tk.LabelFrame(self)
        self.wrapper1.pack(fill='both', expand='yes', padx=10, pady=10)

        self.mycanvas = tk.Canvas(self.wrapper1)
        self.mycanvas.pack(side='left', fill='both', expand='yes')

        self.yscrollbar = ttk.Scrollbar(self.wrapper1, orient='vertical', command=self.mycanvas.yview)
        self.yscrollbar.pack(side='right', fill='y')

        self.mycanvas.configure(yscrollcommand=self.yscrollbar.set)

        self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion=self.mycanvas.bbox('all')))

        self.myframe = tk.Frame(self.mycanvas)
        self.mycanvas.create_window((0, 0), window=self.myframe, anchor='nw')

        label = tk.Label(self.myframe, text="1.Pornire Cameră", )
        label.config(font=("Courier", 30))
        label.pack(side="top", anchor='w')
        label2 = tk.Label(self.myframe, text="Pentru pornirea unei camere, se accesează meniul principal(Program)\nși "
                                             "se introduce linkul(URL-ul complet) de la parcarea dorită.\nSe "
                                             "accesează butonul Pornește Camera pentru "
                                             "procesarea linkului.", justify='left')
        label2.config(font=("Courier", 14))
        label2.pack(side="top", anchor='w')
        label = tk.Label(self.myframe, text="2.Schemă de Parcare Nouă", )
        label.config(font=("Courier", 30))
        label.pack(side="top", anchor='w')
        label2 = tk.Label(self.myframe,
                          text="Pentru a realiza o schemă de parcare nouă, se accesează\nmeniul principal(Program) și "
                               "se introduce linkul(URL-ul complet)\nde la parcarea dorită.\nSe accesează butonul "
                               "Schemă de Parcare Nouă pentru\na înregistra manual locurile de parcare.",
                          justify='left')
        label2.config(font=("Courier", 14))
        label2.pack(side="top", anchor='w')

        label = tk.Label(self.myframe, text="3.Marcare loc de parcare", )
        label.config(font=("Courier", 30))
        label.pack(side="top", anchor='w')
        label2 = tk.Label(self.myframe,
                          text="Pentru marcarea locurilor de parcare, se apasă dublu-click\npe fiecare colț al "
                               "locului de parcare pentru a-l marca corespunzător.\nLa terminarea marcării unui loc "
                               "de parcare, acesta devine vizibil\nși este posibilă marcarea unui loc de parcare nou.",
                          justify='left')
        label2.config(font=("Courier", 14))
        label2.pack(side="top", anchor='w')

        label = tk.Label(self.myframe, text="4.Pornire Camere", )
        label.config(font=("Courier", 30))
        label.pack(side="top", anchor='w')
        label2 = tk.Label(self.myframe, text="Pentru pornirea tuturor camerelor, se accesează meniul Parcare "
                                             "Multiplă\nși se "
                                             "accesează butonul Pornește Toate Camerele.\n"
                                             "Programul afișează toate camerele disponibile din\nLista Locurilor de "
                                             "Parcare",
                          justify='left')
        label2.config(font=("Courier", 14))
        label2.pack(side="top", anchor='w')

        label = tk.Label(self.myframe, text="5.Adaugă Cameră", )
        label.config(font=("Courier", 30))
        label.pack(side="top", anchor='w')
        label2 = tk.Label(self.myframe,
                          text="Pentru a adăuga o cameră de parcare nouă, se accesează\nmeniul Parcare Multiplă "
                               "și se introduce linkul(URL-ul complet)\nși numele parcării dorite.\nSe acceasează"
                               " butonul Adaugă Camera pentru înregistrarea linkului\nși a numelui. "
                          ,
                          justify='left')
        label2.config(font=("Courier", 14))
        label2.pack(side="top", anchor='w')

        label = tk.Label(self.myframe, text="6.Șterge Camera", )
        label.config(font=("Courier", 30))
        label.pack(side="top", anchor='w')
        label2 = tk.Label(self.myframe,
                          text="Pentru a șterge o cameră de parcare, se accesează\nmeniul Parcare Multiplă "
                               "și se introduce numele parcării dorite.\nSe acceasează"
                               " butonul Șterge Camera pentru ștergerea linkului\nși a numelui parcării. "
                          ,
                          justify='left')
        label2.config(font=("Courier", 14))
        label2.pack(side="top", anchor='w')

        label = tk.Label(self.myframe, text="7.Pornire Server", )
        label.config(font=("Courier", 30))
        label.pack(side="top", anchor='w')
        label2 = tk.Label(self.myframe,
                          text="Pentru a porni Serverul, se accesează meniul principal(Program)\n"
                               "și se apasă butonul Pornire Server.\nLa accesarea butonului, utilizatorii au "
                               "posibilitatea de a primi mesaje\nprin intermediul aplicației de mesagerie. "
                          ,
                          justify='left')
        label2.config(font=("Courier", 14))
        label2.pack(side="top", anchor='w')


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
        b2 = tk.Button(buttonframe, text="Parcare Multiplă", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Manual de Utilizare", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()

    root.iconbitmap('smart_parking_short.ico')
    root.title('Smart Parking')
    root.resizable(False, False)

    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1100x900")

    root.mainloop()
