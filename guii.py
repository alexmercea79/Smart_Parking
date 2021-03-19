import tkinter as tk
import webbrowser
from threading import *

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()



def threading_local_server():
    # Call work function
    t1=Thread(target=start_local_server)
    t1.start()



def start_local_server():
    import LocalServer
    webbrowser.open('http://127.0.0.1:5000/sms', new=1)
    LocalServer.run_app()


def threading_detections(text):

    t2 = Thread(target=retrieve_input(text))
    t2.start()


def retrieve_input(text):
    print(text)
    import detections

    detections.detections_working(text)


    # label = tk.Label(self, text="This is page 1")
    # label.pack(side="top", fill="both", expand=True)

def drawing():
    print()
    import detections

    detections.draw()


    # label = tk.Label(self, text="This is page 1")
    # label.pack(side="top", fill="both", expand=True)


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.label=tk.Label(self,text='Introduceti linkul camerei de supravegheat:')
        self.label.grid(row=1,column=3)
        self.text = tk.Text(self, height=1, width=60)
        self.text.grid(row=2, column=3)
        self.button = tk.Button(self, text='Click Here To Start', command=lambda: threading_detections(self.text.get("1.0", "end-1c")))
        self.button.grid(row=3, column=3)
        self.button2 = tk.Button(self, text='Apasati aici pentru a porni Serverul',
                                command=threading_local_server)
        self.button2.grid(row=4, column=3)
        self.label2 = tk.Label(self, text='sa ma bei')
        self.label2.grid(row=5, column=3)
        self.button3 = tk.Button(self, text='Apasati aici pentru a realiza din nou schema de parcare',
                                 command=drawing)
        self.button3.grid(row=6, column=3)


class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

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

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Smart Parking')
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x600")
    root.mainloop()